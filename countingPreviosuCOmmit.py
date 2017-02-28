import json
import os,sys
import csv

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "/home/gerope/PhD/EmpiricalStudy/Data/PrevCommitHorizon"
filesname = os.listdir( path )
tickAnal= len(filesname)
responsibles=0
no_Responsibles=0
undef=0
total=0
ticketDeleted=0

for file in filesname:
	if file!= '.git':
		fn = os.path.join(path, file)
		f= open(fn, 'r')
		content = f.read()
		data= json.loads(content)
		prevCommits = data["CommitPrevious"].split("\n")
		#numCommRespon = data["N_responsible"]
		if prevCommits[0]!="":
			total=total+len(prevCommits)
			if numCommRespon != "NSNC":
				responsibles= responsibles+int(numCommRespon)
				no_Responsibles= no_Responsibles + (len(prevCommits)-int(numCommRespon))
			else:
			 	undef= undef+1
			print file, len(prevCommits)
			print total,responsibles,no_Responsibles,undef
		else:
			if numCommRespon == "NSNC":
				ticketDeleted=ticketDeleted+1
			print file, 'no prev commit'

print "FINALMENTE:",total
