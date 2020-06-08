# arrays in python can only contain values corresponding to same data type.

# Question :- Program to find sum of array
'''Method 1'''
import array as arr
def sumOfArray(arr):
	sum=0
	for i in arr:
		sum=sum+i
	print(sum)
arr=[2,3,5,10]
sumOfArray(arr)

'''Method 2'''
arr=[2,3,5,10]
ans = sum(arr) 
print(ans)




