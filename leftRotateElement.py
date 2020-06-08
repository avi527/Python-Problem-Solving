# Python program to left rotate the elements of an array			
arr = [1, 2, 3, 4, 5];     
#n determine the number of times an array should be rotated    
n = 1;    
     

for i in range(0,n):
	first=arr[0]
	for j in range(0,len(arr)-1):
		arr[j]=arr[j+1]
	arr[len(arr)-1]=first
print(arr)
	