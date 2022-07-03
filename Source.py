import time
from functools import lru_cache

@lru_cache(maxsize=10)
def fab(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return(fab(n-1) + fab(n-2))

if __name__ == '__main__':
    initial_time = time.time()
    print(initial_time)
    choice = int(input("Enter the nth number of which you want to print fabonacci series number : "))
    for i in range(1, choice + 1):
        fabonacci = fab(i)
        print(f"{i}th term in Fabonacci series is : {fabonacci}")
    final_time = time.time()
    print(f"Total time taken is : {final_time-initial_time}")