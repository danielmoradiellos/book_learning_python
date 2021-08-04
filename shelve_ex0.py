#!/usr/bin/env python3
import shelve

d = shelve.open('shelvedata')

d['key'] = 'data'

data = d['key']

del d['key']

flag = 'key' in d
klist = list(d.keys())
print(klist)

d['xxx'] = [0,1,2]

temp = d['xxx']
temp.append(666)
temp.pop(0)
d['xxx'] = temp

print(d['xx'])  # alredy in the file : 
                # d['xx'] = [0,1,2]
                # d['xx'].append(5)
print(d['xxx'])
d.close()

