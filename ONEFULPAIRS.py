# Read a and b from input
a, b = map(int, input().split())

# Calculate the Oneful Pair expression
if a + b + (a * b) == 111:
    print("Yes")
else:
    print("No")
