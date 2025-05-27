# to take a coordinate as input along with an angle theta and perform rotation about that angle
import math
def coord():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    angle = float(input("Enter angle: "))
    angle = math.radians(angle)
    x_rotated = x * math.cos(angle) - y * math.sin(angle)
    y_rotated = x * math.sin(angle) + y * math.cos(angle)
    return (x_rotated, y_rotated)

def main():
    print(coord())
    
main()