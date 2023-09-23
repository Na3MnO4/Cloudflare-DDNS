# Cloudflare-DDNS
Lightweight IPv4 Address Update Tool For Cloudflare

# Configuration
Download and extract the source code

Open "Cloudflare-DDNS.py"

Input your own API Token with Edit Zone DNS permission in api_token
  
e.g. 
  
    api_token = "input-your-own-edit-zone-dns-api-token"
  
Input your Domain Name(s) and the corresponding Record Name(s) in "domain_record_dict"
  
e.g. 
  
    domain_record_dict = {
    "domain1.com": "record1",
    "domain2.org": "record2"
    }
  
Change the interval of every check, the default value is 600 seconds(10 minutes) in time.sleep()
  
e.g.
  
    time.sleep(600)

# Deploy Self-Start
Windows

Edit the path of your py file in the vbs script

e.g.

    Dim ws
    Set ws = Wscript.CreateObject("Wscript.Shell")
    ws.Run "python.exe C:\Server\Cloudflare-DDNS\Cloudflare-DDNS.py",vbhide
    Wscript.quit

Copy a shortcut of the vbs script in the shell:startup dictionary by entering shell:startup in Win+R
