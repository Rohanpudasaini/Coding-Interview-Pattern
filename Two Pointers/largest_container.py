def largest_container_bruteforce(array: list[int]) -> int:
    max_area = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            area = min(array[i], array[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area


# The time complexity of this code is O(N^2) and space complexity is O(1)


def largest_container(array: list[int]) -> int:
    left, right = 0, (len(array) - 1)
    max_area = 0
    while left < right:
        area = min(array[left], array[right]) * (right - left)
        max_area = max(max_area, area)
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_area


test_case = [2, 7, 8, 3, 7, 6]
test_cases = [
    [2, 7, 8, 3, 7, 6],
    [],
    [1],
    [1, 1],
    [0, 1, 0],
    [3, 3, 3, 3],
    [1, 2, 3],
    [3, 2, 1],
    [5, 2, 4, 3, 1, 5],
]
# print(largest_container_bruteforce(test_case))
# print(largest_container(test_case))
for case in test_cases:
    print(f"{case=}: {largest_container(case)}")
