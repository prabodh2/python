# to demo diff methods of list
# createation of list 
# list = ["apple", "banana", "cherry","mango"]
# print(list)
# list.append("orange")
# print(list)
# thislist = ["kajuu", "sprite", "jeera","mango"]
# print(thislist)
# list.extend(thislist)
# print(list)
# list.pop(1)
# print(list)
# list.reverse()
# print(list)
# list.insert(11,10)
# print(list)
# list.remove(10)
# print(list)
# list.sort()
# print(list)

# mylist = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(mylist[2])
# list =[[1,2,3,'a'],[5,6,7,'cat'],[9,10,11,'e'],[13,14,'beta',16]]
# print(list[3])
#aribitary lists need not be of the same length 
# list =[[1,2,3,'a'],[5,6,7],[9,10,12,'e','cat'],[13,14,'beta',16]]
# print(list[2])
#nested list can have arbitrary depth as well
# subL = [['p','q'],['r','s']]
# list =[[1,2,3,'a'],[5,6,7,'cat'],[9,10,12,'e'],[13,14,'beta',subL]]
# print(list[3][3][1][1])
#list as sequences of references 
# a = str(input["Enter a name : "])
# b = int(input["Enter a month : "])
# c = int(input["ENter a date : "])
# d = int(input["Enter a year : "])
# e = str(input["Enter a Address : "])
# f = int(input["ENter a home cell num : "])
# mylist = ['Name',['month','date','year'],"Address"['Home','cell']]
# print(mylist)
#wap to find smallest and largest number in the list
# List = []
# n = int(input("Enter the size of the elements : "))
# for i in range(n):
#     List.append(int(input(f"Enter {i+1}th element of the list: ")))
# larger = List[0]
# small = List[0]
# for i in List:
#     if (larger <= i):
#         larger = i
#     if (small >= i):
#         small = i
# print("larger: ", larger, "\n small: ", small)
#wap that defines a list of countries that are member of brics or not,
# brics = ["brazil", "russai", "india", "china", "south africa"]
# country = input("Enter the country name: ").lower()
# if country in brics:
#     print(f"{country} is member of brics country")
# else:
#     print(f"{country} is not member of brics country")
#wap to print index at which a particular value exsits. If the value exists at mutiple
#positions in the list, than all the indexes also count the number of times that value 
# is repeated in the list.
# List = [1,2,3,3,3,4,6,7,4,3,8,6,9,7]
# n = int(input("Enter the number: "))
# count = 0
# for k in range(len(List)):
#     if n == List[k]:
#         print(k)
#         count += 1
# print("Count: ", count)
# wap that forms a list of first charecter of every word in another list
# words = ["Mintu","Gagan","Jithu"]
# List = [i[0] for i in words]
# print(words)
# wap to add multidimensional 
# matrixa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrixb = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# result = []
# for i in range(len(matrixa)):
#     row = []
#     for j in range(len(matrixa[i])):
#         row.append(matrixa[i][j] + matrixb[i][j])
#     result.append(row)
# print(result)
# wap to circulate the value of n variables 
# def circular_shift(*args):
#     n = len(args)
#     shifted_values = [args[(i + 1) % n] for i in range(n)]
#     return tuple(shifted_values)

# a = 1
# b = 2
# c = 3
# print("Original values:", a, b, c)
# a, b, c = circular_shift(a, b, c)
# print("Circulated values:", a, b, c)
#tuples 
# tuple = ("apple","banana","cherry")
# print(tuple[2])
# loop through a tuple and tuple with for 
# tuple = ("apple","banana","cherry")
# for x in tuple:
#     print(x)
# tuple with if
# if "apple" in tuple:
#     print("yes,'apple' is in the fruits tuple")
#tuple length
# tuple = ("apple","banana","cherry")
# print(len(tuple))
# tuple = (0,4)
# print(tuple)
# tuple = 0,
# print(tuple)
# t = (1,3,3,3,5)
# print(t[1])
# t.index(3)
#Dictionaries 
# d = {
#     "key1" : "Value1", 
#     "key2" : "Value2", 
#     "key3" : "Value3", 
#     "key4" : "Value4"
# }
# d2 = {
#     "key5" : "Value5", 
#     "key6" : "Value6", 
#     "key7" : "Value7", 
# }
# print(d.keys())
# print(d.values())
# d.update(d2)
# print(d)
# d.pop("key6")
# print(d)
# d.clear()
# print(d)
# wap that scans the email addrres and forms a tuple of user name and tuple
# data = []
# for i in range(5):
#     email = input("Enter your email address: ").split("@")
#     tempData = {
#         "username" : email[0],
#         "domain" : email[1]}
#     data.append(tempData)

# data = tuple(data)

# print(data)
# wap to declear the list and print the list 
# list = (1,2,3,4,4,56,7,88,5)
# print("the enter the list is ", list)
# list = (1,2,3,4,5,6,7,8,9)
# print("Element are : ", list)
# for i in range(len(list)):
#     print("element at index ", i, " : ",list[i])
# list = [10,20,30,40,50,60,70,80,90,100]
# print("Element is : ")
# print(list[0:4])
# print(list[-7])
# list.append(111)
# print(list)
# list.pop(-1)
# print(list)
# list.remove(80)
# print(list)
# list.insert(3,143)
# print(list)
# count = list.count(200)
# print("100 is repeated : {coutn} times")

# list.extend([200,240,220])
# print("Print after extending list : ", list)
# list.reverse()
# print("List after reversing : ",list)
#wap to identify even no . or odd num 
# list = [11,22,33,44,55]
# even = [i for i in list if i % 2 == 0]
# odd = [i for i in list if i % 2 == 1]
# print("Even numbers: ", even)
# print("odd numbers: ", odd)
# wap irritate/traverce a list in reverse order by 3 mothds
#using reverse method
#using slicing method
#insert method
# list = [10,20,30,40,50]
# print("first list : ",list)
# list.reverse()
# print(list)
# list = [10,20,30,40,50]
# print(list[::-1])
#extend list by following appoarch 
#  by using '+' operator 
# by using append()
#by using extend()
# list = [10,20,30,40,50]
# print("original list: ", list)
# list = list + [60,70,80]
# print("Extened list: ", list)
# list = [10,20,30,40,50]
# print("original list: ", list)
# list.append(60)
# list.append(70)
# list.append(80)
# print("Extened list: ", list)
# list = [10,20,30,40,50]
# print("original list: ", list)
# list.extend([60,70,80])
# print("Extened list: ", list)
# sum and its mean for a list of 1-10
# lst = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in lst:
#     sum+= i
# print("sum ",sum)

# l = [1,2,3,4,5,6,7,6,5,4]
# for i in l:
#     if l.count(i) > 1:
#         l.remove(i)

# print(l)
# x = [[2,5,4],[1,3,9],[7,6,2]]
# y = [[1,8,5],[7,3,9],[4,0,9]]
# resultMatrix = []

# for i in range(len(x)):
#     row = []
#     for j in range(len(x[i])):
#         row.append(x[i][j] + y[i][j])
#     resultMatrix.append(row)

# print(resultMatrix)
from datetime import datetime, timedelta

def count_sundays(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    count_sundays = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6:  # Sunday
            count_sundays += 1
        current_date += timedelta(days=1)
    return count_sundays
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
current_date = input("Enter the current date (YYYY-MM-DD): ")
result = count_sundays(birth_date, current_date)
print(f"You missed {result} Sundays between {birth_date} and {current_date}.")