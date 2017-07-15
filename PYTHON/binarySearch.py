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