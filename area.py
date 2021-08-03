"""
# heron's formula using function
def heronsformula(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

side1 = float(input("enter the first side of the triangle  "))
side2 = float(input("enter the second side of the triangle "))
side3 = float(input("enter the third side of the triangle  "))

area = heronsformula(side1,side2,side3)

print("area of the triangle using heron's formula is = " + str(area))

"""
#area of circle
radius = float(input("enter the radius of the circle : "))
area = 3.14*radius*radius
circumference = 2*3.14*radius
print("AREA = "+str(area))
print("CIRCUMFERENCE = "+str(circumference))