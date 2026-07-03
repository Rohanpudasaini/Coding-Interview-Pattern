def valid_palindrom_bruteforce(text: str) -> bool:
    """
    Only aplicable if we care all the part of the text is palindrom
    and we don't have to ommit alpha numeric character
    """
    return text == text[::-1]


def valid_palindrom_without_slice(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# case = "a"
# case = ""
# case = " I . ' (?)"
case = "12.02.2021"
print(valid_palindrom_without_slice(case))
