t = int(input())

while t > 0:
    s = input()
    vowels = "aeiou"
    is_happy = False
    n = len(s)
    
    # Check every substring of length 3
    for i in range(n - 2):
        # Check if current character and the next two are vowels
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            is_happy = True
            break
            
    if is_happy:
        print("Happy")
    else:
        print("Sad")
        
    t -= 1