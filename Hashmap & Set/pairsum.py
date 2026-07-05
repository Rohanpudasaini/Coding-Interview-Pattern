def pairsum_bruteforce(array: list[int], sum: int) -> list[int]:
    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            if array[i] + array[j] == sum:
                return [i, j]
    return []


# Time complexity is O(n^2), space complexity is O(1)


def pairsum(array: list[int], sum: int) -> list[int]:
    hash_set = {}
    for i in range(len(array)):
        if hash_set.get(array[i]) is not None:
            return [hash_set[array[i]], i]
        hash_set[sum - array[i]] = i
    return []


# Time complexity is O(N) and space complexity is also O(N)

test_case = [-1, 3, 4, 2]
sum = 3
# print(pairsum_bruteforce(test_case, sum))
print(pairsum(test_case, sum))
