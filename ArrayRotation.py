#Question : Program for array rotation
#input : 1, 2, 3, 4, 5, 6, 7
#output : 3, 4, 5, 6, 7, 1, 2

'''here;
d=number of sweep elements
n=length of array
arr=assign array value
'''

def ArrayReverse(arr,start,end):
	while(start < end):
		temp=arr[start]
		arr[start] = arr[end]
		arr[end]=temp
		start +=1
		end=end-1
def ArrayRotatedLeft(arr,d):
	if d==0:
		return
	n=len(arr)
	ArrayReverse(arr,n,d-1)
	ArrayReverse(arr,d,n-1)
	ArrayReverse(arr,0,n-1)
def PrintArray(arr):
	for i in range(len(arr)):
		print(arr[i],end=" ")

arr=[1, 2, 3, 4, 5, 6, 7]
d=2
ArrayRotatedLeft(arr,d)
PrintArray(arr)


