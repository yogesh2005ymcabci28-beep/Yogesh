t = int(input())

while t > 0:
    n = int(input())
    s = input()
    
    res = ""
    # Iterate from 0 to n-1 with a step of 2
    for i in range(0, n, 2):
        pair = s[i:i+2] # Get the current pair of characters
        
        if pair == "00":
            res += "A"
        elif pair == "01":
            res += "T"
        elif pair == "10":
            res += "C"
        elif pair == "11":
            res += "G"
            
    print(res)
    t -= 1
