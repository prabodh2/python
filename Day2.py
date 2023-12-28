# Num = 3
# if Num > 0 :
#     print(Num, "is positive number")
#     print("testing")
#     print("This is always printed")
#odd or even
# a = int(input("Enter a number : "))
# if (a%2 == 0):
#     print("even")
# else
#     print("odd")

#wap to find gradde of a student
# a = int(input("Enter a number : "))
# if a >= 70:
#     print("Distinction")
# elif a >= 60:
#     print("first class")
# elif a >= 50:
#     print("second class")
# else:
#     print("pass class")
#create a program by using for loop in py
# sum=0
# for i in range (1,11):
#     sum+=i
# print("Sum is",sum)
#* wap to print below pattern
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print("******")
# for i in range(0,5):
#     for j in range(0,1+i):
#         print("* ",end="")
#         print()
#         or
# n = int(input("Enter a number : "))
# for i in range (1,n+1):
#     for j in range(0,i):
#         print ("*",end=" ")
    
#     print("\n",end="")
#* reverse pattern
# n = int(input("Enter the number of rows: "))

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# n = int(input("ENter the noum of rows : "))
# for i in range (1,n+1):
#     for j in range (0,i,1):
#         print ("i",end="  ")
#     print()
# val =65
# for i in range(0,5):
#     for j in range(0,i+1):
#         ch=chr(val)
#         print(ch,end="")
#         val = val+1
#     print()
#* diamond pattern printing in python
# row = int(input("Enter the num of rows : "))
# for i in range(1, row+1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()
# for i in range(row-1,0, -1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()
#* holo diamond pattern printing
# row = int(input("Enter the num of rows : "))
# for i in range(1, row+1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         if j==1 or j==2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(row-1,0, -1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         if j==1 or j==2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#create a hert in python
# n = 6
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
# create a star pattern printing in py
# row = int(input("Enter the num of rows : "))
# for i in range(1, row+1):
#     for j in range(1,row-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         if j==1 or j==2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()