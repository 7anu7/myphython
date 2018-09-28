#program to get random
import random
print(random.randint(1,6))
while True:
	a=input("press 'r'to roll the dice and 'q' to quit")
	if(a=='r'):
		print("hello!")
		exit()

else:
	print(" try again")