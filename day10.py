# class student:
#     def __init__(self, name, age):
#         self.name="ABC"
#         self.age=18
#     def display(self):
#         print("name: ",self.name,"age:",self.age)
# obj = student("ABC",18)
# obj.display()
# obj=student("XYZ",30)
# obj.display()
# class Student:
#     count = 0
#     def __init__(self, name, age):
#         Student.count += 1
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name of the student: ", self.name)
#     def getCount(self):
#         print(Student.count)
# obj = Student("student1", 18)
# obj.display()
# obj.getCount()
# obj1 = Student("student2", 18)
# obj1.display()
# obj1.getCount()
# class Student:
#     noOfStudents = 0
#     def setData(self):
#         self.name = input("Enter your name: ")
#         self.age = int(input("Enter your age: "))
#         Student.noOfStudents += 1
#     def getData(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#     def getNoOfStudents(self):
#         return self.noOfStudents
# toggle = 1
# students = []
# while (toggle):
#     print("Select the option: ")
#     print("1. Add an Student")
#     print("2. Display All the Students")
#     print("3. department-B.Tech")
#     print("4. deparment- Pgdm")
#     print("0. Exit")
#     choice = int(input("Select: "))
#     toggle = choice if (not choice) else toggle
#     if (choice == 1):
#         student = Student()
#         student.setData()
#         students.append(student)
#     elif (choice == 2):
#         if (len(students)):
#             print("No of students: ", students[0].getNoOfStudents(), "\n\n")
#             for student in students:
#                 student.getData()
#     else:
#         print("No Studnets recorded")
# class Student:
#     noOfStudents = 0
#     btechStudents = 0
#     pgdmStudents = 0
#     def setData(self):
#         self.name = input("Enter your name: ")
#         self.age = int(input("Enter your age: "))
#         self.department = input("Enter your department: ").lower()
#         Student.noOfStudents += 1
#         Student.btechStudents = Student.btechStudents + 1 if self.department == "btech" else Student.btechStudents
#         Student.pgdmStudents = Student.pgdmStudents + 1 if self.department == "pgdm" else Student.pgdmStudents
#     def getData(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)

#     def getBTechStudents(self):
#         return self.btechStudents

#     def getPgdmStudents(self):
#         return self.pgdmStudents

#     def getNoOfStudents(self):
#         return self.noOfStudents
    
#     def getDepartment(self):
#         return self.department
# toggle = 1
# students = []

# def displayStudents(data, depertment = None):
#     if (len(data)):
#         count = 0
#         if depertment == "btech":
#             count = students[len(students) - 1].getBTechStudents()
#         elif depertment == "pgdm":
#             count = students[len(students) - 1].getPgdmStudents()
#         else:
#             count = students[len(students) - 1].getNoOfStudents()
#         print("No of students: ", count, "\n\n")

#         for student in data:
#             student.getData()
#     else:
#         print("No Studnets recorded")
        
# while (toggle):
#     print("Select the option: ")
#     print("1. Add an Student")
#     print("2. Display All the Students")
#     print("3. Display All the B.Tech Students")
#     print("4. Display All the PGDM Students")
#     print("0. Exit")

#     choice = int(input("Select: "))
#     if (not choice):
#         toggle = 1
#         print("Exiting...")
#         break
#     elif (choice == 1):
#         student = Student()
#         student.setData()
#         students.append(student)
#     elif (choice == 2):
#         displayStudents(students)
#     elif (choice == 3):
#         if (len(students)):
#             displayStudents([i for i in students if i.getDepartment() == "btech"])
#         else:
#             print("No Students")
#     elif (choice == 4):
#         if (len(students)):
#             displayStudents([i for i in students if i.getDepartment() == "pgdm"])
#         else:
#             print("No Students")
#     else:
#         print("Invalid Operator")
# wap that has a class Store which keeps a record of code and price of each product.
# display the menu of all products to the user and prompt him to enter the quantity 
# of each item required.and generate a bill and display total amount.
class Store:
    def generate_bill(self, quantities):
        total_amount = 0
        print("\nBill:")
        for Name, quantity in quantities.items():
            if Name in self.products:
                price = self.products[Name]
                subtotal = price * quantity
                print(f"Product Name: {Name}, Quantity: {quantity}, Subtotal: ${subtotal}")
                total_amount += subtotal
            else:
                print(f"Invalid product Name: {Name}")
        print(f"\nTotal Amount: {total_amount}")
def main():
    store = Store()
    store.add_product("Moringa", 100)
    store.add_product("powder", 50)
    store.add_product("Badam", 200)
    store.add_product("shampoo",12)
    store.add_product("Casunut", 1000)
    store.display_menu()
    quantities = {}
    for Name in store.products.keys():
        quantity = int(input(f"Enter quantity for Product Name {Name''''''''''''''''''''''''''''''''}: "))
        quantities[Name] = quantity
    store.generate_bill(quantities)
if __name__ == "__main__":
    main()