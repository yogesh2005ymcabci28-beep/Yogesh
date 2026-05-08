# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the status of the three bottles
    B1, B2, B3 = map(int, input().split())
    
    # If the sum of full bottles is 0 or 1, then 2 or 3 are empty
    if (B1 + B2 + B3) <= 1:
        print("Water filling time")
    else:
        print("Not now")
