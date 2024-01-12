#wap function to find the maximum of three numbers
# def find_maximum(num1, num2, num3):
#     maximum = max(num1, num2, num3)
#     return maximum
# num1 = int(input("Enter a value of num1 : "))
# num2 = int(input("Enter a value of num2 : "))
# num3 = int(input("Enter a value of num3 : "))
# result = find_maximum(num1, num2, num3)
# print(f"The maximum of {num1}, {num2}, and {num3} is: {result}")
# wap function to sum all the numbers in a list 
# def sum_of_numbers(numbers):
#     total = sum(numbers)
#     return total
# number_list = [1, 2, 3, 4, 5]
# result = sum_of_numbers(number_list)
# print(f"The sum of the numbers in the list is: {result}")
# wap function to multiply all the numbers in a list 
# def multiply_numbers(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product
# number_list = [2, 3, 4, 5]
# result = multiply_numbers(number_list)
# print(f"The product of the numbers in the list is: {result}")
# wapp to reverse a string 
# def reverse_string(input_string):
#     reversed_string = input_string[::-1]
#     return reversed_string
# original_string = str(input("Enter a string : "))
# result = reverse_string(original_string)
# print(f"The reversed string is: {result}")
# wap function to calculate the factorial of a number 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# number = int(input("Enter a values : "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")
#wap function that takea a list and return a new list with distinct element from the first list
# def distantArr(arr):
#     result = []
#     for i in arr:
#         if i not in result:
#             result.append(i)
#     return result
# print(distantArr([1,2,3,3,3,3,4,5]))
#def distantArr(arr):
# find square and cube of a number in python 
# def squ(n):
#     return n * 2
# def cube(n):
#     return n * 3
# n = int(input("Enter a value of n : "))
# print(squ(n))
# print(cube(n))
#wap function that accepts a string and counts the number of upper and lower case letters 
# def fun(string):
#     upper = 0
#     lower = 0
#     for char in string:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#     return upper, lower
# a = str(input("Enter a string : "))
# upper, lower = fun(a)
# print(f"Uppercase letters: {a}")
# print(f"Lowercase letters: {a}")
#wap to check wheather a number is perfect or not 
# def perfectNumber(num):
#     if num <= 0:
#         return False
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     return sum == num
# print(perfectNumber(6))
#wap function that checks whether a passed string is a palindrome or not 
def palindrome(num):
    tempNum = str(num)
    return tempNum == tempNum[::-1]
num = int(input("Enter a num : "))
if palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
