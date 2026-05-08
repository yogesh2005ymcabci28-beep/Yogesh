# cook your dish here
import sys

def solve():
    # Reading all input at once is faster for large constraints
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n_str = input_data[i]
        n_list = list(n_str)  # Convert string to list to allow modification
        
        carry = 1
        idx = len(n_list) - 1
        
        # Process from right to left
        while idx >= 0 and carry > 0:
            digit = int(n_list[idx]) + carry
            if digit == 10:
                n_list[idx] = '0'
                carry = 1
            else:
                n_list[idx] = str(digit)
                carry = 0
            idx -= 1
            
        # If there is still a carry, prepend '1' (e.g., 99 + 1 = 100)
        if carry == 1:
            results.append("1" + "".join(n_list))
        else:
            results.append("".join(n_list))
            
    # Print all results separated by a newline
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()