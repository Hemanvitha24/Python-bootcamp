# i/p=hello-----wwo----rld and o/p should be --------helloworld
str="hello-----wo----rld"
count=0
# c=""
a=""
for i in str:
    if(i=='-'):
        count+=1 
    else:
        a+=i        

print("-"*count+a)        