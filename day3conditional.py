# -*- coding: utf-8 -*-
"""day3conditional.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LNBLWPuo35Y3DWGgeFaNyeyQ0OD9-5cp
"""

# Memory address check krna .
x=10
print(id(x))

y=x
print(id(y))

age=18
print(id(age))

salary = age
print(id(salary))

salary=20
print("new",id(salary))
# salary ki value change krte hi memory address change ho gya .

print(id(age))
# age ka memory address abhi bhi vo hi h .

# jab python me inteser , string ya koi bhi xyz variable ki baat krte h to vh immutable data type hote h .
# kyunki vo hamesha new memory address ke andar kaam krta h .
# agar ham variable me koi bhi changes krege to hamesha ek new memory address create krega .

# int. , str. , touple and frozen set = immutable data type.
# list , dictioery , set = muteble data type .

# String indexing and slicing .
# string means multiple cherector combination.
# sab cheractor ek position ko hold krte h jise index khte h .
# starting value change nhi hoti h .
# last ki value print nhi hoti h .
# ex. 8=0_7 , 10=0_9
x="RAJASTHAN"
print(x)

x="RAJASTHAN"
print(x[0])

x="RAJASTHAN"
print(  x  [ 2 ]  )

x="RAJASTHAN"
print(  x  [ -2 ]  )

x="RAJASTHAN"
print(  x  [ -5 ]  )

# kisi charector ki position nikalne ke liye iska use kkiya jata h .

# Slicing = data niklna
# [ starting value : stop value : [step size (1,2)] ]
# agar khi pr [[]] aa jaye to iska mtlb h andar vala optional h .

x="RAJASTHAN"
print(  x  [ 2 : 6 : 1 ]  )

x="RAJASTHAN"
print(  x  [ 2:7:2 ]  )

x="RAJASTHAN"
print(  x  [ 2 : 5]  )

x="RAJASTHAN"
print(  x  [ 1 : 8 ]  )

x="RAJASTHAN"
print(  x  [ 2:  ]  )

# agar ending value nhi dete h to pura print hoga .

x="RAJASTHAN"
print(  x  [ : 2 ]  )

# kyunki starting value hamesha 0 se start hoti h .

x="RAJASTHAN"
print(  x  [ 2 : : 2]  )

# last tak 2-2 ke step se jab tk value end na ho jaye .

x="RAJASTHAN"
print(  x  [ :2:2 ]  )

x="RAJASTHAN"
print(  x  [ :4:-1 ]  )

x="RAJASTHAN"
print(  x  [ 0:4:-1 ]  )

# right side jana tha but step size apko ulta lekar ja rha h .

x="RAJASTHAN"
print(  x  [ -1:-3 ]  )

x="RAJASTHAN"
print(  x  [ -1:-3:-1 ]  )

x="RAJASTHAN"
print(  x  [ -4 : -1 : -1 ]  )

x="RAJASTHAN"
print(  x  [ -4 : -1 : 1 ]  )

# Conditional statement

if(True):
    print("hello")

if(False):
    print("hello")

age=18
if(age==18):
    print(" you can vote")

age=19
if(age==18):
    print(" you can vote")

else:
    print("you can not vote")

age=18
country="indea"
if(age==18 and country=="indea"):
    print(" you can vote")

else:
    print("you can not vote")

country="indea"
age=18
if(country=="indea"):
    print("aadhar")
else:
    print("no aadhar")


if(age>=18):
    print("pan card")

else:
    print(" no  pan")

country=str(input("enter the country name : "))
age=int(input("enter your age : "))
if(country=="indea"):
    print("aadhar")
else:
    print("no aadhar")


if(age>=18):
    print("pan card")

else:
    print(" no  pan")

country=str(input("enter the country name : "))
age=int(input("enter your age : "))
if(age>=18):
    print("voter id + aadhar card")

elif(country=="indea"):
    print("aadhar")

else:
    print("no aadhar")
