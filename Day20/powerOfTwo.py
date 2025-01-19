def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0 or n % 2 == 1:
        return False
    else:
        return isPowerOfTwo(n / 2)