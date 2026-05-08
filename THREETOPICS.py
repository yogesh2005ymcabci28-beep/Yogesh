# Read the four space-separated integers from the input
a, b, c, x = map(int, input().split())

# Check if x is equal to any of the topics Chef prepared
if x == a or x == b or x == c:
    print("Yes")
else:
    print("No")