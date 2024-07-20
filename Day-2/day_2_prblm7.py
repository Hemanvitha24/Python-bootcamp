#  6.1 you are giveen with a , seperated natural numbrs 1=10,print even numbers
# my_list=list(map(int,input().split(",")))
# my_list=[1,2,3,4,5,6,7,8,9,10]
# for i in range(1,10+1,2):
#   print(my_list[i],end=",")
# for i in range(1,len(my_list),2):
#   if(i%2==0):
#    print(my_list[i])  
#  7.1  how many even numbers are there in above question
# my_list=list(map(int,input().split(",")))
# count=0
# for i in range(1,len(my_list),2):
#  print(my_list[i])  
#  count+=1
# print(count1 8 6 4 7 )
#  you are given with a space seperaed integer list find no.of even elements and no.of odd elements in a given list
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
 if(my_list[i]%2==0):
  even+=1
#   print(even)
 else:
  odd+=1
print(even)
print(odd) 
# print(my_list[i])  