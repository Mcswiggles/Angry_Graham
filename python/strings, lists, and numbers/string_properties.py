'''
name="sam"

last_letters=name[1:]
first_letter="p"
name2=first_letter+last_letters
print(name2)
'''
'''
letter='z'

x=letter*10
print(x)
'''
'''
x='I suck at python'
x=x.upper()
print(x)
x=x.lower()
print(x)

x='Hi this is a string'
print(x)
print(type(x))
x=x.split()
print(type(x))
print(x)
'''

# Formatting with the .format() function
'''
print('The {0} {1} {2}'.format('quick','brown','fox'))

print('The {q} {b} {f}2'.format(q='quick',b='brown',f='fox'))
'''

# format floating point numbers
'''
result=100/777
print('the result was {r:1.4f}'.format(r=result))
'''

# f string literals
print('please enter your name')
user_name=input()

print(f'Hello {user_name}, it is nice to meet you')