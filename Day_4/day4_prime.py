n=int(input())
r=n**0.5
count=0
if n==1:
    print("neither prime nor composite")
elif n==2:
    print("prime")
for i in range(2,int(r+1)):
    if(n%i==0):
        count=1
        break
if(count==0):
    print("prime number")
else:
    print("not a prime number")    
