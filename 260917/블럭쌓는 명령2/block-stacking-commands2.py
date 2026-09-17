n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0] * n
for i in range(len(commands)):
    a = commands[i][0]
    b = commands[i][1]
    #print(a,b)
    for j in range(a,b+1):
        arr[j-1] += 1

print(max(arr))