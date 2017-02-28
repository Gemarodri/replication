#!/usr/bin/python
# Script to get the Developer, the Id in Launchpad, the Classification, and the Repository 
import json
import os,sys

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "~/Horizon"
filesname = os.listdir( path )
tickAnal= len(filesname)
bugs=[]
notBugs=[]
undefined=[]

#Open File
bugsFile = open("Nellysek_BugsHorizon","wb")
bugsFile.write('[')
for file in filesname:
	if file!= '.git':
		fn = os.path.join(path, file)
		f= open(fn, 'r')
		content = f.read()
		print(file)
		data= json.loads(content)
		if data["Classification"]== "Bug":
			bugs.append(file)
			#Write the Bugs
			revisor= file.split("_")
			if revisor[1]=='DOREALDA DALIPAJ':
				revisor[1]='DDALIPAJ'
			bugsFile.write('"'+revisor[0]+'_'+revisor[1]+'"'+",")
		elif data["Classification"] == "Not_Bug":
			notBugs.append(file)
		else:
			undefined.append(file)
numBugs= len(bugs)*100/tickAnal
numNotBugs= len(notBugs)*100/tickAnal
numUndefi= len(undefined)*100/tickAnal
print 'Statistics are:', len(bugs), len(notBugs), len(undefined)
print 'In percentage:', numBugs, numNotBugs, numUndefi

#Close File
bugsFile.write(']')
bugsFile.close()
