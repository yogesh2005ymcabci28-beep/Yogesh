# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X (submitted) and Y (approved)
    X, Y = map(int, input().split())
    
    # Check if approved problems are at least 50% of total problems
    # Multiplying by 2 is equivalent to checking if Y/X >= 0.5
    if 2 * Y >= X:
        print("YES")
    else:
        print("NO")