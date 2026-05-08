import math

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read N (children) and X (current candies)
    n, x = map(int, input().split())
    
    # Case 1: Chef already has enough candies
    if x >= n:
        print(0)
    else:
        # Case 2: Calculate how many more candies are required
        needed = n - x
        
        # We need the ceiling of (needed / 4)
        # You can use math.ceil() or the integer formula: (needed + 3) // 4
        packets = math.ceil(needed / 4)
        print(packets)