# Question1.
# Python program to check if the given number is a Disarium Number

def countNum(n):
	length=0
	while n !=0:
		length=length+1
		n=n//10
	return length
num=175
rem = sum = 0;      
len=countNum(num)

n=num
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
#Checks whether the sum is equal to the number itself    
if(sum == n):    
    print(n ," is a disarium number");    
else:    
    print(n, " is not a disarium number");    

# Question2.
# Python program to print all disarium numbers between 1 to 100
#calculateLength() will count the digits present in a number    
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    



# Question3.
# Python program to check if the given number is Happy Number
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = 82;    
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
#Happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number");    
#Unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number");   

# Question4.
# Python program to print all happy numbers between 1 and 100
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
            
#Displays all happy numbers between 1 and 100    
print("List of happy numbers between 1 and 100: ");    
for i in range(1, 101):    
    result = i;    
        
    #Happy number always ends with 1 and     
    #unhappy number ends in a cycle of repeating numbers which contains 4    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    if(result == 1):    
        print(i),    
        print(" "),


# Question5.
# Python program to determine whether the given number is a Harshad Number
num = 156;    
rem = sum = 0;    
#Make a copy of num and store it in variable n    
n = num;    
#Calculates sum of digits    
while(num > 0):    
    rem = num%10;    
    sum = sum + rem;    
    num = num//10;    
#Checks whether the number is divisible by the sum of digits    
if(n%sum == 0):    
    print(str(n) + " is a harshad number");    
else:    
    print(str(n) + " is not a harshad number");   

# Question6.
# Python program to print all pronic numbers between 1 and 100 

#isPronicNumber() will determine whether a given number is a pronic number or not    
def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "),      











