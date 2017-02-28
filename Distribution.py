import json
import os,sys
import csv

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "/home/gerope/PhD/EmpiricalStudy/Data/Deleting_Noise/Neutron"
filesname = os.listdir( path )
tickAnal= len(filesname)
responsibles1=0
responsiblesmore=0
no_Responsibles1=0
no_Responsiblesmore=0
undef=0
total=0
totalunde1 = 0
totalundemore = 0
ticketDeleted=0
total1 = 0
totalmore = 0

for file in filesname:
	if file!= '.git':
		fn = os.path.join(path, file)
		f= open(fn, 'r')
		content = f.read()
		data= json.loads(content)
		prevCommits = data["CommitPrevious"].split("\n")
		numCommRespon = data["N_responsible"]
		#if prevCommits[0]!="":
		if len(prevCommits)==1:
			total1 = total1 +1
			if numCommRespon != "NSNC":
				if int(numCommRespon) == 1:
					responsibles1=responsibles1+1
				elif int(numCommRespon) == 0:
					no_Responsibles1=no_Responsibles1+1
			elif numCommRespon == "NSNC":
				totalunde1=totalunde1+1
		elif len(prevCommits)>1:
			totalmore=totalmore +1
			if numCommRespon != "NSNC":
				#print int(numCommRespon)
				if int(numCommRespon) >=1:
					responsiblesmore=responsiblesmore+1
				elif int(numCommRespon) == 0:
					no_Responsiblesmore=no_Responsiblesmore+1
			elif numCommRespon == "NSNC":
				totalundemore=totalundemore+1

print "Un commit", total1,responsibles1,no_Responsibles1, totalunde1,"Mas de un commit", totalmore,responsiblesmore,no_Responsiblesmore, totalundemore