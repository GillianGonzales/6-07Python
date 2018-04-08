#
# Created By Gillian
# Created On April 7 2018
#
# This program will tell the user to guess my age 

print("Guess my age")

guess = input() 
age = "15"

 

while True:
	if guess == age:
		print("You got my age right")
		input("End program")
		break
	elif guess > age: 
		print("Go lower")
		guess = input()
	elif guess < age: 
		print("Go higher")
		guess = input()
	else:
		print("Invaild Answer")
		input("End Program")
		break
	pass
pass





 
