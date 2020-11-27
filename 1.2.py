import matplotlib.pyplot as plt
x = []
y = []
with open('frames.dat', 'r') as f:
	data = f.read().splitlines()
for i in range(12):
	data[i] = data[i].split(' ')
	for j in range(len(data[i])):
		data[i][j] = float(data[i][j])
fig, ax = plt.subplots(2,3)
for i in range(6):
	x=data[0]
	y=data[2*i+1]
	if (i==0):
		a=0
		b=0
	elif(i==1):
		a=0
		b=1
	elif(i==2):
		a=0
		b=2
	elif(i==3):
		a=1
		b=0
	elif(i==4):
		a=1
		b=1
	elif(i==5):
		a=1
		b=2
	ax[a][b].plot(x, y,label=('Frame '+ str(int(i+1))))
	ax[a][b].grid()
	ax[a][b].set_xlim(0, max(x))
	ax[a][b].set_ylim(-12,12)
	ax[a][b].set_title('Frame '+ str(int(i+1)))

plt.show()
