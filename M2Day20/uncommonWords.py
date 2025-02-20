def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    first_words = s1.split()
    second_words = s2.split()
    count_dict = {}
    uniques = []
    for word in first_words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    for word in second_words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    
    for key,value in count_dict.items():
        if value <= 2:
            uniques.append(key)

        
