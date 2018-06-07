print("Q.1- What is Time Tuple?")
from datetime import datetime

dt = datetime(2018, 8, 4)
print(dt.timetuple())


print("Q.2- Write a program to get formatted time.")
import time
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)


print("Q.3- Extract month from the time.")
import calendar

cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)
import datetime

m = datetime.date.today()
#print('%02d' % m.month)
cal=calendar.month(m.year,m.month)
print(cal)

print("Q.4- Extract day from the time.")
print(datetime.datetime.today().weekday())
#today = datetime.datetime(2017, 10, 20)
#today.get_weekday()

print("Q.5- Extract date (ex : 11 in 11/01/2021) from the time.")
d=datetime.date.today()
print(d)


print("Q.6- Write a program to print time using localtime method.")
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

print("Q.7- Find the factorial of a number input by user using math package functions.")
import math
x=math.factorial(int(input("enter no for factorial")))
print(x)

print("Q.8- Find the GCD of a number input by user using math package functions.")
y=math.gcd(12,18)
print(y)
print("Q.9- Use OS package and do the following tasks:")
print("1. Get current working directory.")
print("2. Get the user environment.")
import os
print(os.getcwd())
print(os.environ)

