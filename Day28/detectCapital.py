def detectCapitalUse(word: str) -> bool:
    start_capital = word[0].isupper()
    last_capital = word[len(word) - 1].isupper()

    if start_capital and last_capital:
        for i in range(1, len(word) - 1):
            if word[i].islower():
                return False
    elif start_capital:
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
    else:
        for i in range(len(word)):
            if word[i].isupper():
                return False
    
    return True
        
