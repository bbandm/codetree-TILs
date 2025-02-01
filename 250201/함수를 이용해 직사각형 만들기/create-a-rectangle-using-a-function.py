n, m = map(int, input().split())

# Write your code here!
def rec(n,m):
    for i in range(n):
        print("1" * m)

rec(n,m)