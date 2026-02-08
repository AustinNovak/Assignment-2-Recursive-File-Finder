"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    
    Args:
        numbers (list): List of numbers to sum
    
    Returns:
        int: Sum of all numbers in the list
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int: Count of even numbers in the list
    """
    if len(numbers) == 0:
        return 0
    
    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    else:
        return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    
    Args:
        strings (list): List of strings to search
        target (str): Substring to search for
    
    Returns:
        list: All strings that contain the target substring
    """
    if len(strings) == 0:
        return []
    
    rest = find_strings_with(strings[1:], target)

    if target in strings[0]:
        return [strings[0]] + rest
    else:
        return rest


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    
    Args:
        directory_path (str): Path to the directory to analyze
    
    Returns:
        int: Total number of files in the directory tree
    """
    # Base case: if it's a file, count it as 1
    if os.path.isfile(directory_path):
        return 1

    total = 0

    # Recursive case: directory, loop through everything inside
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            total += 1
        elif os.path.isdir(full_path):
            total += count_files(full_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    
    Args:
        directory_path (str): Path to the directory to analyze
        extension (str): File extension to search for
    
    Returns:
        list: List of full paths to all files with the specified extension
    """
    # Base case: if it is a file, check if it matches extension
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    infected_files = []

    # Recursive case: if it is a directory, search inside
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            if full_path.endswith(extension):
                infected_files.append(full_path)

        elif os.path.isdir(full_path):
            infected_files.extend(find_infected_files(full_path, extension))

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - COMPLETED CODE\n")

    # PART 1 TESTS

    print("Testing sum_list:")
    print("  sum_list([1, 2, 3, 4]) =", sum_list([1, 2, 3, 4]), "(expected: 10)")
    print("  sum_list([]) =", sum_list([]), "(expected: 0)")
    print("  sum_list([5, 5, 5]) =", sum_list([5, 5, 5]), "(expected: 15)\n")

    print("Testing count_even:")
    print("  count_even([1, 2, 3, 4, 5, 6]) =", count_even([1, 2, 3, 4, 5, 6]), "(expected: 3)")
    print("  count_even([1, 3, 5]) =", count_even([1, 3, 5]), "(expected: 0)")
    print("  count_even([2, 4, 6]) =", count_even([2, 4, 6]), "(expected: 3)\n")

    print("Testing find_strings_with:")
    result = find_strings_with(["hello", "world", "help", "test"], "hel")
    print("  find_strings_with(['hello','world','help','test'], 'hel') =", result, "(expected: ['hello','help'])")

    result = find_strings_with(["cat", "dog", "bird"], "z")
    print("  find_strings_with(['cat','dog','bird'], 'z') =", result, "(expected: [])\n")


    # PART 2 TESTS

    print("Testing count_files on test cases:")
    print("  Total files (Test Case 1):", count_files("test_cases/case1_flat"), "(expected: 5)")
    print("  Total files (Test Case 2):", count_files("test_cases/case2_nested"), "(expected: 4)")
    print("  Total files (Test Case 3):", count_files("test_cases/case3_infected"), "(expected: 5)\n")


    # PART 3 TESTS

    print("Testing find_infected_files on test cases:")
    print("  Total infected (Test Case 1):", len(find_infected_files("test_cases/case1_flat")), "(expected: 0)")
    print("  Total infected (Test Case 2):", len(find_infected_files("test_cases/case2_nested")), "(expected: 0)")
    print("  Total infected (Test Case 3):", len(find_infected_files("test_cases/case3_infected")), "(expected: 3)\n")


    # BREACH DATA RESULTS

    print("Scanning breach_data folder...\n")

    print("Total files (breach_data):", count_files("breach_data"))
    print("Total infected files (breach_data):", len(find_infected_files("breach_data")))

    print("\nInfected files by department:")
    print("  Finance infected:", len(find_infected_files("breach_data/Finance")))
    print("  HR infected:", len(find_infected_files("breach_data/HR")))
    print("  Sales infected:", len(find_infected_files("breach_data/Sales")))
