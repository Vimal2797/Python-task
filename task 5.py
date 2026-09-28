'''a='vimal'
print(a[0:3:1])
print(a[-3:])
print(a[::-1])
print(a[::2])
print(a[2:6:1])
print(a[0:-1])
print(a[len(a)//2])

#reverse and palindrome check
a=input('Word:')
b=a[::-1]
print(b)
if b==a:
  print('Palindrome')
else:
  print('Not a Palindrome')
'
#odd index 
a=input('Word:')
print(a[1::2])

#even index
a=input('Word:')
print(a[0::2])

#LIST
a=[1,2,3,4,5,6,7]
print(a[:3])
print(a[-3:])
print(a[::-1])
print(a[::2])
print(a[2:6])
print(a[1:-1])
b=a[len(a)//2-1:len(a)//2+1]#even list
b=a[len(a)//2]#odd list
print(b)
print(a[::2])
print(a[1::2])
c=a[-5:]
print(c)

#TUPLE
a=(1,2,3,4,5,6,7)
print(a[:3])
print(a[-3:])
print(a[::-1])
print(a[::2])
print(a[2:6])
print(a[1:-1])
print(a[::2])
print(a[1::2])
b=len(a)//2
print(a[b-1:b+1])
print(a[b:b+1])'''

#challenge
a="PythonProgramming"
print(a[0:6:1])
print(a[-5:])
print(a[::-1])
print(a[::2])



