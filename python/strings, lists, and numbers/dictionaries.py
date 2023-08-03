# Dictionaries and you

# In dictionaries we can retrieve values without knowing where the value is at in the dictionary by calling the key

myDict={'key1':'value1','key2':'value2'}
print(myDict['key1'])

# Real World
price_lookup={'apple':2.99,'oranges':1.99,'milk':4.99}
print(price_lookup['apple'])

#Crazy shit with dicts. Dicts are flexible with what they can hold.
d={'k1':123, 'k2':[0,1,2], 'k3':{'inside_key':100}}
print(d['k1'])
print(d['k2'])
print(d['k3'])

print(d['k2'][1])
print(d['k3']['inside_key'])

mynum=d['k1']
print(mynum)
mylist=d["k2"]
print(mylist)
newDict=d['k3']
print(newDict)
newDictin=d['k3']['inside_key']
print(newDictin)

#modifying dictionaries

d['k2']=['a','b','c']
print(d['k2'])
d['k2'][0]=d['k2'][0].upper()
print(d)


d={'k1':100,'k2':200}
print(d)

d['k3']=300
print(d)

d['k1']='new value'
print(d['k1'])

print(d.keys())
print(d.values())
print(d.items())
print(d)