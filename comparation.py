import json
import os,sys
import csv

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "~/TicketsAnalyzedCinder"
filesname = os.listdir( path )
tickAnal= len(filesname)

with open('ComparationCinder.cvs', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Repository']+['TicketID'] + ['Revisor']+ ['Classification'])
    for file in filesname:
		fn = os.path.join(path, file)
		f= open(fn, 'r')
		content = f.read()
		data= json.loads(content)
		idTicket = data["Id"]
		classification = data["Classification"]
		revisor= file.split("_")
		if revisor[1]=='DOREALDA DALIPAJ':
			revisor[1]='DOREALDA_DALIPAJ'
		writer.writerow(['Cinder', idTicket, revisor[1], classification])

