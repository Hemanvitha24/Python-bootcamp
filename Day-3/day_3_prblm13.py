lst=list(map(int,input().split()))
# lst[0]=max
min=lst[0]
for i in range(0,len(lst)):
    if(lst[i]<min):
        min=lst[i]
print(min)