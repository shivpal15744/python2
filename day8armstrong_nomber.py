# -*- coding: utf-8 -*-
"""day8armstrong nomber.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aZaRYZmgobJ5-SQLr5fapsL8aJ5P5ILQ
"""

# to find wether any nomber is a armstrong nomber .

x = int(input("enter the nomber : "))

# Calculate rem1, rem2, and rem3 first

rem1 = x % 10
rem2 = (x // 10) % 10
rem3 = (x // 100) % 10

if rem1**3 + rem2**3 + rem3**3 == x:
    print("That is an Armstrong number.")

else:
    print("that is not an armstrong nomber ")

x = int(input("enter the nomber : "))
rem1 = x%10 #(1)
x//10

x=x//10
x%10

rem2 = x%10 #(2)
x=x//10

rem3 = x%10 #(3)
x=x//10

rem1**3 + rem2**3 + rem3**3

from typing import OrderedDict
n=int(input("enter the number : "))
sum=0
order=len(str(n)) # iska kaam didit ko nikalna h . ( nomber of digit's )
copy_n=n # n ki copy create ki agar n update ho jaye to uski copy / orignel value safe rhe .

while(n>0):
      digit=n%10
      sum+=digit**order
      n=n//10

if(sum==copy_n):
      print("armstrong number")
else:
      print("not armstrong number")

from typing import OrderedDict
n=int(input("enter the number : "))
sum=0
order=len(str(n)) # iska kaam didit ko nikalna h . ( nomber of digit's )
copy_n=n # n ki copy create ki agar n update ho jaye to uski copy / orignel value safe rhe .

while(n>0):
      digit=n%10
      sum+=digit**order
      n=n//10

if(sum==copy_n):
      print(f"{copy_n} : armstrong number")
else:
      print(f"{copy_n} : is not armstrong number")

