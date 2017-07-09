#use {} to create dicts, name is a key and meenu is the value

student = {'name': 'Meenu','age':20,'courses': ['math','ml']}
print(student)

print(len(student))

print(student.keys()) 

print(student.items())

for key in student:
	print(key)

for key,value in student.items():
	print(key,value)