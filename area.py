def heronsformula(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

side1 = float(input("enter the first side of the triangle  "))
side2 = float(input("enter the second side of the triangle "))
side3 = float(input("enter the third side of the triangle  "))

area = heronsformula(side1,side2,side3)

print("area of the triangle using heron's formula is = " + str(area))