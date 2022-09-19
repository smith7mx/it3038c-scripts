function getIP{
(Get-NetIPAddress).ipv4address | Select-String "192*"
}
$IP=getIP
function getAdmin{
whoami
}
$User=getAdmin
function getHost{
hostname
}
$Host1=getHost
function getVersion{
$PSVersionTable.PSVersion.Major
}
$Version=(getVersion)
function getDate{
Get-Date
}
$Date=(getDate)
$BODY=("This machine's IP is $IP. User is $User. Hostname is $Host1. 
Powershell Version $Version. Today's Date is $Date.")
$BODY | Out-File C:\it3038c-scripts\powershell\Lab3Script.txt