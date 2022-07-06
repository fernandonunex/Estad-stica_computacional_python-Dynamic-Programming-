# 0,1,1,2,3,5,8,13,21,34
# 0,1,2,3,4,5,6,7,8,9
import functools
import sys
from functools import lru_cache

def fibonacci_recursivo(n):
    """Funtion that return the n iterarion of fibonacci"""
    if n == 0 or n == 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n, memo={}):
    """Using dynamic programming for fibonacci susession"""
    if n == 1 or n == 0:
        return n

    try:
        return memo[n]
    except KeyError:
        result = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = result

        return result

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input("Choose a number: "))
    #print(fibonacci_recursivo(n))
    print("Fibo homemade")
    print(fibonacci_dinamico(n))

    print("\nFibo for production")
    print(fibonacci(n))
    

    
