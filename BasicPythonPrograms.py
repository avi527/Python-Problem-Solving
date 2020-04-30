# Question 1.
# Python program to print "Hello Python"

print("Hello World")

# Question 2.
# Python program to do arithmetical operations
a=10
b=2
sum=a+b
multiply=a*b
divide=a%2
substration=a-b
print(sum,multiply,divide,substration)

# Question 3.
# Python program to find the area of a triangle
# formulaa=Len*width
side1=20
side2=20
side3=10
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print(area,'s')

# Question 4.
# Python program to solve quadratic equation

# formulla=ax^2+bx+c=0

import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
calculate the discriminant  
d = (b**2) - (4*a*c)  
  
find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   

# Question 5.
# Python program to swap two variables
a=5
b=10
# a=b
c=a
a=b
b=c
print(a,b)


# Question 6.
# Python program to generate a random number
import random
print(random.randint(1,100))

# Question 7.
# Python program to convert kilometers to miles
#formulla[1 KM is equal to 0.62137 miles]
km=8
miles=5*0.62137
print(miles)


#Question 8
#Python program to convert Celsius to Fahrenheit
#formulla[fahrenheit = (celsius * 1.8) + 32]
tem=8
fahrenheit=(8*1.8)+32
print(fahrenheit)

# Question 9.
# Python program to display calendar
import calendar
print(calendar.month(2020,7))














