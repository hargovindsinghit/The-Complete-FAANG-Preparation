"""
Given two sorted arrays arr1 and arr2, find their intersection.
The intersection should include all elements that appear in both arrays, including duplicates.
The result should be returned in sorted order.

Example 1:
Input: 
arr1 = [1, 2, 3]
arr2 = [1, 3, 5]
Output: [1, 3]
Explanation: 1 and 3 appear in both arrays.

Example 2:
Input:
arr1 = [1, 1, 1]
arr2 = [1, 1]
Output: [1, 1]
Explanation: Two 1s appear in both arrays.

Example 3:
Input:
arr1 = [1, 2, 2, 3]
arr2 = [2, 2, 3]
Output: [2, 2, 3]
Explanation: Two 2s and one 3 appear in both arrays.

Constraints:
    * The input arrays are sorted in ascending order
    * 0 ≤ arr1.length, arr2.length ≤ 10^5
    * -10^9 ≤ arr1[i], arr2[i] ≤ 10^9
"""

from typing import List

def common_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Finds the intersection of two sorted arrays.
    
    Args:
        arr1 (List[int]): The first sorted array.
        arr2 (List[int]): The second sorted array.
    
    Returns:
        List[int]: The intersection of the two arrays.
    
    Complexity Analysis:
        Time Complexity: O(m + n), where m and n are the lengths of the two arrays.
        Space Complexity: O(1) (excluding the result list).
    """
    p1, p2 = 0, 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1
    return result

def run_tests():
    """
    Runs test cases to validate the `common_elements` function.
    """
    tests = [
        # Provided examples
        ([1, 2, 3], [1, 3, 5], [1, 3]),
        ([1, 1, 1], [1, 1], [1, 1]),
        
        # Additional edge cases
        ([], [], []),                       # Both arrays empty
        ([1], [], []),                      # One array empty
        ([], [1], []),                      # One array empty
        ([1], [1], [1]),                    # Single matching element
        ([1, 2, 3], [4, 5, 6], []),         # No intersection
        ([1, 2, 2, 3], [2, 2, 3], [2, 2, 3]) # Multiple duplicates
    ]

    for i, (arr1, arr2, expected) in enumerate(tests, 1):
        result = common_elements(arr1, arr2)
        assert result == expected, (
            f"Test case {i} failed:\n"
            f"Input: arr1 = {arr1}, arr2 = {arr2}\n"
            f"Expected: {expected}, Got: {result}\n"
        )
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
