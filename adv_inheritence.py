# Base class
class Parent:
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print(f"Hello, I am {self.name} from Parent class.")

#Derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

child = Child("Alice")
child.greet()
child.play()