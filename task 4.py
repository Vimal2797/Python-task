a='vimal'
'''print(a[0:3:1])
print(a[-3:])
print(a[::-1])
print(a[::2])
print(a[2:6:1])
print(a[0:-1])
print(a[len(a)//2])'''

#reverse and palindrome check
print(a[::-1])
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if b==a:
    print('Palindrome')
else:
    print('Not Palindrome')
