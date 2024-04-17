"""OOPS
Define a class called Person with properties like name, age, mobile, set those values by
taking input from the user, and print the values by getting the values using class objects."""
class Person:#Creation of class
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.mobile = input("Enter your mobile number: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

# Create a new Person object and set its properties
person = Person()

# Display the Person's properties
person.display()