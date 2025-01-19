def isHappy(n: int) -> bool:
    string_n = str(n)
    squares_sum = 0
    for number in string_n:
        squared = int(number) * int(number)
        squares_sum += squared
    if squares_sum == 1 or squares_sum == 7:
        return True
    elif squares_sum < 10:
        return False
    else:
        return isHappy(squares_sum)
    