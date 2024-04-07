# Write a program using functions to Compute the monthly payment, given the loan amount, number of years and

# the annual interest rate.
# loan_amount=1000
# years=4
# annual_interest_rate=4

# def calculate_monthly_payment(loan_amount, years, annual_interest_rate):
#     monthly_interest_rate = annual_interest_rate / 100 / 12
#     months = years * 12
#     monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
#     return monthly_payment

# monthly_payment = calculate_monthly_payment(loan_amount,years,annual_interest_rate)
# print(f"The monthly payment is {round(monthly_payment)}")
# from functools import reduce
# numbers_list = [2, 3, 5, 7, 11]
# def multiplication(numbers_list):
#     a=reduce(lambda x,y :x*y,numbers_list)
#     return a 
# result=multiplication(numbers_list)
# print(f"The multiplication is {result}")

# def copy_file(source):
#     try:
#         source1=open(source,"r")
#         content=source1.read()
    

#         destination = open('destination.txt',"w")
#         destination.write(content)
#         print("Copied successfully")
#     except Exception as e :
#         print(e)

# copy_file('source.txt')


# f= open('test.txt',"a")
# f.write("abcde")
# f.close()

# f1=open('test.txt',"r")
# data = f1.read()
# print(data)
# f1.close()

# f2=open('test.txt',"r")
# data=f2.read()
# content=list(data)
# total=0
# for i in content:
#     total+=1   
# print(total)

# import pickle
# data = {'name': 'John', 'age': 30, 'city': 'New York'}
# serialized_data = pickle.dumps(data)
# deserialized_data = pickle.loads(serialized_data)
# print("Original data:", data)
# print("Serialized data:", serialized_data)
# print("Deserialized data:", deserialized_data)


class Library:
    def __init__(self):
        self.acc_number = None
        self.publisher = None
        self.title = None
        self.author = None
    
    def read(self):
        self.acc_number = input("Enter Account Number: ")
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")

    def compute(self,days_late):
        total_charge = 1.50*days_late
        print(f"Total Charge is {total_charge}")

    def display(self):
        print("Account Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)


a=Library()
a.read()
b=Library()
b.compute(5)
a.display()



    




