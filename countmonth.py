import json
from collections import Counter

with open("birthdays.json","r") as myfile:
	birthdays = json.load(myfile)

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []
for name,birthday_list in birthdays.items():
	month=int(birthday_list.split("/")[0]) #converts string to int
#	print(month)
	months.append(num_to_string[month])    #appends the int month with num_to_string
#	print(months)

c= Counter(months)
print("The counts of bithday months: ")
# for x in c.elements():
# 	print("%s:%s"%(x,c[x]),end="\n")
print(c)