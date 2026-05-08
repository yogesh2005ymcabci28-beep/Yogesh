# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X, Y, and Z for each test case
    X, Y, Z = map(int, input().split())
    
    # Calculate total number of students
    total_students = X * Y
    
    # Check if passing students are more than 50%
    if Z > total_students / 2:
        print("YES")
    else:
        print("NO")
