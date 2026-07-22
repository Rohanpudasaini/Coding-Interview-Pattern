def is_happy(num:int)->bool:
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = square_sum(num)
    return num == 1

# Time complexity of this code is O(1) for n < 243 else it's O(log(n))
# Space complexity is O(int(log(n))+1) as we are using space for a set

def square_sum(num:int):
    sum_square = 0
    while num:
        digit = num %10
        num = num //10
        sum_square += digit **2
    return sum_square

if __name__ == '__main__':
    print(is_happy(2))
        

    