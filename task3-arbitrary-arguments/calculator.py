def add(*args):
    if not args:
        raise ValueError("At least one number is required.")
    
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        total += num
    return total


def subtract(*args):
    if len(args) < 2:
        raise ValueError("Enter atleast two numbers for subtraction.")
    
    result = args[0]
    for num in args[1:]:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        result -= num
    return result


def multiply(*args):
    if not args:
        raise ValueError("Atleast one number is required.")
    
    product = 1
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid argument: {num} is not a number.")
        product *= num
    return product


def divide(*args):
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
    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)
    else:
        raise ValueError(f"Invalid operation: {operation}. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")


if __name__ == "__main__":
    try:
       
        print(f"Add: {calculate('+', 1, 2, 3, 4)}") 
        print(f"Subtract: {calculate('-', 10, 5, 2)}") 
        print(f"Multiply: {calculate('*', 2, 3, 4)}")  
        print(f"Divide: {calculate('/', 20, 5, 2)}")  

        print(f"Invalid Operation: {calculate('%', 10, 5)}")  

    except ValueError as e:
        print(f"Error: {e}")
