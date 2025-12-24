def merge(arr1, arr2):
    p1, p2 = 0, 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    while p1 < len(arr1):
        result.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        result.append(arr2[p2])
        p2 += 1
    return result

def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 3, 4, 5], [2, 4, 4], [1, 2, 3, 4, 4, 4, 5]),
      # Example 2 from the book
      ([-1], [], [-1]),
      # Additional test cases
      ([], [], []),
      ([1], [], [1]),
      ([], [1], [1]),
      ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
      ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
  ]
  for arr1, arr2, want in tests:
    got = merge(arr1, arr2)
    assert got == want, f"\nmerge({arr1}, {arr2}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()
    print("All tests passed.")