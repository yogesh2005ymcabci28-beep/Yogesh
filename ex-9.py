a=float(input("Enter maths mark:"))
b=float(input("Enter physics mark:"))
c=float(input("Enter chemistry mark:"))
d=float(input("Enter computer mark:"))
total=a+b+c+d
avg=total/4
print("Total mark:",total)
print("Average mark:",avg)
if (avg>75):
    print("Distinction")
elif (75>avg and avg>=60):
    print("First division")
elif (60>avg and avg>=50):
    print("Second division")
elif (50>avg and avg>=40):
    print("Third division")
else:
    print("Fail")
