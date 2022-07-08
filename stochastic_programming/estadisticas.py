import random
import math

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x- mu)**2
    
    return acumulador / len(X)

def std(X):
    return math.sqrt(varianza(X))

if __name__ == "__main__":
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)  # mu because we are calculating the population mean
    sigma_cuadrado = varianza(X)
    sigma = std(X)
    
    print(f'Array X: {X}')
    print(f'Mean of X: {mu}')
    print(f'Variance of X: {sigma_cuadrado}')
    print(f'Standard Deviation of X: {sigma}')

