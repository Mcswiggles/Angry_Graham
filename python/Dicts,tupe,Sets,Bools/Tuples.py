'''
Tuples are very similar to lists. However, they are immutable
Tuples are defined using() (1,2,3)
'''

# Create our first tuple
t=(1,2,3)
# Let's also create a list to compare it to
myList=[1,2,3]

print(type(t))
print(type(myList))

print(len(t))
print(t[0])

# Indexing and slicing of tuples
print(t[0])
print(t[-1])
print(t[1:])

# Working with tuple methods
t= ('a','a','b')
print(t.count('a'))

print(t.index('a'))
print(t.index('b'))

myList[0]=5
print(myList)

t[0]=5
print(t)