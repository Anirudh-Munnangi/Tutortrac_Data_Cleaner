import re
from tabulate import tabulate
f=open('testfile.csv','r')
text=f.read()
matches=re.findall(r"[0-9]{5,8}|[a-zA-Z'-]+, [a-zA-Z'-]+ [a-zA-Z'-]+|[a-zA-Z'-]+, [a-zA-Z'-]+|SubjectID|[0-9]{2}[A-Z]{4}[0-9]{4}[A-Z]?",text)
list_of_matches=[val for val in matches]
print(len(list_of_matches))
ctr=1
mainlist=[]
templist=[]
for val in list_of_matches:
	if re.match(r"SubjectID",val) or re.match(r"[0-9]{2}[A-Z]{4}[0-9]{4}[A-Z]?",val):
		if ctr%2!=0:
			mainlist.append(["",""])
			mainlist.append(["",""])
			mainlist.append(["",""])
			mainlist.append(["",""])
			mainlist.append([val," "])
			#print("\n\n")
			#print(val,"\n") 	# Print Subjects
			mainlist.append(["Name of Student","M# of Student"])	
			mainlist.append(["-------------------------","----------"])
			ctr+=1
			continue
		ctr+=1
	if re.match(r"[0-9]{5,8}",val):
		templist.append("M"+"0"*(8-len(val))+val)
		#print("M"+"0"*(8-len(val))+val)	# Print Mnumbers
	if re.match(r"[a-zA-Z'-]+, [a-zA-Z'-]+ [a-zA-Z'-]+|[a-zA-Z'-]+, [a-zA-Z'-]+",val):
		templist.append(val)
		#print(val,"\t",end="\t")	# Printing Names
	if len(templist)==2:
		mainlist.append(templist)
		templist=[]
f.close()
print(tabulate(mainlist))