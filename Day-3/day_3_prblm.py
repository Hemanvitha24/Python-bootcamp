# reverse of a number
'''n=234
sum=0
while(n>0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
print(sum)   
 '''
n=1234
rev=""
while(n>0):
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(rev))  
