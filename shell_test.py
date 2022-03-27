# -*- coding: utf-8 -*-

# backward compatible
# La rétrocompatibilité, ou compatibilité descendante, est la
# compatibilité d'un produit vis-à-vis de ses anciennes versions ☠
import sys

while True:
 if sys.version[0] == '2': input = raw_input
 reply = input('Enter text:')
 # reply = raw_input('Enter text:') for python2

 if reply == 'stop':break
 print(reply.upper())

