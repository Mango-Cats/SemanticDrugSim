# Get zip files of PubMed data and extract all XML files from them 
#   into an output directory.
# By: Zhean Ganituen (zrygan)
# On: August 2025
$scriptFolder = Split-Path -Parent $MyInvocation.MyCommand.Definition

$inputFolder = $scriptFolder

$outputFolder = Join-Path $scriptFolder "pubmed_xml"

if (-not (Test-Path $outputFolder)) {
    New-Item -ItemType Directory -Path $outputFolder
}

$gzFiles = Get-ChildItem -Path $inputFolder -Filter "pubmed25n*.xml.gz"

foreach ($gzFile in $gzFiles) {
    $outputFile = Join-Path $outputFolder ($gzFile.BaseName)
    Write-Host "Decompressing $($gzFile.Name) -> $outputFile"

    $inStream = [System.IO.Compression.GzipStream]::new(
        [System.IO.File]::OpenRead($gzFile.FullName),
        [System.IO.Compression.CompressionMode]::Decompress
    )
    $outStream = [System.IO.File]::Create($outputFile)
    $inStream.CopyTo($outStream)

    $inStream.Close()
    $outStream.Close()
}

Write-Host "All files decompressed successfully into $outputFolder"
