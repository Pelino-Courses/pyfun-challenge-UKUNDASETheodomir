from shapes import Circle, Rectangle, Triangle

def main():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 8)
    ]

    for shape in shapes:
        print(f"{shape} has an area of {shape.area():.2f}")

if __name__ == "__main__":
    main()
