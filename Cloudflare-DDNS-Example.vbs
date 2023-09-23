Dim ws
Set ws = Wscript.CreateObject("Wscript.Shell")
ws.Run "python.exe C:\Server\Cloudflare-DDNS\Cloudflare-DDNS.py",vbhide
Wscript.quit
