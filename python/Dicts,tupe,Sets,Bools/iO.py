'''
Let's get some I/O up on this bitch
'''
# WE can use python to creat, edit, and write to documents
# We accomplish this by utilizing the open function
# We tell python this similar to the following example
# Using thr open function

with open('myfile.txt', 'w') as z:
        z.write('Hello, this is a text file')
        z.write('\n')
        z.write('this is the second line')
        z.write('\n')
        z.write("this is the third line")
        z.close()
# A more dumb way to do this would be to put open on every line and have it do it this way
# open('myfile.txt', 'w').write('hello, this is another line of txt')
# WTF does 'w' do? It states we want to write to the file 
#Let's open it back up and put more shit in there
with open('myfile.txt', 'w') as f:
        f.write('This is some more shit top put in here')
        f.close()

myfile=open('myfile.txt')
        

with open('myfile.txt', 'a') as f:
        f.write('\n')
        f.write("I'm sorry I suck at pyhon")
        f.close()

myfile=open('myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines()[1]) 
