# multi level
class Animal:
    def Speak():
        return "animal is speaking"
class Dog(Animal):
    def Bark():
        return "Bow.."
class Puppy(Dog): 
    def Puppy_Speak():
        return "iam puppy"    
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj3.Speak())        
print(obj3.Bark())
print(obj3.Puppy_Speak())