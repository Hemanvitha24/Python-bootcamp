class Animal:
    def Speak():
        return "animal is speaking"
class Dog(Animal):
    def Speak():
        return "Bow.."
class Puppy(Dog): 
    def Speak():
        return "puppy is speaking" 
obj1=Puppy
print(obj1.Speak())  
''' returns only puppy is speaking as the method speak() is overriden
even the parent class have the same method it gets overriden'''