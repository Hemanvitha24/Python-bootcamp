#  print the element in a particular index 
my_list=list(map(int,input().split()))
k=int(input())
for i in range(1,len(my_list)):  
 rem=k%len(my_list)
# print(rem)
print(my_list[i])