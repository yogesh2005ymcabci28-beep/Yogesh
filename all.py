from collections import Counter

def sort_by_frequency(s: str) -> str:
    # 1. Count frequency of each character
    freq = Counter(s)
    
    # 2. Sort by frequency descending (-x[1]), 
    # then by character ASCII value ascending (x[0])
    # freq.items() gives pairs like ('o', 3)
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # 3. Build the result string by repeating each character by its frequency
    result = ''.join(char * count for char, count in sorted_chars)
    
    return result

# Read input from the user
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    if input_data:
        print(sort_by_frequency(input_data))
