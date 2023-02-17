strComputer = “.”

Set objWMIService = GetObject(“winmgmts:\\” & strComputer & “\root\default”)
Set colEvents = objWMIService.ExecNotificationQuery _
    (“SELECT * FROM RegistryKeyChangeEvent WHERE Hive=’HKEY_LOCAL_MACHINE’ AND ” & _
        “KeyPath=’SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'”) 
Do
    Set objLatestEvent = colEvents.NextEvent
    Wscript.Echo Now & “: The registry has been modified.”
Loop