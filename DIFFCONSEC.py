# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the length of the string
    N = int(input())
    # Read the binary string
    S = input()
    
    operations = 0
    
    # Iterate through the string and check adjacent characters
    for i in range(N - 1):
        # If two consecutive characters are the same, we need an operation
        if S[i] == S[i+1]:
            operations += 1
            
    # Output the total count for this test case
    print(operations)
