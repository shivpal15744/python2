# -*- coding: utf-8 -*-
"""labday1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kI9w2GBKEBzlWQSneeACY-iYAllWF2NQ
"""

# (1). input your name into a variable called $ same and then print "hello,<your name here>".

name="shiv"
print("hello",name)

name = input("Enter your name : ")
print("Hello", name )

# (2). write a program that adds two nomber andd then prints out whether the sum of those two numbers is positive or nagative .

num1 = int(input(" first number : "))
num2 = int(input(" second number : "))

result = num1 + num2
# print(result)

if(result%2==0) :

    print("addition of two numbers is positive ")
else :
    print("addition of two numbers is negative ")

print(result)

# (3).write a program that store a number and keeps trying to get user input until the user enters the number correctly . as soon as the correct number is enterd , it prits : correct! .

num = 85
usernumber = int(input("Enter the number : "))

if(num == usernumber) :
    print("Correct!")
else :
    print("Incorrect, Keep trying...")

num1=int(input("enter the first number :"))
num2=int(input("enter the second number"))

if(num1==num2):
  print("correct")

else:
  print("incorrect,try another number....")

# (4). input first name and last name as two seprate variables , labeles as $ firstname and $ lastname respecitively . concatente them together using the dot  operator '.' into a new variable called $ wholename . than print out the $ wholename .

firstname = input ("Enter first name : ")
lastname = input ("Enter last name : ")

wholename = firstname + lastname

print(wholename)

# (5).write a program to accept an input string from the user and toggle the charactoer cases.
# for example .=> "Hello How Are You"
# o/p : hELLO hOW aRE yOU

str = 'hELLO hOW aRE yOU'
print(" Swap all cases in the string : ", str.swapcase())

str = 'Hello How Are You'
print("swap =",str.swapcase())

# (6). write a program which will perform sum and multiplication , that sums and multiplies (respectively) all the number in a list of number . for example , sum([1,2,3,4]) should return 10, and multiply ([1,2,3,4]) should 24.

mylist = [1, 2, 3, 4]
sum = 0
mult = 1
for i in mylist :
    sum = sum + i
print("Sum of all elements in the list : ", sum)

for i in mylist :
    mult = mult * i
print("Multiplication of all elements in the list : ", mult)

# (7). write a program that takes a value (i.e.a number , string , etc) x and a list of values a , and returns true if x is a member of a , false otherwise (note that this is exactly what the in operator does , but for the sake of exercse you should pretend python did not have this operator.)

list1 = [10, 30, 55, 87]

list2 = [20, 55, 40, 99]

for i in list1 :
    # print(i)
    for j in list2 :
        if i == j :
            print("elements are common in both lists : ", i)

list1 =[52,56,85,65,25,655,556,4,94]
list2 =[68,6,8,55,8868,89,998,655,94,4,85,65]

for i in list1 :
  for j in list2 :
      if i == j :

        print("common number",i)

