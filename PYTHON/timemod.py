import timeit

# i_list = range(100)

# def div_by_five(num):
# 	if num%5 == 0:
# 		return True
# 	else:
# 		return False

# xyz = (i for i in i_list if div_by_five(i))

print(timeit.timeit('''i_list = range(100)

def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

xyz = (i for i in i_list if div_by_five(i))
 	''', number = 5000))