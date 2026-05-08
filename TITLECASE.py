# Read the number of test cases
T = int(input())

for _ in range(T):
    # Split the string into a list of words
    S = input().split()
    
    transformed_words = []
    
    for word in S:
        # Check if the word is an acronym (all characters are uppercase)
        if word == word.upper():
            transformed_words.append(word)
        else:
            # Capitalize first letter, lowercase the rest
            transformed_words.append(word.capitalize())
            
    # Join the words back into a single string separated by spaces
    print(" ".join(transformed_words))

