#user defined functions 
PI = 3.14

#area of rectangle 
def rectangle(a=2, b=3):
    return a*b

#area of the square
def square(a=3):
    return a**2

#area of triangle 
def triangle(b=4, h=5):
    return ((b*h)/2)


#area of a circle
def circle(a=5):
    return PI*(a**2)


#execution
rectangle_area = rectangle(a=2, b=3)
square_area = square()
triangle_area = triangle(b=4, h=5)
circle_area = circle(a=5)

print("rectangle", rectangle_area)
print("square" , square_area)
print("triangle" , triangle_area)
print("circle" , circle_area)


print("name: shreyansh singh \nprn no.: 26013010907")