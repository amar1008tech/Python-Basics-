n=int(input("Enter No:"))
sum=0
t=n
while(t>0):
    r=t%10
    sum=sum+r*r*r
    t=t//10
if(sum==n):
    print(n,"Is Armstrong")
else:
    print(n,"Is Not Armstrong")
