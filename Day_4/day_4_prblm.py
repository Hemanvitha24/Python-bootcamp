# mr x is trying to set a new password for his insta account
# these are the required conditions for setting new password
# 1.min leength is 8 and max is 15
# 2.only @,/ are allowed
# 3.no spaces are allowed
# 4.only alphanumerics are allowed
# you are supposed print weak if length is exact 8,medium if length is btwn 8=12,strong if length is btwn 12-15
s=input()
length=len(s)
count=0
# ns="@,/"
countt=0
counttt=0
if(len(s)<8):
    print("follow the conditions")    
if(length>8 or length<15):
    print("")
for i in s:
    if(i==@):
       count+=1
    #    break
    if(i==/):
        countt+=1
        # print(invalid)
    if(i!=" "):
        counttt+=1
if(count==1 or countt==1 or counttt==0):
     print("valid")         
if(length==8):
        print("weak")
elif(length>=8 or length<=12):
        print("medium")
elif(length>=12 or length<=15):
        print("strong")            

                    

