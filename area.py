def area_circle1(radius):
    radius = float(input("enter the radius of the circle : "))
    area = 3.14*radius*radius
    circumference = 2*3.14*radius
    print("AREA = "+str(round(area,2)))
    print("CIRCUMFERENCE = "+str(round(circumference,3)))

area_circle1(1)
