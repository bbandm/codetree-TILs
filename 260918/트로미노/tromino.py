n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]
max_sum = 0
# Please write your code here.
for i in range(n-1):
    for j in range(m-1):
        arr = []
        sum_num = 0
        for k in range(4):
            arr.append(grid[i+dx[k]][j+dy[k]])
        sum_num =  sum(arr) - min(arr)
        if sum_num > max_sum:
            max_sum = sum_num

for i in range(n):
    for j in range(m-2):
        arr = []
        sum_num = 0
        for k in range(3):
            arr.append(grid[i][j+k])
        sum_num =  sum(arr)
        if sum_num > max_sum:
            max_sum = sum_num

for i in range(n-2):
    for j in range(m):
        arr = []
        sum_num = 0
        for k in range(3):
            arr.append(grid[i+k][j])
        sum_num =  sum(arr)
        if sum_num > max_sum:
            max_sum = sum_num

print(max_sum)

