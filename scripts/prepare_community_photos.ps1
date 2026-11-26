# Optional, mechanical display-size derivatives. Original archival files stay intact.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$sigcseRoot = Split-Path $PSScriptRoot -Parent
$sigcseOutput = Join-Path $sigcseRoot 'assets/images/community'
New-Item -ItemType Directory -Force $sigcseOutput | Out-Null
$sigcseSources = @{
  'attendees.jpg' = 'assets/images/home/teaching copy.jpg'
  'celebration.jpg' = 'assets/images/home/exhibits copy.jpg'
  'first-timers.jpg' = 'about/bulletin/bulletin.58.2/SIGCSETS-first-timers.png'
  'board-retreat.jpg' = 'about/bulletin/Bulletin.58.4/SIGCSE Board.jpeg'
}
$sigcseEncoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
foreach ($sigcseName in $sigcseSources.Keys) {
  $sigcseImage = [System.Drawing.Image]::FromFile((Join-Path $sigcseRoot $sigcseSources[$sigcseName]))
  $sigcseWidth = [Math]::Min(1200, $sigcseImage.Width)
  $sigcseHeight = [int]([Math]::Round($sigcseImage.Height * $sigcseWidth / $sigcseImage.Width))
  $sigcseBitmap = [System.Drawing.Bitmap]::new($sigcseWidth, $sigcseHeight)
  $sigcseGraphics = [System.Drawing.Graphics]::FromImage($sigcseBitmap)
  $sigcseGraphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $sigcseGraphics.DrawImage($sigcseImage, 0, 0, $sigcseWidth, $sigcseHeight)
  $sigcseParameters = [System.Drawing.Imaging.EncoderParameters]::new(1)
  $sigcseParameters.Param[0] = [System.Drawing.Imaging.EncoderParameter]::new([System.Drawing.Imaging.Encoder]::Quality, [long]85)
  $sigcseBitmap.Save((Join-Path $sigcseOutput $sigcseName), $sigcseEncoder, $sigcseParameters)
  $sigcseParameters.Dispose(); $sigcseGraphics.Dispose(); $sigcseBitmap.Dispose(); $sigcseImage.Dispose()
}
