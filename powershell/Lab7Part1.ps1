#1. Merging a PDF
$file1="C:\it3038c-scripts\powershell\Document1.pdf"
$file2="C:\it3038c-scripts\powershell\Document2.pdf"

$MergedFile="C:\it3038c-scripts\powershell\MergedDoc.pdf"

Merge-PDF -InputFile $file1, $file2 -OutputFile $MergedFile