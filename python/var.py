# class Amaan:
#     def __init__(self,name):
#         self.name=name
# a=Amaan("anas")
# print(a.name)

# class Bike:
#     wheels=2
#     def __init__(self):
#         self.mil=10
#         self.speed=4
# b=Bike()
# print(b.speed)
# b.speed=5
# print(b.speed)
# b.wheels=4
# print(b.wheels)



                 #class, static,instance method
# class Student:
#     school="oreo"
#     location="mumbai"
#     def __init__(self,marks1,marks2,marks3,marks4):
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#         self.marks4=marks4
#     def avg (self): instance method
#         return (self.marks1+self.marks2+self.marks3+self.marks4)/4
       
    
    
#     @classmethod
#     def getSchool(cls):
#         return cls.school
#     @classmethod
#     def getLocation(cls):
#         return cls.location
#     @staticmethod
#     def info(a):
#         print("This is student info: ",a)
#         print("accessing class variables: ",Student.location)
    
# s1=Student(10,20,30,40)
# s2=Student(20,30,50,90)
# print(s1.avg())
# print(s2.avg())
# print(Student.getSchool())
# print(Student.getLocation())
# Student.info(5)
        
         #classmethod
# class Animal:
#     home="Jungle"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def getNameAge(self):
#         print(f"Name {self.name} AGE is {self.age}") , 
#     @classmethod
#     def animal_home(cls,home):
#         print("First the name was: ",cls.home)
#         cls.home=home
#         print("Now the name is: ",cls.home)

#     @staticmethod
#     def age1(a):
#         if(a>5):
#             print("Adult")
#         else:
#             print("Under-age")


# a=Animal("Tiger",4)
# a.getNameAge()
# Animal.animal_home("zoo")
# Animal.age1(6)

#destructor

# class Student:
#     def __init__(self):
#         print("constructoir")
#     def __del__(self):
#         print("destructor")
# s=Student()  

