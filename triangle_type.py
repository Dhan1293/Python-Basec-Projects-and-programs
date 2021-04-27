def traingle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


x = float(input("Enter sides of traingle:\nx - "))
y = float(input("y - "))
z = float(input("z - "))

print(traingle(x, y, z))
