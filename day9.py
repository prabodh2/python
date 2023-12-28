# str = "ITM Skills University"
# print(str)
# print(str[2:10:3])
# print(str[0::-1])
# for letter in str :
#     print(letter)
# i=0
# while (i < len(str)):
#     print(str[i])
#     i+=1
# def fun(str, char):
#     if char in str:
#         return str.index(char)
#     return None
# u = input("Enter a string: ")
# s = input("Enter the char you want to search: ")
# def count(str,char):
#     return str.count(char)
# print(count("hello","l"))
# print(count("hello","a"))
# print(fun(u,s))
# str = "ITM skills university"
# print(str.find("T"))
# print(str.find("k"))
# print(str.find("e"))
# print(str.find("v"))
# print(str.find("s"))
# string = "Itm skills university"
# print("skills" in string)
# print all letters from string1 print all same letters
# str = input("Enter 1st string: ")
# str1 = input("Enter 2nd string: ")
# for i in str:
#     if i in str1:
#         print(i)
# str1 = input("Enter 1st string: ")
# str2 = input("Enter 2nd string: ")
# if (str1 == str2):
#     print("strings are equal")
# elif (str1 > str2):
#     print("string1 is greater than string2")
# else:
#     print("string1 is lesser than string2")
# print(R"Hi , \"what's up ?\"")
# name = input("Enter your name: ")
# college = input("Enter your college: ")
# print("Hello, {}. Welcome to {}".format(name, college))
# print("Hello, {1}. Welcome to {0}".format(college, name))
# print("Hello, {a}. Welcome to {b}".format(b=college, a=name))
# wap to count no.of oveals in a given string 
# ovels = ["a","e","i","o","u","A","E","I","O","U"]
# string = input("Enter a string: ")
# count = 0
# for i in string:
#     if i in ovels:
#         count += 1
# print(count)
# wap that takes a sentence and count no of words in it
# str = input("Enter a str: ").split(" ")
# print(len(str))
#wap that take list of string as a input and sort them based on there length
# l = ["hello","tesitng", "test"]
# List = [len(i) for i in l]
# List.sort()
# print(List)
#wap to check to stings are anagrams of each other 
# string1 = input("Enter 1st string: ")
# string2 = input("Enter 2st string: ")
# def func(string1, string2):
#     for i in string1:
#         if string1.count(i) != string2.count(i):
#             return False
#     return True
# print(func(string1, string2))
#wap that convert camale case to string to snake case
string = input("Enter a string: ")
for i in string:
    if i.upper() == i:
        index = string.index(i)
        upperString = string[:index]
        lowerString = string[index+1:]
        string = upperString + "_" + i.lower() + lowerString
print(string)