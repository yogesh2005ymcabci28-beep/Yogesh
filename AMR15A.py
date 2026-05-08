# cook your dish here
# Read the number of soldiers
N = int(input())

# Read the number of weapons for each soldier as a list
weapons = list(map(int, input().split()))

lucky_count = 0
unlucky_count = 0

# Iterate through each soldier's weapon count
for a in weapons:
    if a % 2 == 0:
        lucky_count += 1
    else:
        unlucky_count += 1

# Check if the army is ready for battle
if lucky_count > unlucky_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
