for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sum(a)
    c=0
    for t in a:
        if not t:
            c+=1
    if c==0:
        print('NO')
    elif c==k:
        print('YES')
    else:
        if c%2==1:
            print('NO')
        else:
            print('YES')
