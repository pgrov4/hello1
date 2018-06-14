print("Q.1- Name and handle the exception occured in the following program: ")
# a=3
# if a<4:
#     a=a/(a-3)
#     print(a)
#division by zero
print("Q.2- Name and handle the exception occurred in the following program:")
# l=[1,2,3]
# print(l[3])
#index out of range
print("Q.3- What will be theoutput of the following code:")
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print("An exception")
#     raise  # To determine whether the exception was raised or not
# output:raise NameError("Hi there")  # Raise Error
# NameError: Hi there
print("Q.4- What will be the output of the following code:")
# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print("a/b result in 0")
# 	else:
# 		print(c)
# output:-5.0
# a/b result in 0
# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
print("Q.5- Write a program to show and handle following exceptions:  1. Import Error 2. Value Error 3. Index Error")
# while True:
#     try:
#         x=int(input("Enter an integer:"))
#         break
#     except ValueError:
#         print("That was not a valid int! Try again")
# a=[1,2,3]
# while True:
#     try:
#         x=int(input("enter the index you want to check"))
#         if(x<2):
#             print(a[x])
#         elif(x>2):
#             raise IndexError
#             break
#     except IndexError:
#         raise IndexError("invalid index")
# print(a[x])
print("Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18). ")
class error(Exception):
    pass
class smallage(error):
    pass

age=10
while True:
    try:
        age=int(input("enter age"))
        if age<18:
            raise smallage
        break
    except smallage:
        print("age is to small")

print("you guessed is correct")