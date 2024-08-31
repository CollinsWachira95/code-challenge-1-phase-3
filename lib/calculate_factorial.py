def calculate_factorial(n):
    """Calculates the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)