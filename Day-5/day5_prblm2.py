# print all the vowels followed by consonantsstring=input()
# d=['a','e','i','o','u']
string="hello world"
d="aeiou"
lst="bcdfghjklmnpqrstvwxyz"
cs=""
for i in string:
    if i in d:
        cs+=i
for i in string:
    if i in lst:
        cs+=i
print(cs)        
    