def nextGreatestLetter(letters: list[str], target: str) -> str:
    for letter in letters:
        if int(letter - target) > 0:
            return letter
    return letter[0]