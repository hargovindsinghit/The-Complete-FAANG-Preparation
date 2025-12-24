def reverse_case_match(s):
    """
    Given a string s containing both uppercase and lowercase letters, determine if the
    lowercase letters match the uppercase letters in reverse order.
    In other words, check if the sequence of lowercase letters matches the sequence of uppercase letters when read backwards.

    """
    l, r = 0, len(s) - 1
    while l < len(s) and r >= 0:
        if not s[l].islower():
            l += 1
        elif not s[r].isupper():
            r -= 1
        else:
            if s[l] != s[r].lower():
                return False
            l += 1
            r -= 1
    return True

def run_tests():
    tests = [
        # Example 1 from the book
        ("haDrRAHd", True),
        # Example 2 from the book
        ("harHrARDd", False),
        # Additional test cases
        ("", True),
        ("aA", True),
        ("Aa", True),
        ("BbbB", True),
        ("abAB", False),
        ("abBA", True),
        ("helloworldHELLOWORLD", False),
    ]
  
    for i, (s, expected) in enumerate(tests, 1):
        assert reverse_case_match(s) == expected
        print(f"Test {i} passed.")

    print("All tests passed.")

#   for s, want in tests:
    
#     got = reverse_case_match(s)
#     assert got == want, f"\nreverse_case_match({s}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()

    