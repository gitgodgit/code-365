def findWord(words: list[str]) -> list[str]:
    keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    output = []
    for word in words:
        token_of_truth = True
        row_to_check = 0
        if word[0].lower() in keyboard_rows[0]:
            row_to_check = 0
        elif word[0].lower() in keyboard_rows[1]:
            row_to_check = 1
        else:
            row_to_check = 2

        for letter in word:
            letter = letter.lower()
            if letter not in keyboard_rows[row_to_check]:
                token_of_truth = False
        
        if token_of_truth:
            output.append(word)
    return output
