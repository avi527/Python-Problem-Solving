# Python program to print the smallest element in an array
arr=[25, 11, 7, 75, 56];
min=arr[0]
for i in range(0,len(arr)):
	if (arr[i] < min):
		min=arr[i]
print(min)