def is_even(number):
    """Checks if a number is even"""
    if number is number % 2 == 0:
        return True
    else:
        return False
    
is_even(5)