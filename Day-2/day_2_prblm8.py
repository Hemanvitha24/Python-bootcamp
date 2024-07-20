# given an space seperated integer list find the average of elments present in the even index
my_list=list(map(int,input().split()))
avg=0
sum=0
cnt=0
for i in range(0,len(my_list)):
    if(i%2==0):
      print(my_list[i])
      cnt+=1
      sum+=my_list[i]
avg=sum/cnt
print(avg)