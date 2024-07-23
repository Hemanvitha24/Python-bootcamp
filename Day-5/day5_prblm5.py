# reverse the numbers present in a given string
str="hello1234world"
a="1234"
b=(int(a))
print(b)
sum=0
while(b>0):
    r=b%10
    sum=sum*10+r
    b=b//10
print(sum)    