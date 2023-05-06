Dim ws
Set ws = Wscript.CreateObject("Wscript.Shell")
ws.Run "python.exe ./Cloudflare-DDNS.py",vbhide
Wscript.quit
