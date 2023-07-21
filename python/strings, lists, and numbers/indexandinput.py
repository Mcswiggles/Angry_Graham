'''
indexing
h e l l o
0 1 2 3 4

reverse indexing
h  e  l  l  o
0 -4 -3 -2 -1

slicing - sub section of string
[start:stop:step]
'''

mystr='hello world'
print(mystr[5])

mystr='abcdefghijk'
print(mystr[::-1])

print('please enter your first name')
first=input()
print("please enter your last name")
last=input()
username=first[0]+last[:5]
print('your username is ',username)