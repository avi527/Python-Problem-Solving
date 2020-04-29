import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print(a[1],a[-1])

#how to change and element in array
number=arr.array('i',[1,2,3,4,5,6,7,8,9])
number[0]=11
number[2:5]=arr.array('i',[33,44,55])
print(number)

#how to append and extend value in array
num=arr.array('i',[11,12,13,14,15])
num.append(22)
num.extend([33,44])
print(num)

#We can concatenate two arrays using + operator. 
conArr1=arr.array('i',[1,2,3,4,5])
conArr2=arr.array('i',[6,7,8,9,0])
finalContArr=conArr1+conArr2
print(finalContArr)

#We can delete one or more items from an array
remoArr=arr.array('i',[1,2,3,4,5,6,7,8,9])
del remoArr[2]
print(remoArr)

#We can use the remove() method to
#remove the given item, and pop() method to remove an item at the given index.
remoArrs=[11,22,33,44,55,66,77,88,99]
#remoArrs.pop(1)
remoArrs.remove(22)
print(remoArrs)


# Python program to copy all elements of one array into another array
arr1 = [1, 2, 3, 4, 5];
arr2=[None]*len(arr1)
for i in range(0,len(arr1)):
	arr2[i]=arr1[i]
#Displaying elements of array arr1     
print("Elements of original array: ");    
for i in range(0,len(arr1)):
	print(arr1[i])
#Displaying elements of array arr2     
print("Elements of new array: "); 
for i in range(0,len(arr2)):
	print(arr2[i])


# Python program to find the frequency of each element in the array
# Initialize array     
arr = [1, 2, 8, 3, 2, 2, 2, 5, 1];         
fr=[None]*len(arr)
visited = -1;   
for i in range(0,len(arr)):
	counter=1
	for j in range(i+1,len(arr)):
		if arr[i] == arr[j]:
			counter=counter + 1
			fr[j]=visited
	if (fr[i] != visited):
		fr[i]=counter
for i in range(0,len(fr)):
	if (fr[i] !=visited):
		print(arr[i],fr[i])

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
	


# Python program to print the duplicate elements of an array
arr = [1, 2,1, 3, 4, 2, 7, 8, 8, 3];  
for i in range(0,len(arr)):
	for j in range(0,i):
		#print(arr[i],arr[j])
		if arr[i] == arr[j]:
			print("duplicate array is",arr[i])
		

# Python program to print the elements of an array
arr=[1,2,3,4,5]
for i in range(0,len(arr)):
	print(arr[i])

# Python program to print the elements of an array in reverse order
arr=[1,2,3]
for i in range(len(arr)-1,-1,-1):
	print(arr[i])

# Python program to print the elements of an array present on even position
arr=[1,2,3,4]
for i in range(1,len(arr),2):
	print(arr[i],'even')

# Python program to print the elements of an array present on odd position
arr=[1,2,3,4]
for i in range(0,len(arr),2):
	print(arr[i],'odd')

# Python program to print the largest element in an array
arr = [25, 11, 7, 75, 56];
max=arr[0]
for i in range(0,len(arr)):
	if (arr[i]>max):
		max=arr[i]
		print(max)

# Python program to print the smallest element in an array
arr=[25, 11, 7, 75, 56];
min=arr[0]
for i in range(0,len(arr)):
	if (arr[i] < min):
		min=arr[i]
print(min)

# Python program to print the number of elements present in an array
arr = [1, 2, 3, 4, 5];  
print("length of array",len(arr))

# Python program to print the sum of all elements in an array
arr = [1, 2, 3, 4, 5];  
sum=0
for i in arr:
	sum=sum+i
print(sum)

# Python program to right rotate the elements of an array
arr=[1,2,3,4,5]
n=3
for i in range(0,n):
	#store the last element of array
	last=arr[len(arr)-1]
	for j in range(len(arr)-1,-1,-1):
		#shift element of array by one
		arr[j] = arr[j-1]
	arr[0]=last
print(arr)


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
































