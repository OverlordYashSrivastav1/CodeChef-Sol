t = int(input())

while t:

    def prime(x):
        if x<=1:
            return False
        if x<=3:
            return True
        if x%2 == 0 or x%3 == 0:
            return False
        
        i=5
        while i*i<=x:
            i+=6
            if x%i == 0 or x%(i+2) == 0:
                return False
        return True


    def win(N):
        if N%2 == 0:
            return "Bob"

          
        if prime(N):
            return "Alice"

        for i in range(3,N+1,2):
            if N%i == 0 and prime(i):
                return "Alice"
        return "Bob"
    t-=1
    n = int(input())
    op= win(n)
    print(op)