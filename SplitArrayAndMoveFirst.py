#Question : Python program to split array and move first
def SplitArray(arr,n,d):
	for i in range(0,d):
		x=arr[0]
		for j in range (0,n-1):
			arr[j]=arr[j+1]
		arr[n-1]=x
def PrintArray(arr):
	for i in range(0,len(arr)):
		print(arr[i])


arr = [12, 10, 5, 6, 52, 36] 
n = len(arr) 
d = 2
SplitArray(arr,n,d)
PrintArray(arr)

