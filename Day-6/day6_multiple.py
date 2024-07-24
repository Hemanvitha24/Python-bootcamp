# multiple inheritance
class Father:
    def Father_Speak():
        return "father class"
class Mother:
    def Mother_Speak():
        return "mother class"
class Kid(Father,Mother):
    def Kid_Speak():
        return "self"    
obj1=Kid
print(obj1.Father_Speak())     
print(obj1.Mother_Speak())         
print(obj1.Kid_Speak())            
