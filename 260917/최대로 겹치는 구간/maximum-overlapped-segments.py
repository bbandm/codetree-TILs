n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0] * 201
OFFSET = 100
# Please write your code here.
for i in range(n):
    a = segments[i][0]
    b = segments[i][1]
    for j in range(a,b):
        arr[j+OFFSET] += 1
print(max(arr))