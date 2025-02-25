def isPalindrome(x:int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + (x % 10)
            x //= 10
        return x == reversed_number or x == reversed_number // 10
