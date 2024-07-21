# find mising number in an array
lst=list(map(int,input().split()))
n=int(input())
summ=n*(n+1)/2-sum(lst)
print(summ)
