class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

def run_tests():
    tests = [
        # Example 1 from book
        ([-2, 0, 3, 4, 7, 9, 11], 3, 2),
        # Example 2 from book
        ([-2, 0, 3, 4, 7, 9, 11], 2, -1),
        # Edge case - empty array
        ([], 5, -1),
        # Edge case - target at start
        ([1, 2, 3], 1, 0),
        # Edge case - target at end
        ([1, 2, 3], 3, 2),
        # Edge case - single element
        ([5], 5, 0),
        # Edge case - not found
        ([1, 3, 5], 2, -1)
  ]

    s = Solution()
    for arr, target, want in tests:
        got = s.binary_search(arr, target)
        assert got == want, f"binary_search({arr}, {target}): got {got}, want {want}"
        
if __name__ == "__main__":
    run_tests()
    print("All tests passed!")