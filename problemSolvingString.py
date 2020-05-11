#Question 1.
#Write a program to print every character of a string entered by user in a new line using loop.

userInput=input("enter your string")
for i in userInput:
	print(i)



#Questionn 2.
#Write a program to find the length of the string "refrigerator" without using len function.
count=0
for i in "refrigerator":
	count=count+1
print(count)

#Question 3.
#Write a program to check if the letter 'e' is present in the word 'Umbrella'.
if 'e' in 'Umbrella':
	print("match")


#Question 5.
#Write a program to check if the word 'orange' is present in the "This is orange juice".
a='This is orange juice'
print("orange" in a.split())

#Question 6.
#Write a program to find the first and the last 
#occurence of the letter 'o' and character ',' in "Hello, World".
count=0
for i in 'Hello, World':
	count=count+1
	if i == 'o':
		print(i,count)

#Question 7.
#Write the string after the first occurrence of ',' and the string after
#the last occurrence of ',' in the string "Hello, Good, Morning". World".



#Question 8.
#Write a program that takes your full name as input and displays the abbreviations of the 
#first and middle names except the last name which is displayed
#as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
userInput="Avinash Kumar Singh"
userInput=userInput.split()
Output=userInput[0][0]+"."+userInput[1][0]+"."+userInput[2]
print(Output)


#Question 9.
#Check the occurrence of the letter 'e' and the word 'is' in the sentence "This is umbrella".
inputData='This is umbrella'
letter='e'
counter=0
for i in inputData:
	counter=counter+1
	if 'e' in i:
		print("occurrence of the letter :",counter)




#Question 10.
#Write a program to find the number of vowels, consonents, digits and white space
#characters in a string.
inputData="this is avinash 0527"
vowels=['a','e','i','o','u']
count=0
for i in inputData:
	count=count+1
	if i in vowels:
		print("vowels",count)
	elif (i.isdigit()):
		print('digits',i,count)
	else:
		print('consonent',count)


#Question 11.
#Write a program to make a new string with all the consonents deleted from the string
# "Hello, have a good day".
a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
for i in b:
  if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print (b)

#Question 12
#Write a program to find out the largest and smallest word in the string "This is an umbrella".
inpurString="This is an umbrella"
inpurString=inpurString.split(" ")
largest=smallest=inpurString[0]
for i in range(0,len(inpurString)):
	for j in range(0,i):
		if inpurString[i] > inpurString[0]:
			largest=inpurString[i]
		elif inpurString[j] < largest:
			smallest=inpurString[j]
print(largest,"is largest word")
print(smallest,"is smallest word")


#Question 13
# Write a program to check if a given string is a Palindrome.
# A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.
inpurString=input("enter your string")
print(a[:])
print(a[::-1])
print(a==a[::-1])

#Question 14
#Write down the names of 10 of your friends in a list and
# then sort those in alphabetically ascending order.


#Question 15
# Write a program to make a new string with the word "the"
#  deleted in the sentence "This is the lion in the cage".
a = "This is the lion in the cage"


#Question 16
# Write a program to check if the two strings entered by user are anagrams or not.
# Two words are said to be anagrams if the letters of one word can be rearranged to form 
# the other word. For example, jaxa and ajax are anagrams of each other.


#Question 17



#Question 18



#Question 19



#Question 20



#Question 21


#Question 22



#Question 23


#Question 24


#Question 25



#Question 26


#Question 27


#Question 28
