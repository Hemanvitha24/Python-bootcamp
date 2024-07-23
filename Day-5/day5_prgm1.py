# write a prgm to print consonants
string=input()
lst="bcdfghjklmnpqrstvwxyz"
count=0
for i in string:
    if(i in lst):
        count+=1
print(count)    