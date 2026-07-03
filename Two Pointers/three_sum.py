def three_sum(array: list[int]) -> list[list[int]]:
    """
    Function that will return all three elements in an array that will be equal to zero
    input
    arr: list[int]
    return list[list[int]]
    """
    # PSEUDOCDOE
    # 1. SORT THE ARRAY
    # 2. FOR EACH ELEMENT K IN ARRAY FIND TWO OTHER NUMBER THAT'S SUM = -K
    # 3. RETURN TRIPLETS
    array.sort()
    triplets = []
    length = len(array)
    for i in range(length):
        if array[i] > 0:
            break
        if i != 0 and array[i - 1] == array[i]:
            continue
        required_sum = -1 * array[i]
        pairs = sorted_pairs_sum(array, i + 1, length - 1, required_sum)
        print(pairs)
        for pair in pairs:
            triplets.append([array[i]] + pair)
    return triplets


def sorted_pairs_sum(
    array: list[int], left: int, right: int, required_sum: int
) -> list[list[int]]:
    pairs = set()
    while left < right:
        addition = array[left] + array[right]
        if addition > required_sum:
            right -= 1
        elif addition < required_sum:
            left += 1
        else:
            pairs.add((array[left], array[right]))
            left += 1
    return list([list(x) for x in pairs])


test_cases = [0, -1, 2, -3, 1]

print(three_sum(array=test_cases))
