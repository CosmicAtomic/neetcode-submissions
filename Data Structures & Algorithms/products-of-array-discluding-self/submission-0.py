class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if i != j :
                    x *= nums[j]
            output.append(x)        
        return output

        