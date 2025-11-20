'''class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self):
        self.behaviour = 'friendly'
    def speak1(self):
        print(f"Buddy barks. He is very {self.behaviour}")

animal = Animal("Generic Animal")
animal.speak()

dog = Dog()
dog.speak()  '''


class Animal:
    def __init__(self):
        self.name="Buddy"
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks .It is a {self.breed}.")

dog=Dog("Golden Retriver")
dog.speak()