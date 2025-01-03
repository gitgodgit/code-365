def calculate(s) -> int:
    number_pairs = {
        'I': 1,
        'V' : 5,
        'X' : 10, 
        'L' : 50, 
        'C' : 100, 
        'D' : 500, 
        'M' : 1000
    }

    answer = 0
    for i in range(len(s)):
        if i + 1 < len(s) and number_pairs[s[i + 1]] > number_pairs[s[i]]:
            answer -= number_pairs[s[i]]
        else:
            answer += number_pairs[s[i]]
    
    return answer
print(calculate("MCMXCIV"))

