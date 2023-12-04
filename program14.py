class Person:
    count=0
    def __init__(self, name, age, collegename):
        self.name=name
        self.age=age
        self.collegename=collegename
        Person.count +=1
Person1= Person("Pradeepa" , 21, "AWEC")
Person2= Person("Priya" , 30, "AWEC")
print(Person.count)
print(Person1.name)
print(Person2.age)
print(Person1.collegename)

