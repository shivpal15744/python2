# -*- coding: utf-8 -*-
"""assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T-Bjp8pUXl4UvbIEh5mDWUYU7vqTEWWG

user => amount
monday
1+2 +3+ 4+5+6+7
2+3+4+5+6+7+8
3+4+5+6+7+8+9

5 =>15
11 =>42
16 => 70
"""

user = int(input("enter the number :"))
invest = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
total = 0
if user in invest:
    total = invest[user]
for i in range(1, user + 1):
    if i not in invest:
        total += i
print(total)

user = int(input("enter the number :"))
invest = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
total = 0
for i in range(1, user + 1):
    if i not in invest:
        total += i
        print(total)

user = int(input("enter the number :"))
invest = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
total = 0
for i in range(1, user + 1):
    if i not in invest:
        total += i
print(total)
