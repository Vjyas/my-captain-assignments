print('no.of terms:')
nt=int(input())
n1=0
n2=1
count=0
if nt == 0:
    print('enter positive value:')
elif nt==1:
    print('fibonacci series:')
    print(n1)
else:
    print('fibonacci series:')
    while count<nt:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
