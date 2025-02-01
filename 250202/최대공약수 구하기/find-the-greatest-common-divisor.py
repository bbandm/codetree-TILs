n, m = map(int, input().split())
# Write your code here!
def maxDiv(n,m):
    result = 1
    for i in range(1, min(n,m), 1):
        if n % i == 0 and m % i == 0:
            result = i
    print(result)
maxDiv(n,m)