n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
# Please write your code here.
for i in range(0,n-2):
    for j in range(0, n-2):
        count = 0
        for k in range(3):
            for p in range(3):
                if grid[i+k][j+p] == 1:
                    count +=1
        if count > max_num:
            max_num = count

print(max_num)