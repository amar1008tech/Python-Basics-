n=int(input("Enter No:"))
sum=0
t=n
while(t>0):
    r=t%10
    sum=(sum*10)+r
    t=t//10
if(sum==n):
    print(n,"Is Palindrome")
else:
    print(n,"Is Not Palindrome")
