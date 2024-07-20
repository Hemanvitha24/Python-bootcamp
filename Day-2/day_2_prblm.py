my_list=list(map(int,input().split()))
# print(*my_list)
# print(f"1.append 2.pop 3.sort)
choice=int(input("enter your choice"))
if(choice==1):
     print(my_list.append(45))
elif(choice==2):
     print(my_list.pop())
elif(choice==3):
     print(my_list.sort())          
print(*my_list)     
