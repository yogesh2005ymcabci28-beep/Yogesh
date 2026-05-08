# cook your dish here
import math

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N (friends) and X (cost per subscription)
    N, X = map(int, input().split())
    
    # Calculate how many subscriptions are needed
    # (N + 5) // 6 is a quick way to get the ceiling of N/6
    subs_needed = (N + 5) // 6
    
    # Calculate and print total cost
    print(subs_needed * X)
