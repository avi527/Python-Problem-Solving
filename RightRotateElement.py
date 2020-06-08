# Python program to right rotate the elements of an array
arr=[1,2,3,4,5]
n=3
for i in range(0,n):
	#store the last element of array
	last=arr[len(arr)-1]
	for j in range(len(arr)-1,-1,-1):
		#shift element of array by one
		arr[j] = arr[j-1]
	arr[0]=last
print(arr)
