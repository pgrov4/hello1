print("Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.")
class circle:
    r=5
    def getarea(self):
        return(3.14*self.r*self.r)
    def circum(self):
        return(2*3.14*self.r)
c1=circle()
print(c1.getarea())
print(c1.circum())
print("Q.2- Create a Student class and initialize it with name and roll number. Make methods to :")
print("1. Display - It should display all informations of the student.")
class student:
    name="priyanka"
    rollno=4
    def display(self):
        print("name=",self.name)
        print("rollno=",self.rollno)
s1=student()
s1.display()
print("Q.3- Create a Temprature class. Make two methods :")
print("1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.")
print("2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.")
class temp:
    c=0
    f=0
    def ctof(self):
        return(self.c*1.8+32)
    def ftoc(self):
        return((self.f-32)*0.55)
t1=temp()
print("1.convert celsius to farenheit")
print("2. convert farenheit to celsius")
ch=int(input("enter your choice"))
if(ch==1):
    t1.c=int(input("enter celcius"))
    print(t1.ctof())
if(ch==2):
    t1.f=int(input("enter farenheit temerature"))
    print(t1.ftoc())

print("**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .")
print("Make methods to 1. Display-Display the details.2. Update- Update the movie details.")
class movie:
    mname=""
    aname=""
    yor=""
    def __init__(self,name,artist,year):
        self.mname=name
        self.aname=artist
        self.yor=year
    def display(self):
        print("movie is",self.mname)
        print("artist name is",self.aname)
        print("year of release is",self.yor)
    def update(self,name,artist,year):
        self.mname = name
        self.aname = artist
        self.yor = year
m1=movie("deadpool2","ryan reynolds","2018")
m1.display()
m1.update("avengers:infinity war","robert Downey",2018)
m1.display()


print("Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.")
print("1. Display expenditure and savings  2. Calculate total salary 3. Display salary")

class expend:
    exp=0
    salary=0
    def __init__(self,e,s):
        self.exp=e
        self.salary=s
    def display(self):
        print("expenditure=",self.exp)
        print("salary is",self.salary)
    def calsalary(self,basic):
        self.salary=basic+basic*0.5+basic*0.3
e1=expend(20000,40000)
e1.display()
e1.calsalary(20000)
e1.display()




