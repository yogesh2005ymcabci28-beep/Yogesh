# Read X (Alice's marks) and Y (Bob's marks)
x, y = map(int, input().split())

# Alice is happy if she scored at least twice Bob's marks
if x >= 2 * y:
    print("Yes")
else:
    print("No")
