x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c','d']

for r,s,t in zip(x,y,z):
	print(r,s,t)

print(dict(zip(y,z)))