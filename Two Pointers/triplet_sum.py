from collections.abc import Callable


def triplet_sum_bruteforce(array: list[int]) -> list[list[int]]:
    length = len(array)
    triplets = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if array[i] + array[j] + array[k] == 0:
                    triplets.add(tuple(sorted([array[i], array[j], array[k]])))
    return [list(triplet) for triplet in triplets]


def triplet_sum_optimized(array: list[int]) -> list[int] | None:
    # Sort the array
    array.sort()
    result = None
    print(f"{array=}")
    length = len(array)
    # find pivot and alsolist to find the sorted sum of -pivot
    for i in range(length):
        print(f"{i=}, {array[i]=}, {array[i + 1 :]}")
        result = sorted_sum_of_pair(array=array, start=i + 1, sum=(-array[i]))
        if result:
            result.append(array[i])
            return result
    return result


def sorted_sum_of_pair(array: list[int], start: int, sum: int) -> list[int] | None:
    left, right = start, len(array) - 1
    while left < right:
        if array[left] + array[right] > sum:
            right -= 1
        elif array[left] + array[right] < sum:
            left += 1
        else:
            return [array[left], array[right]]
    return None


print(triplet_sum_optimized(array=[-2, -1, -1, 1, 2, 2]))


def test(function: Callable[[list[int]], list[list[int]]], cases: list[list[int]]):
    for case in cases:
        results = function(case)
        print(f"{case=}")
        print(f"{results=}")
        print([sum(result) for result in results])


cases = [
    [-2, -1, -1, 1, 2, 2],
    [],
    [0],
    [1, -1, 0],
    [1, -2, 1],
    [1, -1],
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 1, -1, -1, -1],
    [0, 0, 0, 2, 0, -2, 3, -2, -1],
]

# test(function=triplet_sum_bruteforce, cases=cases)
