def count_vowels(text):
    """Counts vowels in a string"""
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count