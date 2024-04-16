r1=int(input())
c1=int(input())
m= [[int(i)for i in input().split()] for r in range(r1)]  #list comprehension
identical=1
d=m[0][0]
if r1==c1:
    for r in range(r1):
        for c in range(c1):
            if r==c:
                if d!=m[r][c]:
                    identical=0
            else:
                if m[r][c]!=0:
                    identical=0
if identical==1:
    print('Identical')
else:
    print('Not Identical')        
    