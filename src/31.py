import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

circle_radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(circle_radius)
print(f"The area of the circle with radius {circle_radius} is {area}")
