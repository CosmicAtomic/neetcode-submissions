class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:#
        nums = set(nums)
        res  = 0
        for num in nums:
            res = max(res, 1)
            number = num
            while number + 1 in nums:
                number += 1
                res = max(res, number - num + 1)
            
        return res

        
                
