# wap to unpack a tuple in several variables 
# tuple = ("jithu","nagu","mintu")
# tuple('a','b','c')
# print(tuple["a"])
# print(tuple["b"])
# print(tuple["c"])
# wap to remove an empty tuple from a list of tuple
# sampledata = [(),(),('',),('a','b'),('a','b','c'),('d')]
# result = []
# for i in sampledata:
#     if (len(i) != 0):
#         result.append(i)
# print(result)
#wap to upzip a list of tuples into indivisuval list 
# sampledata = [(),(),('',),('a','b'),('a','b','c'),('d')]
# result = [list(i) for i in sampledata if i]
# for i in result:
#     print(i)
#wap to calculate parking charges of a vehicle enter a type of vahicle type of a character 
#c for car,b for bus,and num of hrs, then calculate the charges given below truck / bus - 20 per hrs
# car - 10 per hrs,scootor/cycle/bike - 5 per hrs
# print("Truck")
# print("Bus")
# print("Car")
# print("Scootor")
# print("Cycle")
# print("Bike")
# a = str(input("Choose the vehicle ur parking : ")).lower()
# if a == ("truck"):
#     print("cost of parking per 1 hr is 20 rupees")
# elif a == ("bus"):
#     print("cost of parking per 1 hr is 20 rupees")
# elif a == ("car"):
#     print("cost of parking per 1 hr is 10rupees")
# elif a == ("cycle"):
#     print("cost of parking per 1 hr is 5rupees")
# elif a == ("scootor"):
#     print("cost of parking per 1 hr is 5rupees")
# elif a == ("bike"):
#     print("cost of parking per 1 hr is 5rupees")
# else :
#     print("Not allowed")
# #now  we want to calculate the money after a calculating the time after 3hrs it will add
# # 10 rupees for truck and 10 rupees for car and 5rupees extra for cycle,by,scootor.
# parkingCharges = {"truck" : 20,"bus" : 20,"car" : 10,"scootor" : 5,"cycle" : 5,"bike": 5}
# extraCharges = {"truck" : 10,"bus" : 10,"car" : 10,"scootor" : 5,"cycle" : 5,"bike": 5}
# checkInTime = [int(i) for i in input("Check in Time (24 time format[00:00]): ").split(":")]
# checkOutTime = [int(i) for i in input("Check out Time (24 time format[00:00]): ").split(":")]
# hours = checkOutTime[0] - checkInTime[0]
# mins = checkOutTime[1] - checkInTime[1]
# baseHours =3
# payableHours = hours if baseHours <= hours else baseHours
# payableHours = payableHours + 1 if mins > 0 else payableHours
# finalCharge = 0
# print(f"Parking Report for your vahical {a}")
# for i in range(1, payableHours+1):

#     charge = parkingCharges[a] + extraCharges[a] if i > 3 else parkingCharges[a]
#     if i == payableHours:
#         print(f"{checkInTime[0] + i - 1}:{checkInTime[1]} to {checkOutTime[0]}:{checkOutTime[1]} is {charge} for {abs(mins)}")
#     else:
#         print(f"{checkInTime[0] + i - 1}:{checkInTime[1]} to {checkInTime[0] + i}:{checkInTime[1]} is {charge}")
#     finalCharge += charge

# print(f"Total Paking Charge: {finalCharge}")
# wap that creates dictionaries of cube of odd number in the range 1 to 10
# dictionary = {}
# for i in range(1,11,2):
#     dictionary[i] = i ** 3

# print(dictionary)
#nested tuple to print name of the topper and his/ her in 4 subjects where are in the 
#marks for specified as a list in the tuple
# topper = (
#     ("A", 9, 5, 7, 8),
#     ("B", 0, 1, 3, 2),
#     ("C", 1, 4, 5, 9),
#     ("D", 8, 9, 9, 7),)
# maxMarks , index = 0, 0
# for student in topper:
#     name, marks = student[0], student[1:]
#     totalMarks = sum(marks)
#     if totalMarks > maxMarks:
#         maxMarks = totalMarks
#         index = topper.index(student)
# print("Topper:", topper[index][0])
# print("Marks in Four Subjects:", topper[index][1:])
# wap to add a tupple 
# a = [1,3,5,6]
# b = (67,46,78)
# result = a + list(b)
# print(result)
#find the size of a tuples using using len() method .
# a = (66,77,88,"car","roy",87.65)
# print(len(a))
#python program to create a list of tuples from given list having number and its cube 
# c = [2,3,4,5,6]
# list_of_tuple = [(i, i**3) for i in c]
# print(list_of_tuple)