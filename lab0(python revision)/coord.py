def distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2))

def main():
    x1 = float(input("Enter x1: \n"))
    y1 = float(input("Enter y1: \n"))
    x2 = float(input("Enter x2: \n"))
    y2 = float(input("Enter y2: \n"))

    print(f"Distance is: {distance(x1, y1, x2, y2)}")

main()