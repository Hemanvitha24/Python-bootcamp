a=int(input())
b=int(input())
lcm=a*b
while(b!=0):
        a,b=b,a%b
        gcd=a
lcm=lcm/gcd              
print(lcm)        