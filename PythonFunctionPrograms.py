# Question 1.
# Python Program to Find LCM
def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
      
l = [2, 7, 3, 9, 4] 
  
num1 = l[0] 
num2 = l[1] 
lcm = find_lcm(num1, num2) 
  
for i in range(2, len(l)): 
    lcm = find_lcm(lcm, l[i]) 
      
print(lcm) 


# Question 2.
# Python Program to Find HCF
def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))



# Question 3.
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
dec = int(input("Enter a decimal number: "))  
print(bin(dec),"in binary.")  
print(oct(dec),"in octal.")  
print(hex(dec),"in hexadecimal.")  

#Question 4.
#Python Program To Find ASCII value of a character
c = input("Enter a character: ")  
print("The ASCII value of '" + c + "' is",ord(c))  


# Question 5.
# Python Program to Make a Simple Calculator

def Calculater():
	print("select options")
	print("1. Add")
	print("2. Substract")
	print("3. Multiply")
	print("4. Divide")

	choice=input("choice(1/2/3/4)")
	num1=int(input("enter first number"))
	num2=int(input("enter second number"))
	print(choice,'choice')
	if choice == '1':
		print(num1+num2)
	if choice == '2':
		print(num1-num2)
	if choice == '3':
		print(num1*num2)
	if choice == '4':
		print(num1 / num2)

Calculater()

# Question 6.
# Python Program to Display Calendar
import calendar  
def calendr(y,m):
	yy=y
	mm=m
	print(calendar.month(yy,mm))
calendr(2020,7)

# Question 7.
# Python Program to Display Fibonacci Sequence Using Recursion

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  

# Question 8.
# Python Program to Find Factorial of Number Using Recursion
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))






