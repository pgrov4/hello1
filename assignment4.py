#1. Write a program to create a tuple with different data types and do the following operations.
#1. Find the length of tuples
from typing import Dict

tup="pri","priyanka",1,2
print(tup)
print(len(tup))
#Q.2-Find largest and smallest elements of a tuples.
tup1="pri","priyanka","ab","abc"
print(max(tup1))
print(min(tup1))

#Q.3- Write a program to find the product of all elements of a tuple.

#Q.1- Create two set using user defined values.
num_set=set([input("enter no"),input("enter another no")])
print(num_set)

#1. Calculate difference between two sets.
setx=set(["Red","Blue"])
sety=set(["Blue","Yellow"])
setz=setx-sety
print(setz)

#2. Compare two sets.
setx=set(["Red","Blue"])
sety=set(["Red","Blue"])
if(setx==sety):
    print("same")
else:
    print("different'")

#3. Print the result of intersection of two sets.
setx=set(["Red","Blue"])
sety=set(["Blue","Yellow"])
setz=setx & sety
print(setz)

#Q.1- Create a dictionary to store name and marks of 10 students by user input.
student_info= dict()
student_data = ['Math marks : ', 'Physics marks : ', 'Chemistry marks : ']
for i in range(0,3):
    #student_name = raw_input("Name :")
    student_info['name[i]'] = input("enter name")
    student_info['marks[i]'] = input("enter marks")
for i in range(0,3):
    print(student_info)
    #for entry in student_data:
     #   student_info[student_name][entry] = int(raw_input(entry)) #storing the marks entered as integers to perform arithmetic operations later on.
#print stude


#Q.3-
word="MISSISSIPPI"
print(word[0])
l=len(word)
ct=0
a=0
for j in range(0,l):
    a=word.count(word[j])
    print("in this",word[j],"comes",+a,"no of times")
print(a)
