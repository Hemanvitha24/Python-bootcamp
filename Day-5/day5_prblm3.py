# print the unique characters in a given string
str="hello worldd"
count=""
for i in str:
    if(i not in count):
        count+=i
print(count)        