class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}
        check = {}
        n = len(s2)
        for c in s1:
            s1count[c] = 1 + s1count.get(c, 0)
        for l in range(len(s2)):
            if s2[l] in s1count:
                for r in range(l, l +len(s1)):
                    if r >= len(s2):
                        return False
                    check[s2[r]] = 1 + check.get(s2[r], 0)
                if check == s1count:
                    return True
                check.clear()
        return False



            
            

        