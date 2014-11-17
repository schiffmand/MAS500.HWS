# Code that retrieves the election data from the assignment
from bs4 import BeautifulSoup
import urllib2
election = "http://www.archives.gov/federal-register/electoral-college/2012/popular-vote.html"
page = urllib2.urlopen(election)
soup = BeautifulSoup(page)
#print soup('table')[0].prettify()
#f = csv.writer(open("electionresults.csv","w"))
#f.writerow(["State", "Democratic", "Repub", "Lib", "Green", "Others", "TotalVotes"])


State=""
Democratic=""
Republican=""
Libertarian=""
Green=""
Others=""
TotalVotes=""
table = soup.find("table cellspacing")
for table in t:
	trs=soup.find_all('tr')
	for tr in trs:
		print tr

#table = soup.find("table")
#for table in t:
#	rows = table.findAll('tr')
# 	for tr in rows:
# 		cols=tr.findAll('td')
# 		for td in cols:
# 			g.write(td.find(text=True))
# 			g.write(",")
# 		g.write("\n")
 		
 			
#for row in soup('table')[0].findAll('tr'):
#cells = row.findAll("td")
#For each "tr" assign a td
#State=cells[1].find(text=True)
#Democratic=cells[2].find(text=True)
#Republican=cells[3].find(text=True)
#Libertarian=cells[4].find(text=True)
#Green=cells[5].find(text=True)
#Others=cells[6].find(text=True)
#TotalVotes=cells[7].find(text=True)



