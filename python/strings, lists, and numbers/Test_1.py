
#Answer these 3 questions.
 #   What is the value of the expression 4 * (6 + 5)
print(4*(6+5))
#    What is the value of the expression 4 * 6 + 5
print(4*6+5)
#    What is the value of the expression 4 + 6 * 5
print(4+6*5)

#What is the type of the result of the expression 3 + 1.5 + 4?
float

#What would you use to find a number's square root, as well as its square?
#requires the below
import math
print(math.sqrt(4))
print(4**2)


#If s = 'hello' give an index command that returns 'e'. Enter your code in the cell below.
s="hello"
print(s[1])

#Now reverse the string 'hello' using slicing.
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
print('hello'[4])
print('hello'[-1])
#Build this list [0,0,0] two separate ways.
A=[0]*3
B=[0,0,0]
#Reassign 'hello' in this nested list to say 'goodbye' instead: list3 = [1,2,[3,4,'hello']].
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2]= 'goodbye'
print(list3)


#Sort the list: list4 = [5,3,2,4,6,1]
list4 = [5,3,2,4,6,1]
list4.sort()
print(list4)

