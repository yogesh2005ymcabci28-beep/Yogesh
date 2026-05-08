# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the prize multiplier X
    X = int(input())
    # Read the results string (e.g., "CCNDD...")
    S = input()
    
    # Calculate Carlsen's points
    # 'C' adds 2 points, 'D' adds 1 point
    carlsen_points = S.count('C') * 2 + S.count('D')
    
    # Total points are 28, so Chef's points are (28 - Carlsen's)
    # If carlsen_points > 14, Carlsen wins
    # If carlsen_points < 14, Chef wins
    # If carlsen_points == 14, it's a tie
    
    if carlsen_points > 14:
        print(60 * X)
    elif carlsen_points < 14:
        print(40 * X)
    else:
        print(55 * X)
