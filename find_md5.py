import random
from time import sleep, time, perf_counter
from hashlib import md5
import datetime

PI = "31415926535897931159979634685441"
E  = "27182818284590450907955982984276"
start = time()

# Current records:
N_MD5_of_digits = 32
N_MD5_of_letters = 32
N_gold_md5 = 13
N_nice_match = 12
N_Pi_MD5 = 12
N_e_MD5 = 12

password_length = 16
counter=0
rand_time=0
md5_time=0
check_time=0

def print_find(*msg):
    msg = ' '.join(msg)
    print(msg)
    with open("md5.txt", "a") as myfile:
        myfile.write(str(datetime.datetime.now()) + " " + msg + "\n")

print_find("\n\nStart...")

text = ('%32x' % random.randrange(16**32))
try:
        while(True):
                tic = perf_counter()
                text = hex(int(text,16)+1)
                toc = perf_counter()
                rand_time+=toc - tic

                tic = perf_counter()
                my_hash = md5(text.encode()).hexdigest()
                toc = perf_counter()
                md5_time+=toc - tic

                tic = perf_counter()
                if len(set(my_hash[:N_nice_match]))==1:
                        print_find("N_nice_match of %d was found!" % N_nice_match, text, my_hash)
                if text[:N_gold_md5]==my_hash[:N_gold_md5]:
                        print_find("Gold MD5 of %d was found!" % N_gold_md5, text, my_hash)
                # FOUND...
                #if my_hash[:N_MD5_of_digits].isdigit():
                #    print_find("MD5 of digits of %d was found!" % N_MD5_of_digits, text, my_hash)
                
                if my_hash[:N_MD5_of_letters].isalpha():
                        print_find("MD5 of letters of %d was found!" % N_MD5_of_letters, text, my_hash)
                if my_hash[:N_Pi_MD5] == PI[:N_Pi_MD5]:
                        print_find("Pi MD5 of %d was found!" % N_Pi_MD5, text, my_hash)
                if my_hash[:N_e_MD5] == E[:N_e_MD5]:
                        print_find("e MD5 of %d was found!" % N_e_MD5, text, my_hash)
                toc = perf_counter()
                check_time+=toc - tic

                counter+=1
                if (counter%1_000_000==0): 
                    print(".", end='', flush=True)
                    #sleep(0.01)
except KeyboardInterrupt:
        print_find("\nStop after %s iterations, for %s seconds" % (f'{counter:,}',(int(time()-start))))
        print_find(f"Random in {rand_time:0.10f} seconds")
        print_find(f"MD5 in    {md5_time:0.10f} seconds")
        print_find(f"check in  {check_time:0.10f} seconds")
