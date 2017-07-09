name = ['meenu','ayushi','komal','pinkal']
name_2 = ['mittal','patel']

print(len(name)) #getting length of list
print(name[0]) #getting first item
print(name[-1]) #getting last item
print(name[0:2]) #0 in inclusive while 2 is not, so first and second memeber will be printed
print(name.index('meenu')) #find index of meenu
print('Art' in name) #boolean retrun type , check if art is in name

#adding items to list
name.append('tejal')
print(name)
#['meenu', 'ayushi', 'komal', 'pinkal', 'tejal']

#inserting items to list at a particular pos, it will not overwrirte anything
name.insert(1,'krishna')
print(name)
#['meenu', 'krishna', 'ayushi', 'komal', 'pinkal', 'tejal']

#inserting list into list
# name.insert(1,name_2)
# print(name)
#['meenu', ['mittal', 'patel'], 'krishna', 'ayushi', 'komal', 'pinkal', 'tejal']

#EXTEND METHOD
name.extend(name_2)
print(name)
#['meenu', 'krishna', 'ayushi', 'komal', 'pinkal', 'tejal', 'mittal', 'patel']

#REMOVING
name.remove('komal')
popped = name.pop() #removes last element, gives the removed element
print(name)

#SORTING
name.reverse()
name.sort() #sorts in alphabetical order

num = [1,4,2,5,6]
num.sort() #ascending order
print num 
num.sort(reverse = True) #descending order
print num 

print(sum(num))