# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X (coins per bill) and Y (number of bills)
    X, Y = map(int, input().split())
    
    # Calculate total coins
    total_coins = X * Y
    
    # Calculate how many bags he can get (100 coins each)
    bags = total_coins // 100
    
    # Output the result
    print(bags)
