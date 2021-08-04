#!/usr/bin python3
import pickle
import string
import os.path


if( not os.path.exists('mypicklefile')):
    with open('mypicklefile', 'wb') as f1:
        pickle.dump([6], f1) 

OL = None
print(OL)


with open('mypicklefile', 'rb') as f1:
    OL = pickle.load(f1)


L = list(string.ascii_letters)
print(L)

OL.append(6)
with open('mypicklefile', 'wb') as f1:
    pickle.dump(OL, f1)
with open('mypicklefile', 'rb') as f1:
    f1.read()
OL = None
print(OL)
with open('mypicklefile', 'rb') as f1:
    OL = pickle.load(f1)
type(OL)
print(OL)

