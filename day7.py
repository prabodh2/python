#  simple program in functions      || positional argument,key word base argument, Dry = dont repeat your slef 
# def my_function():                || wet = we enjoying typing 
#     print ('Hello Students')
# my_function()
#add in function
# def my_function(a,b):
#     return a+b
# str = my_function(7,2)
# print(str)
# simple calculator by using function
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mul(a,b):
#     return a * b
# def div(a,b):
#     return a / b
# def sqa(a):
#     return a*2
# def add1():
#     return 1 + 3
# def sub1():
#     return 3 - 1
# def mul1():
#     return 3 * 2
# def div1():
#     return 3 / 2
# print(add(1,2))
# print(sub(1,2))
# print(mul(1,2))
# print(div(1,2))
# print(add1())
# print(sub1())
# print(mul1())
# print(div1())
# arguments types are positional argument , key word based argument
#simple example 
# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(sum(1,2,3))
# simple example 1
# def avg(*nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum / len(nums)
# print(avg(1,2,3))
# simple example 2
# def my_fun(a):
#     print (a)
# my_fun(5*3+4)
# we want to take input from user and add to list and and do addtion 
# def Values(*args):
#     sum = 0
#     for i in args[0]:
#         sum += i
#     return sum
# n = int(input("Enter number of numbers: "))
# list = []
# for i in range(n):
#     user= int(input("Enter the number: "))
#     list.append (user)
# print(Values(list))
#simple example 3
# def my_fun(a,*args):
#     my_fun (a=1,b=2,args=(3,4,5))
# print(my_fun("a"))
# def my_function(a,b,*args):
#     print(a)
#     print (b)
#     print(args)
# my_function(1,2,3,4,5)
#simple heart
# n = int(input("Enter a size of heart : "))
# for i in range(n//2, n, 2):
#     for j in range(1, n-i ,2):
#         print(" ", end="")
#     for j in range(1, i+1, 1):
#         print("*", end="")
#     for j in range(1, n-i+1, 1):
#         print(" ", end="")
#     for j in range(1, i+1, 1):
#         print("*", end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(i, n, 1):
#         print(" ", end="")
#     for j in range(1, i*2, 1):
#         print("*", end="")
#     print()

# def add(a,b,args):

#     sum1=sum(args)
#     return sum1
# l=int(input("Enter number of arguements: "))
# my_list=[]
# for i in range(l):
#     my_list.append(int(input(f"Enter value: ")))
# x=5
# y=0
# print(add(my_list,a=x,b=y))
# print(add(12,10,11,10,10))
# print(add(1,2,5,a=10,b=10))
# a = str(input("What is ur name : "))
# print("Welcome", a, "to itm ")
# take a user input like name,age,mail,and print 
# import random
# def getData(**userData):
#     userData['id'] = int(random.randint(1,47))
#     print("Successfully registered")
#     print("User Details: ")
#     print(f"id: {userData['id']}")
#     if userData['name']:
#         print(f"Name: {userData['name']}")
#     if userData["email"]:
#         print(f"Email: {userData['email']}")
#     if userData["age"]:
#         print(f"age: {userData['age']}")

# print("Enter your details")
# userName = ""
# userAge = 0
# userEmail = ""

# userChoice = int(input("Do you wanna add username(1-Yes, 0-No): "))
# if userChoice == 1:
#     userName = input("Name: ")
    
# userChoice = int(input("Do you wanna add age(1-Yes, 0-No): "))
# if userChoice == 1:
#     userAge = int(input("age: "))
    
# userChoice = int(input("Do you wanna add email(1-Yes, 0-No): "))
# if userChoice == 1:
#     userEmail = input("Email: ")
    
# getData(name = userName, age = userAge, email = userEmail)          