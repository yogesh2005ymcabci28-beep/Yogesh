# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the hidden word S
    S = input().strip()
    # Read the guess word T
    T_word = input().strip()
    
    # Initialize an empty string for the result M
    M = ""
    
    # Iterate through each character index from 0 to 4
    for i in range(5):
        # If the characters at the i-th index are the same, append 'G'
        if S[i] == T_word[i]:
            M += "G"
        # Otherwise, append 'B'
        else:
            M += "B"
            
    # Print the resulting string M
    print(M)
