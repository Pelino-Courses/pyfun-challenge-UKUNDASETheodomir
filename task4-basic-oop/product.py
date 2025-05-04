class Product:
    """
    A class representing a product in the inventory.

    Attributes:
        name (str): Name of the product.
        price (float): Price per unit of the product.
        quantity (int): Available quantity of the product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance with validated values.

        Raises:
            ValueError: If price or quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity

    def add_inventory(self, amount: int):
        """
        Adds inventory to the product.

        Args:
            amount (int): Number of units to add.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Cannot add negative inventory.")
        self._quantity += amount

    def remove_inventory(self, amount: int):
        """
        Removes inventory from the product.

        Args:
            amount (int): Number of units to remove.

        Raises:
            ValueError: If amount is negative or exceeds current inventory.
        """
        if amount < 0:
            raise ValueError("Cannot remove negative inventory.")
        if amount > self._quantity:
            raise ValueError("Not enough inventory to remove.")
        self._quantity -= amount

    def total_value(self) -> float:
        """
        Calculates the total value of the product in inventory.

        Returns:
            float: Total value (price * quantity).
        """
        return self._price * self._quantity

    def display_info(self) -> str:
        """
        Returns a formatted string of product information.

        Returns:
            str: Product name, price, quantity, and total value.
        """
        return (
            f"Product: {self._name}\n"
            f"Price: ${self._price:.2f}\n"
            f"Quantity: {self._quantity}\n"
            f"Total Value: ${self.total_value():.2f}"
        )

    # Properties to expose read-only access to private attributes
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
