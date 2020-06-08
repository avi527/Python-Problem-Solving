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