class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else: 
                res[i] = 1 
        rank = sorted(res.items(), key=lambda item: item[1], reverse=True)[:k]
        return [key for key, value in rank]
        