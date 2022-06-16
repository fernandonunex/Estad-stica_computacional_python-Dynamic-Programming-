# 0,1,1,2,3,5,8,13,21,34
# 0,1,2,3,4,5,6,7,8,9

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

if __name__ == '__main__':
    n = int(input("Choose a number: "))
    print(fibonacci_recursivo(n))