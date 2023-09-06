from itertools import combinations
l=["aa","aaa","ab","bbb"]
comb=[]
comb2=combinations(l,2)
for i in l:
    for j in l:
        con=i+j
        comb.append(con)
for c in comb2:
    a=''.join(c)
    comb.append(a)
comb3=combinations(l,3)
for c in comb3:
    b=''.join(c)
    comb.append(b)
comb4=combinations(l,4)
for c in comb4:
    e=''.join(c)
    comb.append(e)
for i in comb:
    print(i)
j=0
n=int(input())
while(j<n):
    t=input()
    flag=1
    for i in comb:
        if (t==i):
            flag=0
            break
    if(flag==0):
        print("Yes")
    else:
        print("No")
    j=j+1