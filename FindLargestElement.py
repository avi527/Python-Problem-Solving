# Question : Program to find largest element in an array
'''Method 1'''
def LargestEle(arr,largest):
	for i in range(0,len(arr)):
		for j in range(0,len(arr)):
			if arr[j] > largest:
					largest=arr[j]
	print(largest)
arr=[15, 10, 1020, 4, 100,500]
largest=arr[0]
LargestEle(arr,largest)

'''Method 2'''
arr=[15, 10, 1020, 4, 100,500]
max=arr[0]
for i in range(1,len(arr)):
	if arr[i] > max:
		max=arr[i]
print(max)