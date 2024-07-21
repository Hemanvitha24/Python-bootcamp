# replace the elements in an arary with avg of max and min element in and min elements in aray
lst=list(map(int,input().split()))
# lst[0]=max
max=lst[0]
min=lst[0]
for i in range(0,len(lst)):
    if(lst[i]>max):
        max=lst[i]
    if(lst[i]<min):
        min=lst[i]
print(max)    
print(min)
for i in range(len(lst)):
 avg=(max+min)/2
# lst[i]=avg
# avg=lst[i]
# print(avg)
 lst[i]=avg
print(lst)