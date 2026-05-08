# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N (friends) and X (slices per friend)
    N, X = map(int, input().split())
    
    total_slices = N * X
    
    # Calculate pizzas needed (rounding up)
    # Using (total + 3) // 4 is the integer way to do math.ceil(total / 4)
    pizzas = (total_slices + 3) // 4
    
    print(pizzas)
