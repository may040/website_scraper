#!/usr/bin/python3
import re

from ThesisPython.Thesis import *
from ThesisPython.Scraping import *

TYP_BACHELORTHESIS ="Bachelorarbeit"

urlBaMa = "https://pp.info.uni-karlsruhe.de/theses.php"
urlBaMaLook = "https://pp.info.uni-karlsruhe.de/"

urlInstitut="https://pp.info.uni-karlsruhe.de/"
shortname = "PROPA"

soupBaMa = ScrapingHelper(urlBaMa).getSoup()
thesisList = soupBaMa.find(attrs={"class": "ipdtable"})

group = ResearchGroup("",shortname,"Informatik")
group.url = urlInstitut

if(thesisList!=None):
    entries = thesisList.find_all("td")
    for i in range(0,len(entries),2):
        title = entries[i+1].getText().replace('\n',"").replace('\t',"").rstrip(" ")
        t = Thesis(title,extractType(entries[i].getText()))
        t.url= joinURL(urlBaMaLook,entries[i+1].find("a").get("href"))
        group.addThesis(t)

group.serialize()



