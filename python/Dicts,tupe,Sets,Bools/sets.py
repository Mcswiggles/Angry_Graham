'''
What are sets?
Sets are an unordered collection of unique elements

What does this mean?
Sets can only hold one representitive of the same object.

What is meant by one representitive of the same object?
You can't have more than one of the same value meaning you can't have the number 7 in there twice or the letter 'z' more than once.

A set is a collection which is unordered, unchangable*, and unindexed.
'''

myset=set()

myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2)
print(myset)

'''
Real World
'''

mylist=(1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4)
print(set(mylist))

mylist= ['a','a','a','b','b','c','c','c','A','A','B']
print(set(mylist))
