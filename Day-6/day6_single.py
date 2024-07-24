class Animal:
    def Speak():
        return "Animal speaks"
class Cat:
    def Cat_Speaks():
        return "meow.."
class Dog:
    def Dog_Speaks():
        return "bark.."
class All(Animal,Cat,Dog):
    def All_Speaks():
        return "all"
obj1=All
print(obj1.Speak())
print(obj1.Cat_Speaks())
print(obj1.Dog_Speaks())
print(obj1.All_Speaks())


