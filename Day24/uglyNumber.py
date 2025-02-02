def isUgly(number:int)-> bool:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for number in [2, 3, 5]:
            while n % number == 0:
                n == n // number
        return n == 1