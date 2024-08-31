# PYTHON EXERCISES

Task 1: Add Numbers
Purpose: Adds two numbers.

Explanation: 

The add_numbers function takes two parameters, num1 and num2.
It returns the sum of num1 and num2.

Task 2: Is Even
Purpose: Checks if a number is even.

Explanation:

The is_even function takes a single parameter, number.
It uses the modulo operator (%) to check if the remainder of number divided by 2 is 0.
If the remainder is 0, the number is even and the function returns True. Otherwise, it returns False.

Task 3: Reverse String
Purpose: Reverses a string.

Explanation:

The reverse_string function takes a string text as input.
It uses slicing notation [::-1] to reverse the string.
The : indicates the beginning of the slice, the second : indicates the end of the slice, and -1 indicates the step size, which is -1 for reversing.

Task 4: Count Vowels
Purpose: Counts the number of vowels in a string.

Explanation:

The count_vowels function takes a string text as input.
It defines a string vowels containing all vowels (both lowercase and uppercase).
It initializes a count variable to 0.
It iterates over each character in the string.
If the character is a vowel, it increments the count.
Finally, it returns the count.

Task 5: Calculate Factorial
Purpose: Calculates the factorial of a number.

Explanation:

The calculate_factorial function takes a non-negative integer n as input.
It uses recursion to calculate the factorial.
If n is 0, it returns 1 (base case).
Otherwise, it returns n multiplied by the factorial of n - 1.

Task 6: Apply Decorator
Purpose: Applies a decorator to a function.

Explanation:

The decorator_func function takes a function func as input.
It defines an inner function wrapper that prints a message and calls the original function func.
It returns the wrapper function.
The apply_decorator function takes a function func as input and returns the result of applying the decorator_func to it.

Task 7: Sort by Age
Purpose: Sorts a list of tuples by age in descending order.

Explanation:

The sort_by_age function takes a list of tuples as input.
It uses the sorted() function to create a new sorted list.
The key= x:key_function x[1] argument specifies that the sorting should be based on the second element of each tuple (the age).
This indicates that the sorting should be done in ascending order.

Task 8: Merge Dictionaries
Purpose: Merges two dictionaries.

Explanation:

The merge_dicts function takes two dictionaries as input.
It creates a new dictionary merged_dict by unpacking both dict1 and dict2. This automatically merges the dictionaries.
It then iterates over dict2 to add any values for keys that were present in dict2 but not in dict1. This ensures that values from dict2 override values from dict1 for common keys.
Finally, it returns the merged dictionary.

Task 9: Class Creation
Purpose: Defines a Car class with attributes and a method.

Explanation:

The Car class represents a car object.
The __init__ method is the constructor, which initializes the attributes of the car object.
The display_info method prints the car's information.

ACCESSING AND RUNNING THE CODE FROM GITHUB
1. Clone the Repository:
GitHub Link: [Replace this with the actual GitHub link to your repository]
Open a terminal or command prompt.
Navigate to the directory where you want to clone the repository.

Use the following command:
git clone [GitHub Repository Link]

This will create a local copy of the repository on your machine.

2. Navigate to the Directory:
Use the cd command to change directories to the newly created repository:

cd [Repository Name]


3. Run the Python Script:
You can run it using:

python main.py



Machine Requirements
The code should run on any machine with:

Python: Ensure you have Python installed (version 3.6 or later is recommended). You can download it from https://www.python.org/.


AUTHOR : COLLINS WACHIRA