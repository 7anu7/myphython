import random
d={1:"R",2:"P",3:"S"}
while(1):
	c=d[random.randint (1,3)] 
	p=input("enter 'r','p','s'")
	if(c=='p'):
		print("tie")
	elif((c=='r' and p=='s') or (c=='p' and p=='r') or (c=='s' and p=='p')):
		print(" u won the game")
	elif((c=='r' and p=='s') or (c=='p' and p=='r') or (c=='s') and p=='p'):
		print(" oh! my god again u won the game")
	else:
		print("hmm.this time i won")
	

	



	 
