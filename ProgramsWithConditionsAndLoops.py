# Question 1.
# Python Program to Check if a Number is Positive, Negative or Zero
arr=[1,2,3,-4,-6,0,-10,88]
for i in range(0,len(arr)):
	if(arr[i] > 0):
		Positive=arr[i]
		print(Positive,'Positive')
	elif(arr[i] < 0):
		Negative=arr[i]
		print(Negative,'Negative')
	elif(arr[i] == 0):
		print(arr[i],'Zero')

# Question 2.
# Python Program to Check if a Number is Odd or Even
inputUser=int(input("enter your number"))
if inputUser%2==0:
	print("even number")
else:
	print("odd number")

# Question 3.
# Python Program to Check Leap Year
inputYear=int(input("please enter year"))
if inputYear % 4 == 0:
	if inputYear % 100 == 0:
		if inputYear % 400 == 0:
			print(inputYear,"Its leap year")
		else:
			print(inputYear,"Its not leap year")
	else:
		print(inputYear,"Its leap year")
else:
	print(inputYear,"Its not leap year")

# Question 4.
#Python Program to Find the Factorial of a Number

num=5
fact=1
for i in range(1,num+1):
	fact=fact*i
print(fact)

# Question 7.
# Python Program to Display the multiplication Table
num=10
for i in range(1,11):
	tableOf=i*num
	print(tableOf)

# Question 8.
# Python Program to Print the Fibonacci sequence
nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < nterms:  
       nth = n1 + n2  
       print(nth,end=' , ')  
       # update values  
       n1 = n2  
       n2 = nth  
       count += 1  


#Question 
#find prime number
def isPrime(n): 
    if n <= 1: 
        return False
    # Check from 2 to n-1 
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
    print(n,'is prime number')
    # return True
  
print(isPrime(11) )

# Question 9.
# Program to Find the Sum of Natural Numbers
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  





