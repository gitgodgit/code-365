def sqrt(x:int) -> int:
    if x < 2:
        return x
    
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer

print(sqrt(121))