
# Python program to print the duplicate elements of an array
arr = [1, 2,1, 3, 4, 2, 7, 8, 8, 3];  
for i in range(0,len(arr)):
	for j in range(0,i):
		#print(arr[i],arr[j])
		if arr[i] == arr[j]:
			print("duplicate array is",arr[i])