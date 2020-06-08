import array as arr
#how to change and element in array
number=arr.array('i',[1,2,3,4,5,6,7,8,9])
number[0]=11
number[2:5]=arr.array('i',[33,44,55])
print(number)