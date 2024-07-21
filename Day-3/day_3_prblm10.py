# find the element present in k+n index
# k is given by user(3),input parameters are 3,6,8,4,61,2,n=2
my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
# sum=0
length=len(my_list)
if(length<k+n):
    print ("errorr")
else:
    for i in range(len(my_list)):
     print(my_list[k+n])
     break
