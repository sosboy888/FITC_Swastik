for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sum(a)
    for t in a:
        if not t:
            c+=1
    if k==0:
        print('NO')
    elif k==100:
        print('YES')
    else:
        if k>101 or k<100:
            print('NO')
        else:
            print('YES')
