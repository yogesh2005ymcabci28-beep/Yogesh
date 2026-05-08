# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the total amount X
    X = int(input())
    
    # Determine the discount based on the value of X
    if X <= 100:
        discount = 0
    elif X <= 1000:
        discount = 25
    elif X <= 5000:
        discount = 100
    else:
        discount = 500
        
    # Print the final amount (Total - Discount)
    print(X - discount)
