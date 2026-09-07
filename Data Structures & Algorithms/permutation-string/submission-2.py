class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = len(s1), len(s2)
        if s1Count> s2Count :
            return False
        s1Freq = {}
        for c in s1:
            s1Freq[c] = 1 + s1Freq.get(c, 0)
        check = {}
        for r in range(s1Count):
            check[s2[r]] = 1 + check.get(s2[r], 0)
        if check == s1Freq:
            return True
        l = 0
        for r in range(s1Count, s2Count):
            check[s2[l]] -= 1
            if check[s2[l]] ==0:
                del check[s2[l]]
            l += 1
            check[s2[r]] = 1 + check.get(s2[r], 0)
            if check == s1Freq:
                return True
        return False


            




        
