import hashlib
import random
import string
import time
from concurrent.futures import ProcessPoolExecutor

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def find_matching_hash(trial_count):
    num_chars = 32
    for _ in range(trial_count):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        if md5_hash(random_string) == random_string:
            return random_string
    return None

def parallel_search(num_cpus, trial_count):
    with ProcessPoolExecutor(max_workers=num_cpus) as executor:
        results = list(executor.map(find_matching_hash, [trial_count] * num_cpus))
        return next((result for result in results if result is not None), None)

if __name__ == '__main__':
    num_cpus = int(input("Enter the number of CPUs to use: "))
    trial_count = int(input("Enter the number of trials per CPU: "))

    start_time = time.time()
    result = parallel_search(num_cpus, trial_count)

    if result:
        print(f"Found a matching string: {result}")
    else:
        print("No matching string found.")

    print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
