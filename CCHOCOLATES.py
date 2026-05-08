t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    print(int((x*5 + y*10)/z))
    t -= 1