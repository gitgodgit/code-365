class addBinary:
    def addBinary(self, a: str, b: str) -> str:
        remainder = 0
        length_a = len(a)
        length_b = len(b)
        output = ""
        if length_a > length_b:
            for i in range(length_a - length_b):
                b = '0' + b
        else:
            for i in range(length_b - length_a):
                a = '0' + a

        for i in range(length_a - 1, -1, -1):
            output = str((int(a[i]) + int(b[i]) + remainder) % 2) + output
            if (int(a[i]) + int(b[i]) + remainder) > 1:
                remainder = 1
            else:
                remainder = 0
        if remainder == 1:
            output = '1' + output
        return output
        