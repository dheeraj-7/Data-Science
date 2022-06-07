def prime(n):
    flag=True
    for i in range(2,n//2):
        if n%i==0:
            flag=False
            break
    if flag:
        print('Prime')
    else:
        print('Not Prime')

n=int(input('Enter a no: '))
prime(n):    
if n%2==0:
    print('Even number')
else:
    print('Not Even number')
if n%5==0:
    print('Divisible by 5')
else:
    print('Not Divisible by 5')
print('Net sum: ',n*(n+1)//2)    
        
        
