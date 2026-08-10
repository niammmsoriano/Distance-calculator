import math  
# Import math to access square root functions
# Get the coordinates for the first point (x1, y1) from the user
x1 = float(input("Please put x1: "))
y1 = float(input("Please put y1: "))
# Get the coordinates for the second point (x2, y2) from the user
x2 = float(input("Please put x2: "))
y2 = float(input("Please put y2: "))
# Calculate using the formula of: d = square root of (x2-x1)^2 + (y2-y1)^2
d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# Display the final calculation
print(f"The distance between the two points is {d:.2f}")