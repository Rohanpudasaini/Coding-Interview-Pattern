def triplet_sum(array: list[int]) -> list[list[int]]:
    length = len(array)
    triplets = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if array[i] + array[j] + array[k] == 0:
                    triplets.add(tuple(sorted([array[i], array[j], array[k]])))
    return [list(triplet) for triplet in triplets]


def test(cases: list[list[int]]):
    for case in cases:
        results = triplet_sum(case)
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
]

test(cases)
