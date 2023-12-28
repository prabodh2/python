# inheritance =
#single inheritance = single base class and single derived class
# class Parent:
#     def add(self):
#         return self.x + self.y
# class Child(Parent):
#     def take(self):
#         self.x = int(input("Enter 1st value: "))
#         self.y = int(input("Enter 2nd value: "))
# obj = Child()
# obj.take()
# obj.add()
# print(obj.add())
# class shape:
#     def add(self):
#         return self.x * self.y
# class Child(shape):
#     def take(self):
#         self.x = int(input("Enter 1st value: "))
#         self.y = int(input("Enter 2nd value: "))
# obj = Child()
# obj.take()
# obj.add()
# print(obj.add())
# class Shape:
#     def area(self,length1,length2 = None):
#         if length2:
#             return length1 * length2
#         return length1 ** 2
# class Area(Shape):
#     def take(self):
#         choice = int(input("Chose the shape(1- Square, 2- Rectangle)"))
#         lengths = [int(input("Enter: ")) for k in range(choice)]
#         print("Area: ",self.area(*lengths))
# obj = Area()
# obj.take()
# multiple inheritance = 2 base class and 1 derived class 
# class Letsupgrade:
#     sub = ("Full Stack Web development", "AI/ML", "Web 3.O")
#     trainer = ("Trainer 1", "Trainer 2", "Trainer 3")
#     duration = ("6 months","8 months","4 months")
#     def selectLUCourse(self, index):
#         return {"sub" : self.sub[index], "trainer" : self.trainer[index], "duration" : self.duration[index]}
#     def displayLUCourse(self):
#         for i in range(len(self.sub)):
#             print("Subject id: ",i+1)
#             print("Sub: ", self.sub[i])
#             print("Trainer: ", self.trainer[i])
#             print("duration: ", self.duration[i])
# class ITM:
#     ITMSub = ("C++", "DSA", "Management","Python","Java script")
#     ITMTrainer = ("ITM Trainer 1", "ITM Trainer 2", "Trainer 3","Trainer 4","Trainer 5")
#     ITMDuration = ("2 months" ,"4 months" , "1 months","4 months","6 to 9 months")
#     def selectITMCourse(self, index):
#         return {"ITMSub" : self.ITMSub[index], "trainer" : self.ITMTrainer[index], "duration" : self.ITMDuration[index]}
#     def displayITMCourse(self):
#         for i in range(len(self.ITMSub)):
#             print("ITM Subject id: ",i+1)
#             print("ITM Sub: ", self.ITMSub[i])
#             print("Trainer: ", self.ITMTrainer[i])
#             print("duration: ", self.ITMDuration[i])
# class BTech(Letsupgrade, ITM):
#     LUCourses = []
#     ITMCourses = []
#     def __init__(self) -> None:
#         pass
#     def displayCourses(self):
#         self.displayLUCourse()
#         self.displayITMCourse()
#     def selectCourse(self):
#         choice = int(input("Choose: (1- Letsupgrade, 2- ITM): "))
#         id = int(input("Enter the id: "))
#         if choice == 1:
#             self.LUCourses.append(self.selectLUCourse(id))
#         elif choice == 2:
#             self.ITMCourses.append(self.selectITMCourse(id))
#     def displayEnrolledCourses(self):
#         print("Enrolled courses: ")
#         for i in self.LUCourses:
#             print(i)
#         for j in self.ITMCourses:
#             print(j)
# student = BTech()
# student.displayCourses()
# student.selectCourse()
# student.displayEnrolledCourses()
#multilevel = one base class and two derived class 
# class GrandFather:
#     def __init__(self):
#         self.name = " GrandFather"
#         self._assets = 1000
# class Father(GrandFather):
#     def __init__(self):
#         super().__init__()
#         self.name = self.name + " Father"
#         self._inharitedAssets = self._assets 
#         self._purchased = 200
#         self._totalAssets = self._inharitedAssets + self._purchased
# class Child(Father):
#     def __init__(self , name, assets):
#         super().__init__()
#         self.name = self.name + " " + name
#         self.inharitedAssets = self._assets
#         self.purchased = assets
#         self._totalAssets = self.inharitedAssets + self.purchased   
#     def displayData(self):
#         print("Name: ", self.name)
#         print("Assets: ", self._totalAssets)   
# obj = Child("Child",100000)
# obj.displayData()

