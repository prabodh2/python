# puthon to declare asing and print the string 
# a = 'string'
# print(a)
# a1 = "string"
# print(a1)
# a2='''string'''
# print(a2)
# a3="""string"""
# print(a3)
# a5= """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a5)
#python program to access and print characters from the string
# str = "Hello world"
# print(str)
# print(str[0])
# print(str[1])
# print(str[-1])
# print(str[-2])
# print(str[0:5])
# print(str[0:5])
# print(str[1:-1])
# for i in str:
#     print(i)
# python program to find un common words from two string.
# str1 = input("Enter 1st string: ")
# str2 = input("Enter 2nd string: ")
# for i in str1:
#     if i not in str2:
#         print(i)
# for i in str2:
#     if i not in str1:
#         print(i)
# python program to check wether a given string is a binary or not 
# str = input("Enter binary: ")
# for i in str:
#     if not (i == '1' or i == '0'):
#         print("not binary")
#         break
# else:
#     print("Binary")
#python program to find the least frequent character in the string 
# input = input("Enter string: ")
# char = input[0]
# currCount = input.count(char)
# for i in input:
#     if currCount >= input.count(i):
#         char = i
#         currCount = input.count(i)
# print(char)
# create a class employee 
# class employee:
#     def __init__(self,id,name,gender,city,salary):
#         self.id=1
#         self.name="Pankaj"
#         self.gender="male"
#         self.city="delhi"
#         self.salary="55000"
#     def display(self):
#         print("id",self.id)
#         print("name",self.name)
#         print("gender",self.gender)
#         print("city",self.city)
#         print("salary",self.salary)
# e1 = employee(1,"pankaj", "male", "delhi", 55000)
# e1.display()
#python program for removing i-th character from a string 
# a = str(input("Enter a string : "))
# index = 3
# a = a[:index] + a[index + 1 :]
# print(a)