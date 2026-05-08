def isAnagram(s, t):
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Initialize a frequency array for 26 lowercase English letters
    count = [0] * 26

    # Increment counts for string s
    for ch in s:
        count[ord(ch) - ord('a')] += 1

    # Decrement counts for string t
    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    # If all counts are zero, it is an anagram
    for c in count:
        if c != 0:
            return False

    return True

# Driver code to handle input and output
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        s = input_data[0]
        t = input_data[1]
        if isAnagram(s, t):
            print("YES")
        else:
            print("NO")
