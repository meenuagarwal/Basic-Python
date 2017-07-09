#generator does not return anything, it yields.

def simple_gen():
	yield 'oh'
	yield 'hello'
	yield 'there'

for i in simple_gen():
	print(i)

correct_combo = (4,1,4)

def combo_gen():
	for c1 in range(5):
		for c2 in range(5):
			for c3 in range(5):
				yield(c1,c2,c3)


for (c1,c2,c3) in combo_gen():
	print(c1,c2,c3)
	if (c1,c2,c3) == correct_combo:
		print ('YES')
		break
