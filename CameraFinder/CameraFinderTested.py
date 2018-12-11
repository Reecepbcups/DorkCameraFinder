## Reecepbcups - December 10th, 2018
## Discord: Reecepbcups#3370

# Less efficent than the Beta, but more reliable. use ''' for each dork. Most can be found on Exploit db > dorks > "camera"
# https://www.exploit-db.com/google-hacking-database

from googlesearch import search 
import requests

ips = []

def get():
  q = ["""inurl:indexFrame.shtml Axis""",
  '''inurl:view/view.shtml?videos''',
  '''inurl:”CgiStart?page=”''',
  '''inurl:/view.shtml''',
  '''inurl:ViewerFrame?M0de=''',
  '''inurliaxis-cgi/jpg''',
  '''intitle:”live view” intitle:axis''',
  '''intitle:”Live NetSnap Cam-Server feed”''',
  '''intitle:”Live View/ — AXIS 210?''',
  '''intitleisnc-220 inurl:home/''',
  '''intitle:”Toshiba Network Camera” user Iogin''',
'''jpegpull.htm''']

  for query in q:
    try:
      for j in search(query, tld="com", num=100, stop=1, pause=1): 
        ips.append(j)
    except:
      print('failed on: ' + query)
      pass

def d():
  for item in ips:
    if 'alibaba' not in item:
      if 'gov' not in item:
        if 'edu' not in item:
          if 'amazon' not in item:
            if 'ebay' not in item:
              if 'shop' not in item:
                with open('ips.txt', 'a') as f:
                  f.write(item + "\n\n")
                  f.close()

    if 'gov' in item:
      with open('gov_sites.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()

    if 'edu' in item:
      with open('edu_sites.txt', 'a') as f:
        f.write(item + "\n\n")
        f.close()
