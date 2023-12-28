# lists
# x = [1,'Hello',(3+2j)]
# print(x)
# print (x[2])
# print (x[0:2])
# x = [1,2,3]
# y = x[1] = 15
# print (x)
# print (y)
# x.append (12)
# print (y)
# x = [1,2,3]
# y = x
# z = x.append(12)
# z == None
# print (z)
# print (y)
# x = x+[9,10]
# print (x)
# print (y)
#tuples 
# x = (1,2,3)
# print (x[1:])
# y = (2,)
# print (y)
# Dicctionaries
# Dicctionaries is equal to key word
# Dicctionaries are mutable 
# d = {1:'Hello','two':42,'blah':[1,2,3]}
# print (d)
# print (d['blah'])
#Dicctionaries in side Dicctionaries de code
# d = {
#     "k1": {
#         1 : "hey",
#         2: "guyss"
#     },
#     "k2": "V1",
#     "k3": "V2"
# }
# print(d["k1"][1])
# del (d["k2"])
# print (d)
# wap program to create list ,tuple,dicctionaries of 7 elements
# lst = [1,2,3,4,5,6,7]
# t1 = (1,2,3,4,5,6,7)
# d = {1: "value1", 2: "value2", 3: "value3", 4: "value4", 5: "value5", 6: "value6", 7:"value7"}
# print("list",lst)
# print("tuple",t1)
# print("dictionary",d)
# wap to arrage list in decending order
# n = int(input("Enter the size of an array: "))
# arr = []
# for i in range(n):
#     arr.append(int(input(f"Enter the {i}the element of the array: ")))
# for i in range(n):
#     for j in range(n-1):
#         if arr[j] < arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
# print(arr)
# wap to create tuples of diff data types
# t2 = (1,4.3,"string",3+4j,[1,2,3], True, False, (1,2,3), {1: "test1"})
# print(t2)
# wap to demostration loop control statement break
# while True:
#     userChoice = input("Do you want to play game (y-Yes, N-no): ").lower()
#     if (userChoice == "y" or userChoice == "yes"):
#         print("yooo, Yooo!!!")
#     else:
#         break
# develop a program to mange a library use control structure or statement 
# to add search for check out book and matain liabrary inventory system
# books = []
# cart = []

# while (True):
#     print("Select an option")
#     print("1. Add a new Book")
#     print("2. display all books")
#     print("3. display a book")
#     print("4. add a book to cart")
#     print("5. display all books in cart")
#     print("0. Exit")
    
#     userChoice = int(input("Selct: "))
#     if (userChoice == 0):
#         print("Exiting...")
#         break
#     elif (userChoice == 1):
#         bookData = {}
#         bookData["id"] = len(books)
#         bookData["bookName"] = input("Book Name: ")
#         bookData["bookDescription"] = input("Description: ")
#         bookData["price"] = input("Price: ")
#         bookData["quantity"] = int(input("Quantity: "))
#         books.append(bookData)

#     elif (userChoice == 2):
#         if (len(books) == 0):
#             print("No Books to display!!!")
#         else:
#             print(f"There are {len(books)} books to display")
#             for i in range(len(books)):
#                 print(f"Book Id: {books[i]['id']}")
#                 print(f"Book Name: {books[i]['bookName']}")
#                 print(f"Book Description: {books[i]['bookDescription']}")
#                 print(f"Book Price: {books[i]['price']}")
#                 print(f"Book quantity: {books[i]['quantity']}")

#     elif (userChoice == 3):
#         id = int(input("Enter the id to select the book: "))
#         try:
#             print(f"Book Id: {books[id]['id']}")
#             print(f"Book Name: {books[id]['bookName']}")
#             print(f"Book Description: {books[id]['bookDescription']}")
#             print(f"Book Price: {books[id]['price']}")
#             print(f"Book quantity: {books[id]['quantity']}")
#         except:
#             print("Ivalid id, book found!!!")
    
#     elif (userChoice == 4):
#         id = int(input("Enter the id to select the book: "))
#         try:
#             print(f"Book Id: {books[id]['id']}")
#             print(f"Book Name: {books[id]['bookName']}")
#             print(f"Book Description: {books[id]['bookDescription']}")
#             print(f"Book Price: {books[id]['price']}")
#             print(f"Book quantity: {books[id]['quantity']}")
#             quantity = int(input("Enter the quantity: "))
#             if (quantity > books[id]['quantity']):
#                 print("out of stock, please try again!!!")
#             else:
#                 books[id]['quantity'] -= quantity
#                 cart.append(books[id])
#                 books[id]['quantity'] = quantity

#         except:
#             print("Ivalid id, book found!!!")

#     elif (userChoice == 5):
#         if (len(cart) == 0):
#             print("No Books to display!!!")
#         else:
#             print(f"There are {len(cart)} books to display")
#             for i in range(len(cart)):
#                 print(f"Book Id: {cart[i]['id']}")
#                 print(f"Book Name: {cart[i]['bookName']}")
#                 print(f"Book Description: {cart[i]['bookDescription']}")
#                 print(f"Book Price: {cart[i]['price']}")
#                 print(f"Book quantity: {cart[i]['quantity']}")

#     else:
#         print("Ivalid choice, please try again!!!")
x = 3**1**2
print(x)