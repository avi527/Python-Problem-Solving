# Python program to sort the elements of an array in ascending order
arr = [5, 2, 8, 7, 1];     
temp = 0;    
     
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if(arr[i] > arr[j]):
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp

for i in range(0,len(arr)):
	print(arr[i])

# Python program to sort the elements of an array in descending order
arr = [5, 2, 8, 7, 1];
temp=0
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if (arr[i] < arr[j]):
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp

for i in range(0,len(arr)):
	print(arr[i])