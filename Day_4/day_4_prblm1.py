# peak element
lst=list(map(int,input().split()))
# lst=[12,34,14,86,78]
# peak=0
# summ=0
for i in range(1,len(lst)-1):
    if(lst[i-1]<lst[i] and lst[i]>lst[i+1]):
     peak=lst[i]
    #  summ=summ+peak
    #  break
     print(peak,end=" ")        
# print(summ)