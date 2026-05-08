# Read X and Y from a single line of input
x, y = map(int, input().split())

# Check if current speed Y is greater than threshold X
if y > x:
    print("YES")
else:
    print("NO")
