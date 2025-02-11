class Solution:
    def isLongPressedName(name: str, typed: str) -> bool:
        count_in_first = 0
        count_in_second = 0
        index_on_name = 0
        second_pointer = 0
        i = 0

        while i < len(name):
            current_letter = name[i]
            for j in range(i, len(name)):
                if name[j] == current_letter:
                    count_in_first +=1
                else:
                    break
            for k in range(second_pointer, len(typed)):
                if typed[k] == current_letter:
                    count_in_second += 1
                else:
                    break
            second_pointer += count_in_second
            if count_in_first <= count_in_second:
                i += count_in_first
                count_in_first = 0
                count_in_second = 0
            else:
                return False
        if second_pointer <= len(typed) - 1 :
            return False
        else:
            return True