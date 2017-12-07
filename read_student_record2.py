import re
import openpyxl as op
import time
import os
import sys
# Importing Output.xlsx sheet
print("Welcome to Tutor Trac Cleaner:- Group By Name.\nThe System that reads raw data and gives you a cleaner version.\n\n")
try:
	#dirval=os.path.normpath("C:/Python_Scripts/TutorTrac_Cleaner_Group_By_Name/output.xlsx")
	wb=op.Workbook()
	#sheet=wb.get_sheet_by_name('Sheet1')
	sheet=wb.active
	sheet.title='Records'
except (FileNotFoundError,IOError) as err:
	print("\n\nCannot find output.xlsx file\n\n")
	time.sleep(5)
	sys.exit(1)
# Opening the file input.csv
try:
	dirval=os.path.normpath("C:/Python_Scripts/TutorTrac_Cleaner_Group_By_Name/input.csv")
	f=open(dirval,'r')
except (FileNotFoundError,IOError) as err:
	print("\n\nCannot find input.csv file\n\n")
	time.sleep(5)
	sys.exit(1)
text=f.read()
row_element_five=input("\n\nPlease INPUT the year/semester to which the data is related to. Ex: AY16 or 2016 etc \t:")
# Finding Matches of Names and Mnumbers
list_of_name_mnum=re.findall(r"([ a-zA-Z'-\.]+, [ a-zA-Z'-\.]+)(?=(\",[0-9]{5,8}))",text)
# Finding Matches of Visits and Hours
list_of_visits_hours=re.findall(r"([0-9]+)(?=(,[0-9]+\.[0-9]+,,,,|,[0-9]+,,,,))",text)
#Adding the headers into our sheet
sheet['A1']='Name'
sheet['B1']='M_Number'
sheet['C1']='Visits'
sheet['D1']='Hours'
sheet['E1']='Term'
# Iterating through all and finding the row_elements
counter=2
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
	sheet['A'+str(counter)]=row_element_one
	sheet['B'+str(counter)]=row_element_two
	sheet['C'+str(counter)]=row_element_three
	sheet['D'+str(counter)]=row_element_four
	sheet['E'+str(counter)]=row_element_five
	counter+=1
# Saving the sheet
dirval=os.path.normpath("C:/Python_Scripts/TutorTrac_Cleaner_Group_By_Name/output.xlsx")
wb.save(dirval)
f.close()
print("\n\n***** Thank you for using TutorTrac Cleaner- Group By name *****\n\n")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\nYOUR RESULTS ARE WAITING IN THE 'output.xlsx' FILE\n")
time.sleep(1)
print("BYE")
time.sleep(2)
ch=input("\n\nJust hit enter for the page to close\t:")