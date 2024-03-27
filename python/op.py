# a=10
# b=10
# print(a+b)
# print(type(a))
# print(int.__add__(a,b))

# s1="Amaan"
# s2="Khan"
# print(s1+s2)
# print(type(s1))
# print(str.__add__(s1,s2))

# class Student:
#     def __init__(self,marks1,marks2,marks3):
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3

#     def __add__(self,other):
#         #  if isinstance(other, Student):
#             marks1=self.marks1+other.marks1
#             print(marks1)
#             marks2=self.marks2+other.marks2
#             marks3=self.marks3+other.marks3
#             s4=Student(marks1,marks2,marks3)
#             return s4
# s1=Student(10,20,20)
# s2=Student(30,40,20)
# s3=Student(30,40,20)
# s4=s1+s2+s3
# print(s4.marks1)
# print(s4.marks2)


# class Student:
#     def __init__(self,marks1,marks2):
#         self.marks1=marks1
#         self.marks2=marks2
#     def __sub__(self,other):
#         marks1=self.marks1-other.marks1
#         marks2=self.marks2-other.marks2
#         s3=Student(marks1,marks2)
#         return s3
# s1=Student(10,20)
# s2=Student(30,40)
# s3=s1-s2
# print(s3.marks1)
# print(s3.marks2)

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# print(a/b)       
# ZeroDivisionError: division by zero


# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except Exception as e:
#     print("Cannot divide by zero ")
#     print(e)
# finally:
#     print("Resource Closed")


# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Cannot divide by zero")
# except ValueError as e:
#     print("Invalid input")
# except Exception as e:
#     print("Something went wrong")
#     print(e)
# finally:
#     print("resource closed")


# class Divide:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def divide(self):
#         try:
#             c=self.a/self.b
#             print(c)
#         except ZeroDivisionError as e:
#             print("Cannot divide by zero")
#         except ValueError as e:
#             print("invalid input")
#         except Exception as e:
#             print("Something went wrong")
#         finally:
#             print("Success")
# d=Divide(4,0)
# d.divide()

