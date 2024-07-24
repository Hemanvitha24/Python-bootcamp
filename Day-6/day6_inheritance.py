class Animal:
    def Speak():
        return "animal is speaking"
    # single inheritance
class Dog(Animal):
    def Bark():
        return "Bow.."
obj1=Animal
obj2=Dog
print(obj2.Speak())        
print(obj2.Bark())
