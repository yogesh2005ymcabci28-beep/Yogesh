# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X (Mon-Thu hours) and Y (Friday hours)
    X, Y = map(int, input().split())
    
    # Calculate total: 4 days of X hours + 1 day of Y hours
    total_hours = (4 * X) + Y
    
    # Print the result for the current test case
    print(total_hours)
