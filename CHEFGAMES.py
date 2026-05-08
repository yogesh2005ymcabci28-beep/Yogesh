# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the decisions of the 4 referees as a list
    R = list(map(int, input().split()))
    
    # Check if the sum of all decisions is 0
    if sum(R) == 0:
        print("IN")
    else:
        print("OUT")
