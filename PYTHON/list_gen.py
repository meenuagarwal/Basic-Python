i_list = [5,6,1,4,10,11,15,20]

def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

#() means generator, it is not created in memory untill iteration
xyz = (i for i in i_list if div_by_five(i))
#same as 
# xyz = []
# for i in i_list:
#	if div_by_five:
#		xyz.append(i)

for i in xyz:
	print(i)

xyz = (((i,ii) for ii in range(5)) for i in range(5))

for i in xyz:
	print(i)