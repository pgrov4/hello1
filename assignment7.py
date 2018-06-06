print("Q.1- Create a function to calculate the area of a sphere by taking radius from user.")

def area_sp(r):
    ar=3.14*r*r
    print("area is",+ar)
area_sp(4)
print("Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.")
print("An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].")
def perfect(x):
    sum=0
    for i in range(1,x):
        if(x%i==0):
            sum=sum+i
    if(sum==x):
        print(x)
print("perfect nos are")
for i in range(1,101):
    perfect(i)


print("Q.3- Print multiplication table of 12 using recursion.")

def multi(no,i):
    m=0
    j=i
    if(j==0):
        return m
    else:
        j=j-1
        m=no+multi(no,i-1)
        return(m)


no=12
for i in range(1,11):
    print(no,"*",+i,multi(no,i,))


print("Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.")

def power1(n,p):
    result=1
    i=p
    if(i==1):
        return n
    else:
        i=i-1
        result=n*(power1(n,p-1))
        return result
x=power1(5,3)
print(x)
print("Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary")

def fact(x):
    i=x
    if(i==1):
        return x
    else:
        return(x*fact(x-1))


dict1=dict()
#dict1={'num':int(input("enter a no")),'factorial':fact(dict1['num'])}
dict1['num']=int(input("enter a no"))
y=fact(dict1['num'])
print("number is")
print(dict1['num'])
print("factorial is")
dict1["factorial"]=fact(dict1['num'])
print(dict1['factorial'])
