import random
import string
from time import sleep
from hashlib import md5
import time
import math

start = time.time()
N_nice_match = 7
limit_char = 8
counter=0
try:
	while(True):
		text = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
		my_hash = md5(text.encode()).hexdigest()

		if len(set(my_hash))==1:
			print("nice_pattern was found!",text,my_hash)
		if len(set(my_hash[:N_nice_match]))==1:
			print("N_nice_match of %d was found!!!!" % N_nice_match,text,my_hash)
		if text==my_hash:
			print("Gold MD5 was found!!!!",text,my_hash)
		if len(set(my_hash))==limit_char:
			print("limit char of %d MD5 was found!!!!" % limit_char,text,my_hash)
		#if my_hash.isdigit():
		#	print("All digits was found!!!!",text,my_hash)
		if my_hash.isalpha():
			print("All alphabetical characters was found!!!!",text,my_hash)
		if my_hash in [format(math.pi, '.33f').replace('.',''), format(math.e, '.33f').replace('.','')]:
			print("math consts was found!!!!",text,my_hash)
		
		counter+=1
		if (counter%1_000==0): print(".", end='', flush=True)
		sleep(0.01)
except KeyboardInterrupt:
	print(" Stop after %s iterations, for %s seconds" % (f'{counter:,}',(int(time.time()-start))))
