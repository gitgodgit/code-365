def reverseOnlyLetters(s: str) -> str:
    reversed_string = ""
    j = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[-j-1].isalpha():
                reversed_string += s[-j-1]
                j+= 1
            else:
                while not s[-j-1].isalpha():
                    j += 1
                reversed_string += s[-j-1]
                j+= 1
        else:
            reversed_string += s[i]
    return reversed_string
