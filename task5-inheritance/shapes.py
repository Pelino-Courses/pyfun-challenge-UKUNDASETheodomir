import math

class Shape:
    """
    Base class for geometric shapes.

    Attributes:
        name (str): Name of the shape.
    """

    def __init__(self, name: str):
        """
        Initialize a Shape with a name.

        Args:
            name (str): The name of the shape.
        """
        self.name = name

    def area(self) -> float:
        """
        Calculates the area of the shape.
        This should be overridden by derived classes.

        Returns:
            float: Area of the shape.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self) -> str:
        return f"A shape named {self.name}"


class Circle(Shape):
    """
    Represents a circle.

    Attributes:
        radius (float): Radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle with a given radius.

        Raises:
            ValueError: If radius is negative.
        """
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"{self.name} with radius {self.radius}"


class Rectangle(Shape):
    """
    Represents a rectangle.

    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle with width and height.

        Raises:
            ValueError: If width or height is negative.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height

    def __str__(self) -> str:
        return f"{self.name} ({self.width} x {self.height})"


class Triangle(Shape):
    """
    Represents a triangle.

    Attributes:
        base (float): Base length of the triangle.
        height (float): Height of the triangle.
    """

    def __init__(self, base: float, height: float):
        """
        Initialize a Triangle with base and height.

        Raises:
            ValueError: If base or height is negative.
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self) -> float:
        """Return the area of the triangle."""
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"{self.name} (base={self.base}, height={self.height})"
