
def isPalindrome(x:int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True
    elif x >= 10:
        x = f"{x}"
        for i in range(len(x)//2):
            if x[i] == x[len(x) - i - 1]:
                continue
            else:
                return False
        return True
    
print(isPalindrome(-12121))

