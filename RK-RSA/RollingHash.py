import csv
import random
import time
from collections import deque
import SomeModArithmetic
modinv = SomeModArithmetic.modinv

class RollingHash:
	'#todo'

	def __init__(self, base, prime):
		self.base = base
		self.baseInverse = modinv(base,prime)
		self.prime = prime
		self.h = 0
		self.magic = 1
		self.string = deque('')

	def hash(self):
		return self.h;

	def append(self,val):
		val = ord(val)
		self.h = (self.h*self.base + val)%self.prime
		self.magic = (self.magic*self.base)%self.prime
		self.string.append(val)

	def skip(self):
		#todo: update hash & magic
		val = self.string[0]
		self.magic = self.magic*self.baseInverse%self.prime
		self.h = (self.h - val*self.magic +self.prime*self.base)%self.prime
		self.string.popleft()


r = RollingHash(256,2147483647)
r.append('b')
assert r.hash() == ord('b')
#['b']

r.append('c')
assert r.hash() == (ord('b')*256 + ord('c'))
#['b', 'c']

r.skip()
assert r.hash() == ord('c')
#['c'