class LastWordLength:
    def last_word_length(self, sentance: str) -> int:
        for word in sentance.split():
            length = len(str(word))
        return length