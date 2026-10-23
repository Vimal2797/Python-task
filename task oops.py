# class student:
#     def fun1(self):
#         print("Vimal")
# s=student()
# s.fun1()
#
# class trainer:
#     def fun1(self):
#         print("Shiny")
# class vimal(trainer):
#     def fun2(self):
#         print("Vimal")
# t=trainer()
# v=vimal()
# t.fun1()
# v.fun1()
# v.fun2()
#
# class trainer:
#     def fun1(self):
#         print("Shiny")
# class vimal(trainer):
#     def fun2(self):
#         print("Vimal")
# class joy(trainer):
#     def fun3(self):
#         print("Joy")
# t=trainer()
# v=vimal()
# j=joy()
# t.fun1()
# v.fun1()
# v.fun2()
# j.fun1()
# j.fun3()
#
# class person:
#     def fun1(self):
#         print("Vimal")
# class movie(person):
#     def fun2(self):
#         print("Jailer 2")
# class theatre(movie):
#     def fun3(self):
#         print("PVR")
# p=person()
# m=movie()
# t=theatre()
# p.fun1()
# m.fun2()
# t.fun3()
#
# class trainer:
#     def fun1(self):
#         print("Shiny")
# class joy(trainer):
#     def fun2(self):
#         print("Joy")
# class gowsik(trainer):
#     def fun3(self):
#         print("Gowsik")
# class fees (joy,gowsik):
#     def fun4(self):
#         print("To pay fees")
# t=trainer()
# j=joy()
# g=gowsik()
# f=fees()
# t.fun1()
# j.fun2()
# g.fun3()
# f.fun1()
# f.fun2()
# f.fun3()
# f.fun4()
#
# class python:
#     def fun1(self):
#         print('Python')
# class dataanalytics:
#     def fun2(self):
#         print('Data Analytics')
# class student(python,dataanalytics):
#     def fun3(self):
#         print('Both')
# p=python()
# d=dataanalytics()
# s=student()
# p.fun1()
# d.fun2()
# s.fun1()
# s.fun2()
# s.fun3()
#
# class calulator:
#     def fun(self,a,b=0,c=0):
#         print (a+b+c)
# c=calulator()
# c.fun(10)
# c.fun(10,20)
# c.fun(10,20,30)
#
# class calculator:
#     def fun(self,*args):
#         print (sum(args))
# c=calc ulator()
# c.fun(10)
# c.fun(10,20)
# c.fun(10,20,30)

# from abc import ABC, abstractmethod
# class calculation (ABC):
#     @abstractmethod
#     def calculate(self,x,y):
#         pass
# class Addition (calculation):
#     def calculate(self,x,y):
#         return x + y
# class Subtraction (calculation):
#     def calculate(self,x,y):
#         return x - y
# class Multiplication (calculation):
#     def calculate(self,x,y):
#         return x * y
# class Division (calculation):
#     def calculate(self,x,y):
#         return x / y
# a=Addition()
# s=Subtraction()
# m=Multiplication()
# d=Division()
# result1=a.calculate(20,40)
# result2=s.calculate(10,2)
# result3=m.calculate(50,20)
# result4=d.calculate(500,2)
# print('Addition:',result1)
# print('Subtraction:',result2)
# print('Multiplication:',result3)
# print('Division:',result4)

# class student:
#     def __init__(self):
#         self.name="Vimal"
# s1=student()
# print(s1.name)

# class student:
#     def __init__(self):
#         self.name="Vimal"
# class hii:
#     def fun1(self):
#         self._hii=2697
# s1=student()
# print(s1.name)
# h=hii()
# h.fun1()
# print(h._hii)
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount >=0:
#             self.__balance=amount
#         else:
#             print("Invalid Amount")
# acc=BankAccount()
# print("Initial Balance:",acc.get_balance())
# acc.set_balance(100)
# print("Updated Balance:",acc.get_balance())
# acc.set_balance(200)

# class password:
#     def __init__(self,password):
#         self.__password='Hi2697'
# p=password()
# print(p.__password)

# number=[10,20,30,40,50]
# it=iter(number)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# text='Python'
# it=iter(text)
# while True:
#     try:
#         letter=next(it)
#         print(letter)
#     except StopIteration:
#         break

nums=[10,20,30,40,50]
it=iter(nums)
for num in it:
    print(num)