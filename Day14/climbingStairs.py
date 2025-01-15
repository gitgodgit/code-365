def climbStairs(n: int) -> int:
    before_last_member = 1
    last_member = 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(2 , n):
            temp = before_last_member + last_member
            before_last_member = last_member
            last_member = temp
    return last_member

    
    