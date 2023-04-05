import math
import calendar

print(math.sqrt(16))
print("hello")

print(math.pow(2,2))


cal = calendar.month(1984, 1)
print(cal)  

def calculate_triangle_area(base, height):
    return 1/2*(base*height)

triangle_1 = calculate_triangle_area(4, 5)
print(triangle_1)

def calculate_square_area(length):
    print("__name__:", __name__)
    return length*length

square_area = calculate_square_area(7)
print(square_area)

 ### __name__ == "__main__"

if __name__ == "__main__":
    print("I am in modules.py")
    a = calculate_square_area(20)
    print("area: ", a)