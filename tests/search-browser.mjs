import { chromium } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { mkdir, writeFile, readFile, stat } from 'node:fs/promises';
import assert from 'node:assert/strict';

const prefix = process.env.SEARCH_BASEURL || '';
const origin = process.env.SEARCH_ORIGIN || 'http://127.0.0.1:8765';
const output = `artifacts/search${prefix ? '-staging' : ''}`;
await mkdir(output, {recursive: true});
const browser = await chromium.launch({headless:true,
  ...(process.env.CHROMIUM_PATH ? {executablePath:process.env.CHROMIUM_PATH} : {})});
const context = await browser.newContext({viewport:{width:1440,height:1000}});
const page = await context.newPage();
const failures = [];
page.on('pageerror', error => failures.push(error.message));
page.on('response', response => {if (response.status() >= 400 && response.url().startsWith(origin)) failures.push(`${response.status()} ${response.url()}`);});
try {
  await page.goto(`${origin}${prefix}/search/`);
  await page.locator('.pagefind-ui__search-input').waitFor();
  const inventory = await page.evaluate(async prefix => {
    const engine = await import(`${prefix}/pagefind/pagefind.js`);
    await engine.options({baseUrl: `${prefix}/`});
    const response = await engine.search(null);
    return {filters:await engine.filters(), results:await Promise.all(response.results.map(r=>r.data()))};
  }, prefix);
  assert(inventory.results.length > 300, 'expected public historical and organizational coverage');
  const urls = inventory.results.map(r=>r.url);
  assert.equal(new Set(urls).size, urls.length, 'duplicate page URLs');
  const redirects = JSON.parse(await readFile('docs/baselines/redirects.json','utf8'));
  for (const result of inventory.results) {
    assert(result.meta.title?.trim(), `missing title ${result.url}`);
    const url = new URL(result.url, origin);
    assert(url.pathname.startsWith(`${prefix}/`), `baseurl ${result.url}`);
    const path = url.pathname.slice(prefix.length);
    assert(!/^\/(audit|docs|scripts|tests|artifacts|vendor|node_modules|_pending|_unused|search)(\/|$)/.test(path), path);
    assert(!Object.keys(redirects).some(r=>path === `/${r}`), `redirect indexed ${path}`);
    if (!process.env.SEARCH_HOSTED) await stat(`_site${decodeURIComponent(path)}${path.endsWith('/') ? 'index.html' : ''}`);
  }
  for (const filter of ['Category','Record type','Year']) assert(inventory.filters[filter], `missing ${filter}`);
  const tasks = JSON.parse(await readFile('tests/search-tasks.json','utf8'));
  const benchmarks = [];
  for (const task of tasks) {
    const found = await page.evaluate(async ({prefix,task}) => {
      const engine = await import(`${prefix}/pagefind/pagefind.js`);
      const start = performance.now();
      const r = await engine.search(task.query, task.filters ? {filters:task.filters} : {});
      const data = await Promise.all(r.results.slice(0,10).map(r=>r.data()));
      return {milliseconds:Math.round(performance.now()-start), results:data.map(r=>({url:r.url,title:r.meta.title,excerpt:r.excerpt}))};
    }, {prefix,task});
    const rank = found.results.findIndex(r=>new URL(r.url,origin).pathname.slice(prefix.length).includes(task.path));
    assert(rank >= 0, `${task.query}: expected ${task.path} in top ten: ${JSON.stringify(found.results)}`);
    assert(found.results[rank].excerpt, `${task.query}: missing excerpt`);
    benchmarks.push({...task,rank:rank+1,...found});
  }
  // Submit the real header form with keyboard, then exercise UI filters.
  await page.locator('#header-search').fill('Special Project');
  await page.locator('#header-search').press('Enter');
  await page.locator('.pagefind-ui__result-link').first().waitFor();
  assert(new URL(page.url()).searchParams.get('q') === 'Special Project');
  assert(await page.locator('.pagefind-ui__search-input').inputValue() === 'Special Project');
  await page.screenshot({path:`${output}/desktop.png`,fullPage:true});
  const axe = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
  assert.deepEqual(axe.violations.map(v=>({id:v.id,help:v.help,nodes:v.nodes.map(n=>n.target)})), [], 'search accessibility violations');
  const checks = [];
  for (const width of [390,320]) {
    await page.setViewportSize({width,height:844});
    assert(await page.locator('#header-search').isVisible(), 'mobile header search visible');
    assert(await page.evaluate(()=>document.documentElement.scrollWidth <= innerWidth), `overflow at ${width}`);
    await page.screenshot({path:`${output}/mobile-${width}.png`,fullPage:true});
    checks.push({width,overflow:false});
  }
  await page.locator('.pagefind-ui__search-input').fill('quokkanonexistentphrase extraterrestrialunknown');
  await page.waitForFunction(()=>document.querySelector('.pagefind-ui__message')?.textContent.trim().startsWith('No results'));
  assert.equal(await page.locator('.pagefind-ui__result-link:visible').count(),0);
  const filterLabel = page.locator('.pagefind-ui__filter-name').first();
  await filterLabel.click();
  const checkbox = page.locator('.pagefind-ui__filter-value input').first();
  await checkbox.focus();
  await checkbox.press('Space');
  assert(await checkbox.isChecked(), 'keyboard filter toggle');
  const nojs = await browser.newContext({javaScriptEnabled:false});
  const fallback = await nojs.newPage();
  await fallback.goto(`${origin}${prefix}/search/`);
  assert(await fallback.locator('noscript p').isVisible(), 'no-JavaScript explanation');
  assert(await fallback.getByRole('link',{name:'all pages',exact:true}).isVisible(), 'browse fallback');
  await nojs.close();
  const unavailable = await context.newPage();
  await unavailable.route('**/pagefind/pagefind-ui.js', route=>route.abort());
  await unavailable.goto(`${origin}${prefix}/search/`);
  await unavailable.getByText('Search could not load.',{exact:false}).waitFor();
  await unavailable.close();
  const home = await context.newPage();
  await home.goto(`${origin}${prefix}/`);
  await home.screenshot({path:`${output}/home-desktop.png`,fullPage:true});
  await home.setViewportSize({width:390,height:844});
  assert(await home.evaluate(()=>document.documentElement.scrollWidth <= innerWidth), 'mobile homepage overflow');
  await home.screenshot({path:`${output}/home-mobile.png`,fullPage:true});
  await home.close();
  assert.deepEqual(failures,[]);
  await writeFile(`${output}/results.json`,JSON.stringify({indexed:urls.length,filters:inventory.filters,benchmarks,checks,axeViolations:0,errors:failures},null,2));
  console.log(`PASS: ${urls.length} indexed public pages, ${tasks.length} search tasks, baseurl '${prefix}', desktop/mobile, keyboard and axe`);
} finally { await browser.close(); }
