from time import sleep

import requests

def hehe(proxy):
    pap = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json; encoding=utf8",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "referrerPolicy": "strict-origin-when-cross-origin"
    }
    
    proxie = {'https': proxy}
    print(proxie)
    hehe = {"exhibition":"63ee43d8004f09ca3666ff17"}
    try:
        haha = requests.post('https://www.artsteps.com/api/views', proxies=proxie, headers=pap, json=hehe, timeout=30)
        print(haha.json())
    except:
        print('dead proxy')
 


def getallproxy():
    proxhttps = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies.json')
    return proxhttps.json()['https']

while (True):
    for allprox in getallproxy():
      sleep(5)
      print('sleep 5s')
      hehe(allprox)
