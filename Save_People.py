from collections import deque

def maxi(N,M,x,y):
    dir = [(1,0),(-1,0),(0,1),(0,-1)]

    grid = [[0] * M for _ in range(N)]

    grid[x-1][y-1] = 1

    que = deque([(x-1,y-1)])

    while que:
        i,j = que.popleft()
        for ax,ay in dir:
            ai,aj = i +ax,j+ay

            if 0 <= ai < N and 0<= aj < M and grid[ai][aj] == 0:
                grid[ai][aj] = grid[i][j] + 1
                que.append((ai,aj))
    maxVax = max(max(row) for row in grid)

    return maxVax
t= int(input())

while t:
    t-=1
    N, M = map(int,input().split())

    x, y = map(int,input().split())

    op = maxi(N,M,x,y)

    print(op)