# n = int(input("Enter a num : "))
# n = 10
# sum = 0
# i = 1
# while i<=n:
#     sum = sum+i
#     i = i+1
#     print("The sum is ", sum)
# find the lcm of any two user number
# n1 = int(input("Enter a n1 : "))
# n2 = int(input("Enter a n2 : "))

# maxNum = n1 if n1 >= n2 else n2

# while True:
#     if (maxNum % n1 == 0 and maxNum % n2 == 0):
#         print(maxNum)
#         break
#     maxNum+=1
# wap to check prime number in given range 
# n1 = int(input("Enter the n1 : "))
# n2 = int(input("Enter the n2 : "))
# print ("The Prime Numbers in the range are: ")  
# for number in range (n1, n2 + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number)

#pattern printting of triangle
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i + 1):
#         print("*", end="")
#     print()
# n = int(input("Enter a n : "))
# char = 65
# for i in range(n,0,-1):
#     for j in range(i):
#         print(char, end="")
#     print()
#     char = chr(ord(char) + 1)
#pattern printting of ABCDE
        #print(ABCDE)
        #print( BCDE)
        #print(  CDE)
# n = 5
# char = 65
# for i in range(n - 2):
#     char = 65 + i
#     for s in range(i):
#         print(" ", end ="")
#     for j in range(n - i):
#         print(chr(char), end=" ")
#         char += 1
#     print()
    
# pattern printting 
# n = 5
# char = 65
# for i in range(3,n):
#     char = 65 + n - i
#     for s in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print(chr(char), end=" ")
#         char += 1
#     print()
# for i in range(n - 2):
#     char = 65 + i
#     for s in range(i):
#         print(" ", end ="")
#     for j in range(n - i):
#         print(chr(char), end=" ")
#         char += 1
#     print()
# wap to implement the double triangle
# n = 5
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ", end = "")
#     for p in range(i):
#         print("*", end = " ")
#     for l in range(n - i):
#         print(" ",end = " ")
#     for r in range (i):
#         print("*",end = " ")
#     print()
#