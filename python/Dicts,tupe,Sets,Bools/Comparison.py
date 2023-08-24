'''
==    If the values of two operands are equal, then the condition becomes true.    (a == b) is not true.
!=    If values of two operands are not equal, then condition becomes true.    (a != b) is true.
>    If the value of left operand is greater than the value of right operand, then condition becomes true.    (a > b) is not true.
<    If the value of left operand is less than the value of right operand, then condition becomes true.    (a < b) is true.
>=    If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.    (a >= b) is not true.
<=    If the value of left operand is less than or equal to the value of right operand, then condition becomes true.    (a <= b) is true.
and when comparing more than one of the above and both should be either true or false
or when comparing more than one og the above and the only one should be either true or false
'''
x=2
y=1
print(2==2)
print(2==1)
mybool=x==y
print(mybool)
print(2!=2)
print(2!=1)

print(3>1)
print(3>5)

print(3<5)
print(3<1)

print('Hello'=='bye')
print('Hello'=='hello')

print('2'==2)
print(2.0==2)

print('h'=='h'and 2==2)
print('h'=='h'and 2==1)

print('h'=='h'or 2==2)
print('h'=='h'or 2==1)
print('h'=='x'or 2==1)

print(not 1==1)
print(not 100>1000)