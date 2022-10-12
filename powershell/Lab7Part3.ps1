#3. Creating a PDF with Text
New-PDF{
New-PDFText -Text 'Hello ', 'World' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
} -FilePath "C:\it3038c-scripts\powershell\Lab7Part3PDF.pdf" -Show
