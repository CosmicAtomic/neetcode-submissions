class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            if char not in t:
                return False
            if s.count(char) != t.count(char):
                return False
        for char in s:
            if char not in s:
                return False
            if s.count(char) != t.count(char):
                return False
        return True
        
        