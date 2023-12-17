N= int(input())
li= []
for i in range(N):
    line= input().split()

    if len(line)== 1:
        command= line[0]
        if command== 'Print':
            print(li)
        else:
            getattr(li,command)()
    elif len(line)==2:
        command,n= line
        n= int(n)
        getattr(li,command)(n)

    elif len(line)== 3:
        command,n,m= line
        n= int(n)
        m= int(m)
        getattr(li,command)(n,m)
        