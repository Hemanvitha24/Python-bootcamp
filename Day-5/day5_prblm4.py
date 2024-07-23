# sum of digits in a string
str="hello123world"
d="1234567890"
summ=0
for i in str:
    if i in d:
       summ+=int(i)
print(summ)  
# summ=sum(summ[i])
# print(summ.sum())

  