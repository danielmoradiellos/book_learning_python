#!/usr/bin env python3
import shelve

d = shelve.open('shelvedata')

d['key'] = 'data'

data = d['key']

del d['key']

flag = 'key' in d
klist = list(d.keys())
print(klist)

d['xxx'] = [0,1,2]
d['xxx'].append(3)

temp = d['xxx']
temp.append(666)
d['xxx'] = temp

print(d['xx'])  #alredy in the file
print(d['xxx'])
d.close()

