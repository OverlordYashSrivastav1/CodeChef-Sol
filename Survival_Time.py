t = int(input())

while t:
    t-=1
    arr = list(map(int,input().split()))

    Days = arr[2]+(arr[0]//(arr[1]*5))

    print(Days)