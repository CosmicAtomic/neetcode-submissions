import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            k = lo + (hi - lo)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            if totalTime <= h:
                res = k
                hi = k - 1
            else:
                lo = k + 1
        return res



                





        
        