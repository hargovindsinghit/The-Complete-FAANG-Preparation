from typing import List

def smaller_prefixes(arr: List[int]) -> bool:
    """
    Determines if the sum of the first k elements is smaller than the sum of the next 2k elements 
    for every k in the range 1 ≤ k ≤ n/2, where n is the length of the array.

    Args:
        arr (List[int]): A list of integers with even length.
    
    Returns:
        bool: 
            - True if the condition holds for all valid k.
            - False if any prefix sum is not smaller than the sum of the next two elements.
    
    Approach:
        - A two-pointer technique is used to optimize the solution from O(n^2) to O(n).
        - A slow pointer (`sp`) tracks the prefix sum, while a fast pointer (`fp`) evaluates 
          the sum of the next two consecutive elements.
    
    Time Complexity:
        O(n), where n is the length of the array, due to single-pass traversal.
    
    Space Complexity:
        O(1), as only a few additional variables are used.
    """
    sp, fp = 0, 0  # Initialize slow and fast pointers
    slow_sum, fast_sum = 0, 0  # Initialize prefix sums

    # Traverse the array until the fast pointer reaches the second last element
    while fp < len(arr) - 1:
        slow_sum += arr[sp]
        fast_sum += arr[fp] + arr[fp + 1]

        if slow_sum >= fast_sum:
            return False  # Condition failed for some k

        sp += 1  # Move slow pointer by 1
        fp += 2  # Move fast pointer by 2

    return True  # Condition holds for all k


def run_tests():
    """
    Runs a set of test cases to validate the `smaller_prefixes` function.
    """
    test_cases = [
        # Provided examples
        ([1, 2, 2, -1], True),
        ([1, 2, -2, 1, 3, 5], False),
        
        # Additional test cases
        ([2, 1, -1, 4, -2, 0], True),  # Example from the book's diagram
        ([1, 2], True),  # Minimal even-length array
        ([1, 1, 1, 1, 1, 1], True),  # All elements equal
        ([], True),  # Empty array, trivially satisfies the condition

    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = smaller_prefixes(arr)
        assert result == expected, (
            f"Test case {i} failed:\n"
            f"Input: {arr}\n"
            f"Expected: {expected}, Got: {result}\n"
        )

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
