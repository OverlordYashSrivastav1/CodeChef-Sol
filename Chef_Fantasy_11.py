
from math import factorial
t = int(input())

while t:
    t-=1
    n = int(input())

    def total(N):
        if N < 2:
            return 0
        return factorial(N) // (factorial(2) * factorial(N-2))
    
    choices = total(n)

    print(choices*2)