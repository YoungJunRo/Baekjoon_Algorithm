# import sys
import copy

# sys.stdin = open("input.txt", "r")

n = int(input())

block = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def move(dir):
    if dir == 0:
        for j in range(n):
            dir = 0
            for i in range(1, n):
                if block[i][j] != 0:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[dir][j] == 0:
                        block[dir][j] = temp
                    elif block[dir][j] == temp:
                        block[dir][j] =  temp * 2
                        dir += 1
                    else:
                        block[dir][j] = temp
                        dir += 1
    elif dir == 1:
        for j in range(n):
            dir = n - 1 
            for i in range(n-2, -1, -1):
                if block[i][j] != 0:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[dir][j] == 0:
                        block[dir][j] = temp
                    elif block[dir][j] == temp:
                        block[dir][j] =  temp * 2
                        dir -= 1
                    else:
                        block[dir][j] = temp
                        dir -= 1
            
    elif dir == 2:
        for i in range(n):
            dir = 0
            for j in range(1, n):
                if block[i][j] != 0:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[i][dir] == 0:
                        block[i][dir] = temp
                    elif block[i][dir] == temp:
                        block[i][dir] =  temp * 2
                        dir += 1
                    else:
                        block[i][dir] = temp
                        dir += 1

    else:
        for i in range(n):
            dir = n - 1 
            for j in range(n-2, -1, -1):
                if block[i][j] != 0:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[i][dir] == 0:
                        block[i][dir] = temp
                    elif block[i][dir] == temp:
                        block[i][dir] =  temp * 2
                        dir -= 1
                    else:
                        block[i][dir] = temp
                        dir -= 1

def dfs(cnt):
    global ans, block
    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(block[i]))
        return
        
    tmp = copy.deepcopy(block)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        block = copy.deepcopy(tmp)

dfs(0)
print(ans)