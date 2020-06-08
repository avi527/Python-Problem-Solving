#Question : Python Program for Find remainder of array multiplication divided by n
def DivideReminder(array,length,n):
	multi=1
	for i in range(0,length):
		multi=(multi*(array[i] % n)% n)
	print(multi)
array = [ 100, 10, 5, 25, 35, 14 ] 
length = len(array) 
n = 15
DivideReminder(array,length,n)