class PlusOne:
    def plus_one(self, digits: list[int]) -> list[int]:
        pointer = len(digits) - 1
        counter = 0
        while(digits[pointer - counter] == 9 and counter <= pointer):
            digits[pointer - counter] = 0
            counter += 1
        if counter > pointer:
            return [1] + digits
        else:
            digits[pointer - counter] += 1
            return digits