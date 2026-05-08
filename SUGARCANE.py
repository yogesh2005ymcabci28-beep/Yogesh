# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of glasses N
    n = int(input())
    
    # Calculate profit based on the derived formula (15 * N)
    profit = n * 15
    
    # Output the result
    print(profit)