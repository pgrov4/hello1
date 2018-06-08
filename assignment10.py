print("Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.")
class animal:
    def animal_attribute(self):
        print("we are in animal attribute")
class tiger(animal):
    def tiger_attribute(self):
        print("tiger attribute")
        self.animal_attribute()
t1=tiger()
t1.tiger_attribute()

print("Q.2- What will be the output of following code.")
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())


print("Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.")
class cop:
    name="abc"
    age=24
    exp=2
    designation="inspector"
    def display(self):
        print("name is",self.name)
        print("age is ",self.age)
        print("work experience is",self.exp)
        print("designation is",self.designation)
    def add(self,n,a,ex,desig):
        self.name=n
        self.age=a
        self.exp=ex
        self.designation=desig
class mission(cop):
    def add_mission_details(self):
        print("we are in mission class")
        print("cop details are")
        self.display()

c1=cop()
c1.display()
c1.add("priyanka",24,2,"inspector")
c1.display()

print("Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.")

class shape:
    ln=5
    b=6
    def area(self):
        return self.ln * self.b

class rectangle(shape):
     ln=5
     b=6
class square(shape):
    ln=5
    b=5
sh1=shape()
sh1.area()
r1=rectangle()

s1=square()
r1.area()
print("area of rectangle is")
print(r1.area())
print("area of square is")
print(s1.area())