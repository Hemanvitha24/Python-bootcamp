# method overloading-compiletime
# method overriding-runtime

'''class Cal:
   def add(a,b,c):
      return a+b+c
obj1=Cal
print(obj1.add(1,2,3))  
# static inputs '''

'''
class Cal:
    def add(self,*args):
        return sum(args)
obj1=Cal
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
'''


# variable length arguments method for method overloading
class Cal:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return (sum)
obj1=Cal()
print(obj1.add(1,2))
# print(obj1.add(1,2,3))
# print(obj1.add(1,2,3,4))
 