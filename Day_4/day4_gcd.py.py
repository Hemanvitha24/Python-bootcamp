a=int(input())
b=int(input())
while(b!=0):
    a,b=b,a%b
print("gcd of 2 number is:",a)    