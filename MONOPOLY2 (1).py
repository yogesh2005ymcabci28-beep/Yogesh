# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the profits of the four companies
    p, q, r, s = map(int, input().split())
    
    # Check if any company's profit is greater than the sum of the others
    if (p > q + r + s) or (q > p + r + s) or (r > p + q + s) or (s > p + q + r):
        print("YES")
    else:
        print("NO")