# -*- coding: utf-8 -*-
"""calendar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eIVCo_4XL10Z4Hsh3lkVAHKfZUxs6M-T
"""

##3. Programm to display calendar
import calendar
year=int(input("Enter the year: "))
print(calendar.calendar(year))
month=int(input("Enter the number of the month which you want to display in  the above year: "))
print(calendar.month(year,month))
date=int(input("Enter the date for which you want to know the weekday: "))
print(calendar.weekday(year,month,date))

