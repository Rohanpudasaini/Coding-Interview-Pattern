Case = tuple[list[int], int]


def pair_in_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]
    return []


def test(cases: list[Case]):
    for case in cases:
        nums = case[0]
        target = case[1]
        result = pair_in_sorted(nums, target)
        print(f"{nums=}, f{target=}")
        print(result, end="\n")


cases = [
    ([], 0),
    ([1], 1),
    ([2, 3], 5),
    ([2, 4], 5),
    ([2, 2, 3], 5),
    ([-1, 2, 3], 2),
    ([-3, -2, -1], -5),
]

test(cases)
