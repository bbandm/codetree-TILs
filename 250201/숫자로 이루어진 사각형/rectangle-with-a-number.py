n = int(input())

# Write your code here!
def rec(n):
    a = 1
    for i in range(n):
        for i in range(n):
            print(a, end = ' ')
            if a == 9:
                a = 0
            a += 1
        print()

rec(n)