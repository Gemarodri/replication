import json
import os,sys
import csv

#Fix the correct path from the repo, where the tickets are, without .git repository
path= "~/PrevCommitCinder"
filesname = os.listdir( path )
tickAnal= len(filesname)
cont=0
Res=0
AtLeast=0
NoRes=0
Unde=0

for file in filesname:
	if file!= '.git':
		fn = os.path.join(path, file)
		f= open(fn, 'r')
		content = f.read()
		data= json.loads(content)
		prevCommits = data["CommitPrevious"].split("\n")
		#Change the len of the previous commit that yu want analyze
		if len(prevCommits) >= 5:
			cont=cont+1
			if data["Responsible"]=="All":
				Res=Res+1
			elif data["Responsible"]=="Atleastone":
				AtLeast=AtLeast+1
			elif data["Responsible"]=="Neither":
				NoRes=NoRes+1
			elif data["Responsible"]=="Undecided":
				Unde=Unde+1
print Res,AtLeast,NoRes,Unde
