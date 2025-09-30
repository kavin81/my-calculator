"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with validation and logging."""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(f"Multiplying {a} by {b}...")
        result = a * b
        print(f"Result of multiplication: {result}")
        return result
    else:
        raise TypeError("Both inputs must be numbers.")

def divide(a, b):
    """Perform division with input validation and error handling."""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b != 0:
            print(f"Performing division: {a} divided by {b}")
            result = a / b
            print(f"Result: {result}")
            return result
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise TypeError("Both arguments must be numbers.")

def power(base, exponent):
    """Raise base to the power of exponent with validation."""
    if isinstance(base, (int, float)) and isinstance(exponent, (int, float)):
        print(f"Calculating {base} raised to the power of {exponent}...")
        result = base ** exponent
        print(f"Result: {result}")
        return result
    else:
        raise TypeError("Both base and exponent must be numbers.")

def sqrt(value):
    """Calculate the square root of a number with validation."""
    if isinstance(value, (int, float)):
        if value >= 0:
            print(f"Calculating the square root of {value}...")
            result = value ** 0.5
            print(f"Result: {result}")
            return result
        else:
            raise ValueError("Cannot compute the square root of a negative number.")
    else:
        raise TypeError("Input must be a number.")

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")