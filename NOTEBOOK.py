# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the weight of pulp N
    n = int(input())
    
    # Since 1kg makes 10 notebooks, multiply N by 10
    result = n * 10
    
    # Output the result
    print(result)