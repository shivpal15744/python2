# -*- coding: utf-8 -*-
"""day3assignmentpy

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/186PZr0PtfbIOuwpH5_MnS_teKUiR4WRw
"""

x=10
y=19
if(x<=10  and y>=18):
    print("age is valid")
else:
    print("age is not valid")

a=3
b=6
c=4
if(a<b and a<c):
    print ("a is minimum")

elif(b<a and b<c):
    print(" b is minimum")
else:
  print("c is minimum")

x=75
if(x>60):
    print("avrege")
if(x>75):
    print("good")
if(x>85):
    print("excelent")
if(x>95):
    print("brilliant")

else:
    print("fail")

x=75.69

if(x>60 and x<=75):
    print("avrege")
elif(x>75 and x<=85):
    print("good")
elif(x>85 and x<=95):
    print("excelent")
elif(x>95 and z<=100):
    print("brilliant")

else:
    print("fail")

x=int(input("enter the number "))

if(x==1):
    print("sunday")

elif(x==2):
    print("monday")

elif(x==3):
    print("tuesday")

elif(x==4):
    print("wednesday")

elif(x==5):
    print("thrusday")

elif(x==6):
    print("friday")

elif(x==7):
  print("saturday")
else:
    print("please enter correct value")

x=int(input())

if(x==1):
    print("january")

elif(x==2):
    print("febuary")

elif(x==3):
    print("march")

elif(x==4):
    print("april")

elif(x==5):
    print("may")

elif(x==6):
    print("june")

elif(x==7):
    print("july")

elif(x==8):
    print("august")

elif(x==9):
    print("september")

elif(x==10):
    print("octumber")

elif(x==11):
    print("november")

elif(x==12):
   print("december")

else:
    print("please enter correct value")

x=int and float (input())

if(x>60 and x<=75):
    print("avrege")
elif(x>75 and x<=85):
    print("good")
elif(x>85 and x<=95):
    print("excelent")
elif(x>95 and z<=100):
    print("brilliant")

else:
    print("fail")

x=int and float ( input ( ) )

if(x>70 and x<=80):
    print("good")

elif(x>81 and x<=91 ):
    print("very good ")

elif(x>91 and x<=100):
    print("excellent")

else:
  print("fail")

age=int(input("enter your age"))
country=str (input("enter your country"))
if(age<=10  and age>=18):
    print("age is valid")

elif(country=="indea"):
    print("valid")
else:
    print("age is not valid")

import os

# Define the shutdown_os function
def shutdown_os():
    os.system("shutdown -h now")

# Get user input
x = int(input("Enter the number: "))

# Check the input
if x == 2:
    # Call the shutdown_os function
    shutdown_os()