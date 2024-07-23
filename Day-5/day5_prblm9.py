# remove all the braces from the given algebraic expression
'''str="[(a+b)+c]"
a=""
# d=[(,),{,},[,]]
d="[]{}()"
for i in str:
    if i not in d:
        a+=i
print(a)        '''
str="[(a+b)+c]"
sum=""
for i in str:
    if(ord(i)==91 or ord(i)==93 or ord(i)==40 or ord(i)==41 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
print()        

