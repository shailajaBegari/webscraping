n=int(input('enter the limit,space:='))
i=0
space=n
while i<=n:
    print(' '*space,end='')
    a=i+1
    j=0
    while j<=i:
        print(a-j,end='')
        j=j+1
    print()
    i=i+1
    space-=1
    