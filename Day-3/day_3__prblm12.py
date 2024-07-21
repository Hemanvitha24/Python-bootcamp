# find max element in a given list 
lst=list(map(int,input().split()))
# lst[0]=max
grt=lst[0]
for i in range(0,len(lst)):
    if(lst[i]>grt):
        grt=lst[i]
print(grt)
