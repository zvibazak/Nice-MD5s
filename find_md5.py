import random
import string
from time import sleep, time
from hashlib import md5
import math

start = time()
N_perfect_match = 11
N_nice_match = 10
N_gold_md5 = 2
N_limit_char = 6
N_MD5_of_digits = 32
N_MD5_of_letters = 18
N_Pi_MD5 = 7
N_e_MD5 = 7

counter=0
try:
	while(True):
		text = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
		my_hash = md5(text.encode()).hexdigest()

		if len(set(my_hash))==1:
			print("Perfect match of %d was found!" % N_perfect_match, text, my_hash)
		if len(set(my_hash[:N_nice_match]))==1:
			print("N_nice_match of %d was found!" % N_nice_match, text, my_hash)
		if text==my_hash:
			print("Gold MD5 of %d was found!" % N_gold_md5, text, my_hash)
		if len(set(my_hash))<=N_limit_char:
			print("limit char of %d MD5 was found!" % N_limit_char, text, my_hash)
# FOUND...
#		if my_hash[:N_MD5_of_digits].isdigit():
#			print("MD5 of digits of %d was found!" % N_MD5_of_digits, text, my_hash)
		if my_hash[:N_MD5_of_letters].isalpha():
			print("MD5 of letters of %d was found!" % N_MD5_of_letters, text, my_hash)
		if my_hash[:N_Pi_MD5] == str(format(math.pi, '.33f').replace('.',''))[:N_Pi_MD5]:
			print("Pi MD5 of %d was found!" % N_Pi_MD5, text, my_hash)
		if my_hash[:N_e_MD5] == str(format(math.e, '.33f').replace('.',''))[:N_e_MD5]:
			print("e MD5 of %d was found!" % N_e_MD5, text, my_hash)
		
		counter+=1
		if (counter%1_000==0): print(".", end='', flush=True)
		sleep(0.0001)
except KeyboardInterrupt:
	print(" Stop after %s iterations, for %s seconds" % (f'{counter:,}',(int(time()-start))))
