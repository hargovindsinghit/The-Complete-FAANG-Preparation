from typing import List

def two_sum(nums: List[int]) -> bool:
    """
    Description: Given an sorted array of integers, return true if there are two numbers in the array that add up to 0.
    Args:
        nums: sorted List[int]
    Returns: bool
    """
    
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > 0:
            right -= 1
        elif nums[left] + nums[right] < 0:
            left += 1
        else:
            return True
    return False

def run_tests():
  tests = [
      # Example 1 from the book
      ([-5, -2, -1, 1, 1, 10], True),
      # Example 2 from the book
      ([-3, 0, 0, 1, 2], True),
      # Example 3 from the book
      ([-5, -3, -1, 0, 2, 4, 6], False),
      # Additional test cases
      ([], False),
      ([0], False),
      ([-1, 1], True),
      ([-2, -1, 0, 1], True),
      ([1, 2, 3, 4], False),
  ]
  for arr, want in tests:
    got = two_sum(arr)
    assert got == want, f"\ntwo_sum({arr}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()
    print("All tests passed.")