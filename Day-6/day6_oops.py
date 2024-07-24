class MyClass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
obj1=MyClass
print(obj1.add(2,5))
print(obj1.sub(10,5))
print(obj1.mul(2,5))
obj2=MyClass
print(obj2.mod(8,3))
