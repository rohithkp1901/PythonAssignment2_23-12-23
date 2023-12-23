n=int(input('Enter a number: '))
if n<=1:
    p=False
else:
    p=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            p=False
            break
if p:
    print(n,'is a prime number')
else:
    print(n, 'is not a prime number')