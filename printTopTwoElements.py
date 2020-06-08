
# Python program to print the second largest element in an array
arr=[2,3,60,88,99,80,90,100]
first=second=arr[0]
for i in range(0,len(arr)):
	if(arr[i] > first):
		second=first
		first=arr[i]
	elif(arr[i] > first and arr[i] < second):
		second=arr[i]
print(first,second)