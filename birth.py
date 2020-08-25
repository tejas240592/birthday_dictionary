# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json

birthday={}
with open("birthdays.json","r") as myfile:
	birthday = json.load(myfile)

#add birthday entry to json file	
def add_entry():
	name = input("Who do you want to add to the Birthday Dictionnary?\n").title()
	date = input(f"When was {name} born?\n")
	birthday[name] = date
	with open("birthdays.json","w") as myfile:
		json.dump(birthday,myfile)
		print(f"{name} was added in my birthday dictionary!\n")

#find birthday from that json file
def find_date():
	name = input("Who's birthday do you want to know?\n").title()
	try:
		if birthday[name]:
			print(f"{name}\'s birthday is on {birthday[name]}")
	except:
		print("Sadly we don't have the record of this person")

#View the entries in json file
def list_entries():
	print("The current entries in my birthday list are:\n============================================")
	for i in birthday:
		print(i.ljust(31),':',birthday[i])
	print()

while True:
	what_next = input("What do you want to do next? you can: Add, Find, List, Quit\n").capitalize()
	if what_next=='Quit':
		print('Good bye!')
		raise SystemExit(0)
	elif what_next == 'Add':
		add_entry()
	elif what_next == 'Find':
		find_date()
	elif what_next == 'List':
		list_entries()
	