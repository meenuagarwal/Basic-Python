''' Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half. Otherwise narrow it to the upper half. 
Repeatedly check until the value is found or the interval is empty.'''
def BinarySearch(arr,num):
	first,last = 0, len(arr)-1
	found = False
	while(first<=last and not found):
		mid_point = int((first+last)/2) 
		if num == arr[mid_point]:
			found = True
		elif num<arr[mid_point]:
			last = mid_point - 1
		else:
			first = mid_point + 1
	if(found):
		return mid_point
	else:
		raise "Error"


tar = [1,2,3,4,5]
print (BinarySearch(tar,4))
