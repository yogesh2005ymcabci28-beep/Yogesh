# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read X and Y for each test case
    x, y = map(int, input().split())
    
    # Compare the times and print the result
    if x < y:
        print("BIKE")
    elif x > y:
        print("CAR")
    else:
        print("SAME")