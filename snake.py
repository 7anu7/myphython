import random
count=0
while(count<=100):
	a=input("enter r to roll dice or q to quit")
	if(a=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position",count)
		print("random value",a)
	if(count==11):
		count=2
		print("oops!snake go back")
		print("my position",count)
	elif(count==25):
		count=4
		print("oops!snake go back")
		print("my position",count)
	elif(count==38):
		count=9
		print("oops!snake go back")
		print("my position",count)
	elif(count==65):
		count=46
		print("oops!snake go back")
		print("my position",count)
	elif(count==89):
		count=70
		print("oops!snake go back")
		print("my position",count)
	elif(count==93):
		count=64
		print("oops!snake go back")
		print("my position",count)
	elif(count==8):
		count=37
		print("congragulations go forward")
		print("my position",count)
	elif(count==13):
		count=34
		print("congragulations go forward")
		print("my position",count)
	elif(count==40):
		count=68
		print("congragulations go forward")
		print("my position",count)
	elif(count==52):
		count=81
		print("congragulations go forward")
		print("my position",count)
	elif(count==76):
		count=97
		print("congragulations go forward")
		print("my position",count)
	elif(count==100):
		print("game is urs")
		
	if(a=='q'):
		print("byee")
		exit()
  
  
    
    	
   

    