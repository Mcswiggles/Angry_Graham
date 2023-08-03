# Lists in python

mylist=[1,2,3]
print(mylist)
print(type(mylist))

mylist=[0]*3
print(mylist)

mylist=['string',100,23.2]
print(len(mylist))

mylist=['one','two','three']
print(mylist[0])

#Slicing with lists [1:]

print(mylist[::-1])

mylist1=['one','two','three']
mylist2=['four','five','six']
newlist=mylist1+mylist2
print(newlist)

newlist[0]='ONE'
print(newlist)

newlist.append('seven')
print(newlist)
newlist.pop()
print(newlist)
newlist.pop(0)
print(newlist)

newlist=['a','e','x','b','c']
numlist=[4,1,8,3]
newlist.sort()
numlist.sort()
print(newlist)
print(numlist)

#Sort is an inplace function. They do not return a value
inplace=[7,5,1,6,8]
sort_list=inplace.sort()
print(sort_list)

#Reverse lists. 

numlist.reverse()
newlist.reverse()
print(f'{numlist}\n{newlist}')

#Real shit: tasked with creating a new library sorting system

book_names=['Lord of the Flys','Catcher and the Rye','Harry Potter','Lord of the Rings']
book_names.append('DeezNuts')
book_names.sort()

print(book_names)

book_names.pop(2)
print(book_names)