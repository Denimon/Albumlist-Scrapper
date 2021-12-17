from os import close
import re


discogs = open("10967-250.html", encoding="utf-8")
txt = discogs.read()
discogsList = re.findall(r'<div class="listitem_number">\s*(.*)\s*</div>\s*<h3 class="listitem_title.*\s*<a href=".*">(.*)</a>',txt)

print(discogsList)
#for record in discogsList:
#    print(record)

discogs.close()

popvortex = open("popvortex100", encoding="utf-8")
txt2 = popvortex.read()
popvortexList = re.findall(r'</tr><tr><td>([0-9]*.)</td><td><a href=".*?.php">(.*?)</a></td><td>(.*?)</td><td>',txt2)
print(popvortexList)
#for record2 in popvortexList:
#   print(record2)

popvortex.close()

rollingstone1 = open("rollingstone1-50.html", encoding="utf-8")
txt3= rollingstone1.read()
rollingstoneOneToFifty = re.findall(r'class="html-attribute-value">position</span>"&gt;</span>([0-9]*)<span.*?<span class="html-attribute-value">url</span>"&gt;</span>(.*?)<span class="html-tag">&lt;/a&gt;</span>',txt3) 
print("-------------------------Rollingstone 1-50--------------------------")
print(rollingstoneOneToFifty)

rollingstone1.close()


rollingstone2 = open("rollingstone51-100.html", encoding="utf-8")
txt4= rollingstone2.read()
rollingstoneFiftyToHundred = re.findall(r'class="html-attribute-value">position</span>"&gt;</span>([0-9]*)<span.*?<span class="html-attribute-value">url</span>"&gt;</span>(.*?)<span class="html-tag">&lt;/a&gt;</span>',txt4) 
print("-------------------------Rollingstone 50-100--------------------------")
print(rollingstoneFiftyToHundred)

rollingstone2.close()