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
  
#WAP to check if the list is palindrome or not
series=[]
series.append(input("enter the first series:"))
series.append(input("enter the second series:"))
series.append(input("enter the third series:"))
seriescopy=series.copy()
seriescopy.reverse()
if (series==seriescopy):
    print ("the series is palindrome")
else:
    print("the series is not palindrome")
'''
'''#WAP to check the number of A in student's grade using tuple. store the above value in a list and then sort the

grade=("a","b","c","d","e","a")
print(grade.count("a")) 
#converting tuple into list
grade_list=list(grade)
#sorting the list
grade_list.sort(reverse=True)
print(grade_list)'''

#WAP to construct the dictionary and search the value.
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(dictionary)
#WAP to construct set of classrooms and count them
set={"python","java","c++","javascript","python","java","c++","javascript"}
print(len(set))
print(type(set))

#WAP to enter marks f 3 subjects and store them in a dictionar. start with an empty dictionary
#and add one by one. use subject as key and marks as value
marks={}#empty dictionary
x=int(input("enter mark of phy:"))
marks.update({"phy":x}) #passing the new key value pair
print(marks["phy"])
#store 8 and 8.0 separately in set
set1={8,8.0}
print(set1)
'''it will print 8.0 only'''
#hence we use built in data types like tuples or store in string format
#set2={"8","8.0"} is one way
set2={
    ("float",8.0),
    ("int",8)
}   
print(set2) 