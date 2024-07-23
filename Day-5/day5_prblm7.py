'''str="hello1234world"
sum=0
for i in str:
 if(ord(i)>=48 and ord(i)<=57):
    sum+=int(i)
print(sum)        '''
str="hello1234world"
sum=""
for i in str:
 if(ord(i)>=97 and ord(i)<=122):
    sum+=i
print(sum)        