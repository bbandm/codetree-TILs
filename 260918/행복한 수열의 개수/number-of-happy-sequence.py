n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 0
# Please write your code here.
for i in range(n):
    for j in range(n-m+1):
        arr = [0] * m
        for k in range(0,m):
            arr[k] = grid[i][j+k]
        if min(arr) == max(arr):
            result += 1
            break

for i in range(n):
    for j in range(n-m+1):
        arr = [0] * m
        for k in range(0,m):
            arr[k] = grid[j+k][i]
        if min(arr) == max(arr):
            result += 1
            break

print(result)