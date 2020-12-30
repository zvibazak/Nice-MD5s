import random
import string
from time import sleep
from hashlib import md5

N_nice_match = 6

while(True):
  text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

  my_hash = md5(text.encode()).hexdigest()

  if len(set(my_hash))==1:
    print("nice_pattern was found!!!!")
    print(text,my_hash)
  if len(set(my_hash[:N_nice_match]))==1:
    print("N_nice_match of %d was found!!!!" % N_nice_match)
    print(text,my_hash)
  if text==my_hash:
    print("Gold MD5 was found!!!!")
    print(text,my_hash)
  sleep(0.01)
