s,e=(input().split())
s=int(s)
e=int(e)
for i in range(s+1,e):
        for j in range(2,i):
                if i%j==0:
                        break
                else:
                        print(i,end=' ')
                       
