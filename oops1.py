class employee:
    # special method/magic method/dunder method-> constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes/data have been initialised")

    def travel(self,destination):
        print("This travel function will called manually")
        print("Employee is travelling to ",destination)
# create an obj/instance of the class
sam=employee()

# print(sam.salary)
# sam.travel("UP")