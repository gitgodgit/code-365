def isIsomorphic(s: str, t: str) -> bool:
    if len(s) == len(t):
        for i in range(len(s)):
            if s.find(s[i]) != t.find(t[i]):
                return False
        return True
    else:
        return False

            
            