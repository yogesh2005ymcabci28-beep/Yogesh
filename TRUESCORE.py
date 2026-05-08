# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read A and B from the first line of the test case
    a, b = map(int, input().split())
    # Read C and D from the second line of the test case
    c, d = map(int, input().split())
    
    # Check if the goals have not decreased
    if c >= a and d >= b:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")