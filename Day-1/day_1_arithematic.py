a=int(input())
print(a)
if(a%2==0 and a>0):
  print("a is even and positive")
elif(a%2==0 and a<0):
  print("a is even and negative")
elif(a%2!=0 and a>0):
  print("a is odd and positive")
elif(a%2!=0 and a<0):
  print("a is odd and negative")  
else:
  print("0")  