from urllib.request import Request, urlopen
from collections import OrderedDict
import re, os

def page_downloader(link, path):
    if os.path.isfile(path):
        return 1
    try : 
        req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(req).read()
        mydata = webpage.decode("utf8")
        f=open(path,'w',encoding="utf-8")
        f.write(mydata)
        f.close
        return 1
    except : 
        return 0