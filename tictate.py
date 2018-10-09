a=['0','1','2','3','4','5','6','7','8']
def printboard():
	print(a[0]+'|' +a[1]+'|' +a[2])
	print("------")
	print(a[3]+'|' +a[4]+'|' +a[5])
	print("------")
	print(a[6]+'|' +a[7]+'|' +a[8])
	print("------")

playeroneturn = True
for i in range(8):
	printboard()
#player 1 plays
	if playeroneturn:
		p=input("player 1, choose ur place: ")
		if p in a:
			a[int(p)-1] = 'x'
			playeroneturn = not playeroneturn
#player 2 plays
	else:
		p=input("player 2, choose ur place: ")
		if p in a:
			a[int(p)-1] = 'O'
			playeroneturn = not playeroneturn
#check for wining combinations
a1=a[0,1,2]
a2=a[3,4,5]
a3=a[6,7,8]
a4=a[0,3,6]
a5=a[2,5,4]
a6=a[8,7,1]
a7=a[0,4,8]
a8=a[2,4,6]		
if(:
	winner = True
	printboard()												
if()
#check for a tie condition
print("It's a tie")






