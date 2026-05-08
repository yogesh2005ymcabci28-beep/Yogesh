t = int(input())

while t > 0:
    n = int(input())
    s = input()
    
    # Alice starts as the server
    current_server = 'A'
    alice_score = 0
    bob_score = 0
    
    # Iterate through each point won in the string
    for winner in s:
        if winner == current_server:
            # If the current server wins the point, they get a score
            if current_server == 'A':
                alice_score += 1
            else:
                bob_score += 1
        else:
            # If the receiver wins, they simply become the server
            current_server = winner
            
    # Output the final scores for Alice and Bob
    print(alice_score, bob_score)
    
    t -= 1