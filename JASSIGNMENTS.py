# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the start time X
    X = int(input())
    
    # Check if he can finish by 10 PM
    if X + 3 <= 10:
        print("Yes")
    else:
        print("No")

