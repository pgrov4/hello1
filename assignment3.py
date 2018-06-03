#Create a list with user defined inputs
mylist=[input("enter  first no"),input("emter  second no")]
print(mylist)

#2.Add the following list to above created list:
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
mylist2=["google","apple","facebook","microsoft","tesla"]
mylist.extend(mylist2)
print(mylist)

#3. Count the number of time an object occurs in a list.
mylist4=["as","wsd","ab","we","ab"]
print(mylist4.count("ab"))

#4.  create a list with numbers and sort it in ascending order.
mylist3=[2,1,5,4,6,8,3]
mylist3.sort()
print(mylist3)


#5. Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
mylist5=[1,2,3,4,6,7]
mylist6=[5,8,9]
mylist5.extend(mylist6)
mylist5.sort()
print(mylist5)