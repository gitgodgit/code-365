def isPalindrome(s: str) -> bool:
    lower_string = s.lower()
    half_length = len(s) // 2
    full_length = len(s)
    index = 0
    left_spaces = 0
    right_spaces = 0
    if full_length > 0:
        while (index <= half_length and index + left_spaces < full_length and right_spaces < full_length) :
            if not lower_string[index + left_spaces].isalpha() and not lower_string[index + left_spaces].isdigit():
                left_spaces += 1
                continue
            if not lower_string[full_length - 1 - index - right_spaces].isalpha() and not lower_string[full_length - 1 - index - right_spaces].isdigit():
                right_spaces += 1
                continue
            if lower_string[left_spaces + index] != lower_string[full_length - 1 - right_spaces - index]:
                return False
            index += 1
        return True
    else:
        return False
    
