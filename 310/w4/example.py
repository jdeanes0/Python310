"""
We are doing something today, not really sure what though.

@author jdeanes0
@version 9/18/23
"""
import time

def run_count(n):
    """Will literally count up based on the input given"""
    count = 0
    for i in range(0,n,1):
        count += 1

    print(count)

def run_constant(n):
    print(n)

def run_log(n):
    count = 0
    while count < n: # THIS STILL DOESN'T WORK!
        n /= 2
        count += 1
    
    print(count)

def main():
    """Main function that is cool and good."""
    start1 = time.time()
    run_count(300000)
    linear_time = time.time() - start1
    print(f"O(n): {linear_time}")

    start2 = time.time()
    run_constant(300000)
    constant_time = time.time() - start2
    print(f"O(1): {constant_time}")

    start3 = time.time()
    run_log(300000)
    log_time = time.time() - start3
    print(f"O(lg n): {log_time}")

main()