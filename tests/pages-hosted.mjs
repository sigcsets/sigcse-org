import { chromium } from '@playwright/test';
import assert from 'node:assert/strict';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
const origin = 'https://sigcsets.github.io';
const prefix = '/sigcse-org';
const base = origin + prefix;
const output = 'artifacts/hosted';
await mkdir(output,{recursive:true});
const browser = await chromium.launch({headless:true});
const context = await browser.newContext({viewport:{width:1440,height:1000}});
await context.route('**/*', async route => {
  const host = new URL(route.request().url()).hostname;
  if (['sigcse.org','www.sigcse.org'].includes(host)) {
    await route.abort();
    throw new Error('Unexpected ACM production request');
  }
  await route.continue();
});
const page = await context.newPage();
const report = {pages:[],downloads:[],redirects:[],excluded:[],wasm:[],errors:[]};
page.on('pageerror',e=>report.errors.push(e.message));
page.on('response',r=>{if(r.url().includes('/pagefind/wasm.')) report.wasm.push({url:r.url(),status:r.status()});});
try {
  const paths = ['/', '/conferences/', '/membership/', '/programs/awards/', '/funding/', '/resources/', '/governance/', '/policies/', '/programs/awards/outstanding.html', '/about/reports/board.html', '/events/symposia/2010.html', '/search/'];
  for (const path of paths) {
    const response = await page.goto(base+path);
    assert.equal(response.status(),200,path);
    assert(page.url().startsWith(base+'/'),page.url());
    assert((await page.locator('meta[name=robots]').getAttribute('content')).includes('noindex'),path);
    for (const width of [1440,390,320]) {
      await page.setViewportSize({width,height:width===1440?1000:844});
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`${path}: overflow ${width}`);
      assert.deepEqual(await page.locator('img').evaluateAll(imgs=>imgs.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)),[],`${path}: broken images`);
      if (['/','/conferences/','/programs/awards/outstanding.html','/about/reports/board.html'].includes(path))
        await page.screenshot({path:`${output}/${path.replaceAll('/','_')||'home'}-${width}.png`,fullPage:true});
    }
    if(path==='/') {
      const links=await page.locator('nav[aria-label="Main navigation"] a').evaluateAll(as=>as.map(a=>a.href));
      assert(links.length>=7,'primary navigation');
      for(const url of links) {assert(url.startsWith(base+'/'),url);assert((await context.request.get(url)).ok(),url);}
    }
    if(path==='/about/reports/board.html') {
      const urls=await page.locator('main a[href$=".pdf"]').evaluateAll(as=>as.slice(0,2).map(a=>a.href));
      assert.equal(urls.length,2);
      const baseline=JSON.parse(await readFile('docs/baselines/public-files.json','utf8'));
      for(const url of urls) {
        assert(url.startsWith(base+'/'),url);
        const r=await context.request.get(url);assert.equal(r.status(),200);
        assert((r.headers()['content-type']||'').includes('application/pdf'));
        const data=await r.body();assert(data.subarray(0,5).toString()==='%PDF-');
        const name=decodeURIComponent(new URL(url).pathname.slice(prefix.length+1));
        assert.equal(createHash('sha256').update(data).digest('hex'),baseline[name].sha256);
        report.downloads.push({url,status:r.status(),bytes:data.length,sha256:baseline[name].sha256});
      }
    }
    report.pages.push({path,status:200,widths:[1440,390,320]});
  }
  const redirects=JSON.parse(await readFile('docs/baselines/redirects.json','utf8'));
  for(const [from,to] of Object.entries(redirects)) {
    await page.goto(base+'/'+from);
    await page.waitForURL(base+'/'+to);
    report.redirects.push({from,to,url:page.url()});
  }
  await page.goto(base+'/search/');
  await page.locator('.pagefind-ui__search-input').fill('Mitchel Resnick');
  await page.locator('.pagefind-ui__result-link').first().waitFor();
  assert(report.wasm.some(r=>r.status===200),'actual WASM network response');
  const forbidden=['AGENTS.md','README.md','MAINTAINING.md','Gemfile','Gemfile.lock','package.json','pnpm-lock.yaml','CNAME','_config.yml','_config_github_pages.yml','docs/PROJECT_STATUS.md','audit/CONTENT_INVENTORY.csv','scripts/build.rb','tests/search-browser.mjs','artifacts/validation.json','_pending/','_unused/','.git/config','content/organization/index.md'];
  for(const name of forbidden) {const r=await context.request.get(base+'/'+name);assert.equal(r.status(),404,name);report.excluded.push({path:name,status:r.status()});}
  const robots=await context.request.get(base+'/robots.txt');assert((await robots.text()).includes('Disallow: /'));
  assert.deepEqual(report.errors,[]);
  console.log(`PASS: hosted ${report.pages.length} pages, desktop/mobile, ${report.redirects.length} redirects, PDFs, WASM and ${forbidden.length} exclusions`);
} finally {
  await writeFile(`${output}/results.json`,JSON.stringify(report,null,2));
  await browser.close();
}
