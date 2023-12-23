fruits=[]
n=int(input('Enter the No.of Fruits'))
for i in range(n):
    a=input('Enter fruit name: ')
    fruits.append(a)
fruit_e=[a for a in fruits if 'e' in a]
print('List of fruits: ',fruits)
print('E lettered fruits: ',fruit_e)