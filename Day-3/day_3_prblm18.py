# sum of squares
n=1234568
sum=0
while(n>0):
    rem=n%10
    # sum=sum+rem*rem(sum of squaares)
    if(rem%2==0):
        sum=sum+rem
        '''sum of even digitss in a number'''
    n=n//10
print(sum)    

