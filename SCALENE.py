t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    print('Yes' if a < b and b < c else 'No')
    t -= 1
