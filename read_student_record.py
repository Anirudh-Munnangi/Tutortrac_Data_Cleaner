import re
import pyexcel as pe
import time
import os
# Importing Output.xlsx sheet
sheet=pe.get_sheet(file_name=os.path.abspath("output.xlsx"))
# Opening the file input.csv
f=open('input.csv','r')
text=f.read()
# Finding Matches of Names and Mnumbers
list_of_name_mnum=re.findall(r"([ a-zA-Z'-\.]+, [a-zA-Z'-\.]+ [a-zA-Z'-\.]+ [a-zA-Z'-\.]+ [a-zA-Z'-\.]+|[ a-zA-Z'-\.]+, [a-zA-Z'-\.]+ [a-zA-Z'-\.]+ [a-zA-Z'-\.]+|[ a-zA-Z'-\.]+, [a-zA-Z'-\.]+ [a-zA-Z'-\.]+|[ a-zA-Z'-\.]+, [a-zA-Z'-\.]+)(?=(\",[0-9]{5,8}))",text)
# Finding Matches of Visits and Hours
list_of_visits_hours=re.findall(r"([0-9]+)(?=(,[0-9]+\.[0-9]+,,,,|,[0-9]+,,,,))",text)
# Iterating through all and finding the row_elements
for val in range(0,len(list_of_name_mnum)):
	# Describing Elements to be written to the output files
	item1=list_of_name_mnum[val]
	item2=list_of_visits_hours[val]
	row_element_one=item1[0]
	# Modifying the Mnumber to its actual format
	id=item1[1]
	id=id[2:]
	row_element_two="M"+"0"*(8-len(id))+id
	row_element_three=item2[0]
	# Modifying the hour item to its original format
	hour=item2[1]
	hour=hour[1:]
	hour=hour[:-4]
	row_element_four=hour
	# Writing the elements to the output files
	sheet.row += [row_element_one,row_element_two,row_element_three,row_element_four]
# Saving the sheet
sheet.save_as("Output.xlsx")
f.close()
print("\n\n***** Thank you for using TutorTrac Cleaner- Group By name *****\n\n")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("BYE")
time.sleep(1)