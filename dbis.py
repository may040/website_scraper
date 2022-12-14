#!/usr/bin/python3
import re
from ThesisPython.Thesis import *
from ThesisPython.Scraping import *

# TYP_HIWI_SPACE="Wissenschaftlicher Mitarbeiter/Wissenschaftliche Mitarbeiterin "
urlBaMa = "https://dbis.ipd.kit.edu/2798.php"
# urlHIWI= "https://dbis.ipd.kit.edu/2814.php"
urlInstitut="https://dbis.ipd.kit.edu/2793.php"
shortname = "DBIS"

soupBaMa = ScrapingHelper(urlBaMa).getSoup()
wholeList = soupBaMa.find(attrs={"id": "table_1217"})

# soupHIWI = ScrapingHelper(urlHIWI).getSoup()
# hiwiList = soupHIWI.find(attrs={"id": "table_1832"})

group = ResearchGroup("", shortname, "Informatik")
group.url = urlInstitut

if(wholeList!=None):
    entries = soupBaMa.find_all("td")
    for i in range(0,len(entries),3):
        title = entries[i].getText()
        t = Thesis(title, extractType(entries[i+1].getText()))
        t.url= joinURL(urlBaMa,entries[i].find("a").get("href"))
        group.addThesis(t)

"""
if(hiwiList!=None):
    tableContent = soupHIWI.tbody.find_all("td")
    for i in range(0,len(tableContent),2):
        if (TYP_HIWI_SPACE) in tableContent[i].getText():
            title = tableContent[i].getText().replace(TYP_HIWI_SPACE,"")
            t = Thesis(title, ThesisType.HIWI)
            t.url = joinURL(urlHIWI, tableContent[i].find("a").get("href"))
            group.addThesis(t)
"""

group.serialize()

