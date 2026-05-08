# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read A, B, and C for each test case
    A, B, C = map(int, input().split())
    
    # Check the condition
    if (A + B) / 2 > C:
        print("YES")
    else:
        print("NO")
