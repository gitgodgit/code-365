def findRepeatedDnaSequences(s: str) -> list[str]:
    repeated_strings = []
    substring_checker = {}

    for i in range((len(s) - 9)):
        substring = s[i:i+10]
        if substring in substring_checker:
            substring_checker[substring] += 1
        else:
            substring_checker[substring] = 1

    for substring, count in substring_checker:
        if count > 1:
            repeated_strings.append(substring)
        
    return repeated_strings