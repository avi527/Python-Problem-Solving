import array as arr
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
