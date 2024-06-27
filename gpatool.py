#!/usr/bin/python3
#gpatool.py
#Tool to math out GPA stuff
#by Thomas Dodds

def main():
	while True:
		print("Enter current GPA Hours (0 for blank slate): ", end='')
		gpahours = int("0" + input())
		if(gpahours > 0):
			print("Enter current GPA (<5) or Quality Points: ", end='')
			value = float("0" + input())
			if(value < 5):
				gpa = value
				gpapoints = int(gpahours * value)
				go = True
			else:
				gpapoints = int(value)
				try:
					gpa = float(gpapoints) / float(gpahours)
					go = True
				except ZeroDivisionError:
					print("You cannot have quality points and not have GPA hours.")
					go = False
		else:
			print("Blank slate. GPA: 0, Quality points: 0")
			gpa = 0
			gpapoints = 0
			go = True
		whatifgpahours = gpahours
		whatifgpapoints = gpapoints
		while go:
			choice = mainmenu()
			match choice:
				case 1:
					print("Course-Add) Hours: ", end='')
					addhours = int(input())
					print("Course-Add) Grade (A-F): ", end='')
					addqhours = qhours(addhours)
					whatifgpahours = whatifgpahours + addhours
					whatifgpapoints = whatifgpapoints + addqhours
				case 2:
					print("Course-Retake) Hours: ", end='')
					retakehours = int(input())
					print("Course-Retake) Previous grade (A-F): ", end='')
					retakeqhours = qhours(retakehours) * -1
					print("Course-Retake) Expected grade (A-F): ", end='')
					retakeqhours = retakeqhours + qhours(retakehours)
					whatifgpapoints = whatifgpapoints + retakeqhours
				case 3:
					print("Course-Remove) Hours: ", end='')
					remhours = int(input())
					print("Course-Remove) Grade (A-F): ", end='')
					remqhours = qhours(addhours)
					whatifgpahours = whatifgpahours - remhours
					whatifgpapoints = whatifgpapoints - remqhours
				case 4:
					try:
						whatifgpa = float(whatifgpapoints) / (whatifgpahours)
					except ZeroDivisionError:
						whatifgpa = 0
					print("What-If) GPA: " + str(round(whatifgpa, 3)) + " (" + sign(round(whatifgpa-gpa, 3)) + ")")
					print("What-If) Hours: " + str(whatifgpahours) + " (" + sign(whatifgpahours - gpahours) + " hours)")
					print("What-If) Quality Points: " + str(whatifgpapoints) + " (" + sign(whatifgpapoints - gpapoints) + " points)")
				case 5:
					whatifgpahours = gpahours
					whatifgpapoints = gpapoints
				case 6:
					print("Current) GPA: " + str(round(gpa, 3)))
					print("Current) Hours: " + str(gpahours))
					print("Current) Quality Points: " + str(gpapoints))
				case 7:
					go = False
				case _:
					pass

def mainmenu():
	choice = 0
	while(choice == 0):
		print("Menu) ", end='')
		choice = input()
		if(choice == "?" or len(choice) == 0):
			print("1. Add course")
			print("2. Retake course")
			print("3. Remove course")
			print("4. Print what-if info")
			print("5. Reset what-if info")
			print("6. Print current info")
			print("7. Restart")
			choice = 0
		else:
			try:
				choice = int(choice)
				if(choice < 1 or choice > 7):
					raise ValueError("not in range")
			except ValueError:
				choice = 0
				print("Invalid option: ? for help")
	return choice

def qhours(chours):
	invalid = True
	scalar = 0
	while(invalid):
		invalid = False
		try:
			match input()[0].upper():
				case 'A':
					scalar = 4
				case 'B':
					scalar = 3
				case 'C':
					scalar = 2
				case 'D':
					scalar = 1
				case 'F':
					scalar = 0
				case _:
					invalid = True
		except IndexError:
			invalid = True
	return chours * scalar

def sign(value):
	if(float(value) < 0):
		return str(value)
	else:
		return "+" + str(value)

if(__name__ == "__main__"):
	main()
