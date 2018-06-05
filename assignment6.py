print("Q.1- Take 10 integers from user and print it on screen.")
for i in range(1,6):
    x=input("enter a no")
    print(x)

print("Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.")
a={}
for i in range(1,4):
    a[i]=int(input("enter a no"))
for i in range(1,4):
    a[i]=a[i]*a[i]
    print(a[i])
print("Q 4.From a list containing ints, strings and floats, make three lists to store them separately")
mylist=[1,2,"pri",2.3]
#print(type(mylist[2]))
mylistint=[]
mylistfloat=[]
myliststr=[]
for i in range(0,len(mylist)):
    if(type(mylist[i])==int):
        mylistint.append(mylist[i])
    elif(type(mylist[i])==float):
        mylistfloat.append(mylist[i])
    elif (type(mylist[i]) == str):
        myliststr.append(mylist[i])
print("main list")
print(mylist)
print("integer list")
print(mylistint)
print("flloat list")
print(mylistfloat)
print("string list")
print(myliststr)

print("Q.5- Using range(1,101), make a list containing only prime numbers")
for i in range(1,101):
    j=2
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(i==j):
        print(i)
print("Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.")
i=6
while(i>5):
    print("infinite")
    i=i+1