# Design a library catalogue system using inheritance. take base class library item and derieved classes 
# book, dvd and journal. each derived class should have unique attributes and methohds and system should
# support checking in nd checking out System.
# class LibraryItem:
#     def __init__(self, title, call_number):
#         self.title = title
#         self.call_number = call_number
#         self.checked_out = False
#     def check_out(self):
#         if not self.checked_out:
#             self.checked_out = True
#             print(f"{self.title} checked out successfully.")
#         else:
#             print(f"{self.title} is already checked out.")
#     def check_in(self):
#         if self.checked_out:
#             self.checked_out = False
#             print(f"{self.title} checked in successfully.")
#         else:
#             print(f"{self.title} is not checked out.")
#     def display_info(self):
#         raise NotImplementedError("Subclasses must implement display_info.")
# class Book(LibraryItem):
#     def __init__(self, title, call_number, author, num_pages):
#         super().__init__(title, call_number)
#         self.author = author
#         self.num_pages = num_pages
#     def display_info(self):
#         print(f"Book: {self.title} by {self.author}, {self.num_pages} pages")
# class DVD(LibraryItem):
#     def __init__(self, title, call_number, director, duration):
#         super().__init__(title, call_number)
#         self.director = director
#         self.duration = duration
#     def display_info(self):
#         print(f"DVD: {self.title} directed by {self.director}, {self.duration} minutes")
# class Journal(LibraryItem):
#     def __init__(self, title, call_number, volume, issue):
#         super().__init__(title, call_number)
#         self.volume = volume
#         self.issue = issue
#     def display_info(self):
#         print(f"Journal: {self.title}, Volume {self.volume}, Issue {self.issue}")
# def get_user_input():
#     title = input("Enter title: ")
#     call_number = input("Enter call number: ")
#     return title, call_number
# if __name__ == "__main__":
#     item_type = input("Enter item type (Book/DVD/Journal): ").lower()
#     if item_type == "book":
#         author = input("Enter author: ")
#         num_pages = int(input("Enter number of pages: "))
#         item = Book(*get_user_input(), author, num_pages)
#     elif item_type == "dvd":
#         director = input("Enter director: ")
#         duration = int(input("Enter duration in minutes: "))
#         item = DVD(*get_user_input(), director, duration)
#     elif item_type == "journal":
#         volume = input("Enter volume: ")
#         issue = input("Enter issue: ")
#         item = Journal(*get_user_input(), volume, issue)
#     else:
#         print("Invalid item type.")
#         exit()
#     item.display_info()
#     action = input("Do you want to check out (C) or check in (I) the item? ").lower()
#     if action == "c":
#         item.check_out()
#     elif action == "i":
#         item.check_in()
#     else:

class LibraryItem:
    def __init__(self, title, author, item_id, quantity=1):
        self.title = title
        self.author = author
        self.itemId = item_id
        self.isCheckedOut = False
        self.quantity = quantity
    def displayData(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.itemId}")
        print("Status: Checked out" if self.isCheckedOut else "Status: Available")
        print(f"Quantity: {self.quantity}")
    def checkOut(self):
        if not self.isCheckedOut and self.quantity > 0:
            print(f"{self.title} has been checked out.")
            self.isCheckedOut = True
            self.quantity -= 1
        elif self.isCheckedOut:
            print(f"{self.title} is already checked out.")
        else:
            print(f"{self.title} is out of stock.")
    def checkIn(self):
        if self.isCheckedOut:
            print(f"{self.title} has been checked in.")
            self.isCheckedOut = False
            self.quantity += 1
        else:
            print(f"{self.title} is already checked in.")
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, quantity=1):
        super().__init__(title, author, item_id, quantity)
        self.genre = genre
    def displayData(self):
        super().displayData()
        print(f"Genre: {self.genre}")
class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration, quantity=1):
        super().__init__(title, director, item_id, quantity)
        self.director = director
        self.duration = duration
    def displayData(self):
        super().displayData()
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")
class Journal(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number, quantity=1):
        super().__init__(title, publisher, item_id, quantity)
        self.publisher = publisher
        self.issue_number = issue_number
    def displayData(self):
        super().displayData()
        print(f"Publisher: {self.publisher}")
        print(f"Issue Number: {self.issue_number}")
book1 = Book("Rich Dad Poor Dad", "Robert", "B01", "Finace", 1000)
dvd1 = DVD("Salaar", "Prasanth Neel", "M01", 180, 100)
journal1 = Journal("Journal", "Authur", "J01", 369, 10)
book1.displayData()
book1.checkOut()
book1.checkIn()
dvd1.displayData()
dvd1.checkOut()
journal1.displayData()
journal1.checkOut()
print("Invalid action.")