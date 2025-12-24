def is_palindrome(s: str) -> bool:
    """
    Determine if the given string is a palindrome, considering only alphabetic characters and ignoring case.
    Non-alphabetic characters (spaces, punctuation) are ignored.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    l, r = 0, len(s) - 1  # Initialize left and right pointers
    while l < r:
        # Skip non-alphabetic characters
        if not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        else:
            # Compare the characters ignoring case
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True

def run_tests():
    """
    Run a set of test cases to validate the `is_palindrome` function.
    """
    tests = [
      ("Bob wondered, 'Now, Bob?'", True),
      ("", True),
      ("a", True),
      ("A man, a plan, a canal: Panama", True),
      ("race a car", False),
      ("Was it a car or a cat I saw?", True),
      ("hello", False),
      (".,?!'", True),
  ]
    
    for i, (s, expected) in enumerate(tests, 1):
        assert is_palindrome(s) == expected
        print(f"Test {i} passed.")

    print("All tests passed.")

# Example usage
if __name__ == "__main__":
    run_tests()