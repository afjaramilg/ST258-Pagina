class Animal:
    
    def __init__(self,name = "Animal"):
        self.name = name

    def to_string(self):
        print(f"This being is: {self.name}")

class Dog(Animal):
    
    def __init__(self, name = "Dog"):
        super(Dog,self).__init__(name)

    def bark(self):
        print(f"{self.name}: Barking...Wooof")
    
    def eat(self):
        print(f"{self.name} eats kibble...")

class BabyDog(Dog):

    def __init__(self, name = "Babydog"):
        super(BabyDog, self).__init__(name)

    def weep():
        print(f"{self.name} weeping...")

animal = Animal()
animal.to_string()
dog = Dog("dog")
dog.to_string()
babydog = BabyDog("babydog")
babydog.to_string()