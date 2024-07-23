# check how many vowels are there in a string
string=input()
# d=['a','e','i','o','u']
d="aeiou"
count=0
for i in string:
    if(i in d):
        count+=1
print(count)     
