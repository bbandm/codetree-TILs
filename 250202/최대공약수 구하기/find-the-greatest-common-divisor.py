n, m = map(int, input().split())
result = 1
# Write your code here!
def maxDiv(n,m):
    for i in range(1, min(n,m), 1):
        if n % i == 0 and m % i == 0:
            result = i
    print(result)
maxDiv(n,m)