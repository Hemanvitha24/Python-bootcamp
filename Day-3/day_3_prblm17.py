# find the duplicates in an array
lst=list(map(int,input().split()))
new_lst=[]
for i in lst:
 if(i not in new_lst):
    new_lst.append(i)
print(new_lst)    