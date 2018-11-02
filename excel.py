import csv
import matplotlib.pyplot as plt
x = []
y = []
with open('anu1.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
plt.plot(x,y,label='loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\ncheck it out')
plt.legend()
plt.show()