'''
#the first python program
#program to take input of two numbers and find their sum
import math


num1=int(input("enter the first number:"))
num2=int (input ("enter 2nd number:"))
sum=num1+num2
print ("the sum is :",sum)

print("""The area of the square""")
side=int(input ("enter the side of the square:"))#here you need type casting.
area=math.pow(side,2)
print ("the area of the square is:",area)

print("""The average of two floating point numbers""")
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
average=(num1+num2)/2
print ("the average of two numbers is:",average)
print ("the changes are added")
print ("the changes are added")

"""lecture  2"""
"""WAP to find input the name of the user and find its length"""
str=input("enter your name:")
print (str)
print (len(str))
"""Occurence of dollar in the string"""
str1=input("enter the string:")
print(str1.count("$"))
"""CONDITIONS"""
marks=75

if(marks>=90):
    print ("Grade is A")
elif(marks<90 and marks>=80):
    print("Grade is B ")
elif(marks<80 and marks>=70):
        print("Grade is c") 
        '''
         # TUPLES AND LISTS
#write a program to ask the user to enter the name of 3 favourite movies and store them in the list
m1=str (input("enter the movie1:"))
m2=str(input("enter the movie2:"))
m3=str(input("enter the movie3:"))
movies=[]
movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)
print(type(movies))

