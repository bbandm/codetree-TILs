n, m = map(int, input().split())

# Write your code here!
def minMul(n,m):
    for i in range(max(n,m), n*m + 1, 1):
        if i % n == 0 and i % m == 0:
            print(i)
            return;

minMul(n,m)