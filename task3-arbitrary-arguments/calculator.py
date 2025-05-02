def add(*args):
    """
    Adds all the numbers passed as arguments.

    Args:
        *args: Arbitrary positional arguments representing numbers to be added.

    Returns:
        float: The sum of the numbers.
    
    Raises:
        ValueError: If any of the arguments is not a number.
    """
    if not args:
        raise ValueError("At least one number is required.")
    
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        total += num
    return total


def subtract(*args):
    """
    Subtracts all the numbers passed as arguments from the first one.

    Args:
        *args: Arbitrary positional arguments, with at least two numbers.

    Returns:
        float: The result of the subtraction.

    Raises:
        ValueError: If any of the arguments is not a number or there are not enough arguments.
    """
    if len(args) < 2:
        raise ValueError("At least two numbers are required for subtraction.")
    
    result = args[0]
    for num in args[1:]:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        result -= num
    return result


def multiply(*args):
    """
    Multiplies all the numbers passed as arguments.

    Args:
        *args: Arbitrary positional arguments representing numbers to be multiplied.

    Returns:
        float: The product of the numbers.
    
    Raises:
        ValueError: If any of the arguments is not a number.
    """
    if not args:
        raise ValueError("At least one number is required.")
    
    product = 1
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        product *= num
    return product


def divide(*args):
    """
    Divides the first number by the rest of the numbers sequentially.

    Args:
        *args: Arbitrary positional arguments, with at least two numbers.

    Returns:
        float: The result of the division.
    
    Raises:
        ValueError: If there are not enough numbers or if a division by zero is attempted.
    """
    if len(args) < 2:
        raise ValueError("At least two numbers are required for division.")
    
    result = args[0]
    for num in args[1:]:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        if num == 0:
            raise ValueError("Division by zero is not allowed.")
        result /= num
    return result


def calculate(operation, *args, **kwargs):
    if operation == 'add':
        return add(*args)
    elif operation == 'subtract':
        return subtract(*args)
    elif operation == 'multiply':
        return multiply(*args)
    elif operation == 'divide':
        return divide(*args)
    else:
        raise ValueError(f"Invalid operation: {operation}. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")


if __name__ == "__main__":
    try:
       
        print(f"Add: {calculate('add', 1, 2, 3, 4)}") 
        print(f"Subtract: {calculate('subtract', 10, 5, 2)}") 
        print(f"Multiply: {calculate('multiply', 2, 3, 4)}")  
        print(f"Divide: {calculate('divide', 20, 5, 2)}")  

        print(f"Invalid Operation: {calculate('modulus', 10, 5)}")  

    except ValueError as e:
        print(f"Error: {e}")
