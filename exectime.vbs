Set oShell = CreateObject ("Wscript.Shell")
Dim srtArgs
strArgs = "cmd /c exectime.bat"
oShell.Run strArgs, 0, false