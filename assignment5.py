year= input('enter year')
year=int(year)
if((year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print('Not a leap year')

#2Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l= int(input('enter length'))
b= int(input('enter breadth'))
if(l==b):
    print("its a square")
else:
    print("its a rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
age1= int(input('enter age of first one'))
age2= int(input('enter age of second one'))
age3= int(input('enter age of third one'))
if(age1>age2):
    if(age1>age3):
        print("first one is the oldest")
    else:
        print("third one is the oldets")
elif(age2>age3):
    print("age2 is oldest")
else:
    print("age3 is oldest")
if(age1<age2 and age1<age3):
        print("first one is the youngest")
elif(age2<age1 and age2<age3):
    print("second one is the youngest")
else:
    print("age3 is youngest")


#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

#1. if employee is female, then she will work only in urban areas.
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#4. And any other input of age should print "ERROR".

Age = int(input('Enter your Age '))
Sex = input('Enter your Gender (M or F)')
Marital_Status = input('Enter your Marital Status (Y or N')

if(Sex == 'F' or Sex=='f'):
    print("Working area will be Uran")
if((Sex == 'M'or Sex=='m') and (Age > 20 and Age < 40)):
    print('He may work anywhere')
elif((Sex == 'M'or Sex=='m') and (Age>=40 and Age < 60)):
    print('Working area will be urban')
elif(Age>60 or Sex==' ' or Sex == ''):
    print("Incorrect Age")


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

number_of_units = int(input('Enter number of units'))
Price_per_unit = 100
Total_Cost = number_of_units * Price_per_unit
if(Total_Cost > 1000):
    Total_Cost = Total_Cost - (Total_Cost * 0.01)
print(Total_Cost)
