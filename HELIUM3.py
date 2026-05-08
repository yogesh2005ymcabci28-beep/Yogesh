# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read A, B, X, Y from a single line
    a, b, x, y = map(int, input().split())
    
    # Calculate total power needed and total power available
    power_needed = a * b
    power_available = x * y
    
    # Compare and print the result
    if power_available >= power_needed:
        print("Yes")
    else:
        print("No")