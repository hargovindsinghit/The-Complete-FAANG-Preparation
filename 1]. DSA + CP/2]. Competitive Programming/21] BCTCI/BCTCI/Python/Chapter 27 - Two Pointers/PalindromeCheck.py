"""
Module: palindrome_checker

This module provides a function to check if a given string is a palindrome.
A palindrome is a string that reads the same forward and backward.

Example Usage:
--------------
    >>> is_palindrome("level")
    True
    >>> is_palindrome("hello")
    False
"""

def is_palindrome(s: str) -> bool:
    """
    Determines whether the provided string is a palindrome.

    Args:
        s (str): The input string consisting of lowercase English letters.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Constraints:
        - The length of s is at most 10^5.
        - s consists of lowercase English letters.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def run_tests() -> None:
    """
    Runs a series of test cases to validate the is_palindrome function.
    """
    test_cases = [
        # Provided examples
        ("level", True),
        ("naan", True),
        ("hello", False),
        
        # Additional edge cases
        ("", True),             # Empty string
        ("a", True),            # Single character
        ("ab", False),          # Two different characters
        ("abba", True),         # Even-length palindrome
        ("abcba", True),        # Odd-length palindrome
        ("abc", False),         # Non-palindrome
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        assert result == expected, (
            f"Test case {i} failed:\n"
            f"Input: {input_str}\n"
            f"Expected: {expected}, Got: {result}\n"
        )
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
