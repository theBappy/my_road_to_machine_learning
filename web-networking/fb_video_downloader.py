import os
import re
import requests
import wget

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "downloads")
if not os.path.exists(path):
    os.mkdir(path)

link = input("Enter the of the video to download: ")
try:
    r = requests.get(link)
    if r.status_code == requests.codes.ok:
        try:
            sd_url = re.search('sd_src:"(.+?)"',r.text)[1]
            url = (
                re.search('hd_src:"(.+?)"', r.text)[1] if "hd_src" in r.text else sd_url
            )
            print("Downloading...")
            wget.download(url, path)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
    