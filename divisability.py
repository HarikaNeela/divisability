n=int(input())
l=[]
p=[]
for x in range(n):
    s=int(input())
    l.append(s)
for x in l:
    y=x%10
    p.append(y)
q=sum(p)
if q%10==0:
    ans="Yes"
else:
    ans="no"

# Write your code here
# ans = 

print(ans)