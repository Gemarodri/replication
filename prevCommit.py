import json
import os,sys
import csv

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "~/PrevCommitCinder"
filesname = os.listdir( path )
tickAnal= len(filesname)
bugs=[]
notBugs=[]
undefined=[]
with open('ResponsabilityCinder.cvs', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Repository']+['TicketID'] + ['n_Files']+ ['n_PrevCommit']+ ['Responsability'])
    for file in filesname:
    	if file!= '.git':
			fn = os.path.join(path, file)
			f= open(fn, 'r')
			content = f.read()
			data= json.loads(content)
			idTicket = data["Id"]
			classification = data["Responsible"]
			nameFiles= data["Files"].split(",")
			prevCommits = data["CommitPrevious"].split("\n")
			writer.writerow(['Cinder', idTicket, len(nameFiles), len(prevCommits), classification])
