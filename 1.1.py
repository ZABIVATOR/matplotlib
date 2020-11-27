import matplotlib.pyplot as plt
with open('dead_moroz/004.dat', 'r') as f:
    data = [line.split() for line in f]
N = int(data.pop([0][0])[0])
del data[N:]
x = []
y = []
for line in data:
    x.append(float(line[0]))
    y.append(float(line[1]))
fig, ax = plt.subplots(figsize=(20, 5))
ax.scatter(x,y,s=2)
plt.title('Number of points: '+str(N)) 
plt.show()
