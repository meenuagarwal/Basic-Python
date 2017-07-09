#to get index of value we are accessing
#ENUMERATE FUNCTION

num = [2,3,1,4,5,6]
for index,number in enumerate(num):
	print(index,number)

#to change the start index
for index,number in enumerate(num, start =1):
	print(index,number)

#joining
name = ['meenu','ayushi','komal','pinkal']
name_str = ','.join(name)
print name_str
#meenu,ayushi,komal,pinkal

#splitting
new_name = name_str.split(',')
print new_name

new_dict = dict(enumerate(num))
print(new_dict)