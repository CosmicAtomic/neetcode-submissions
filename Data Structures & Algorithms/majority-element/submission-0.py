class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = len(nums)/2
        major = nums[0]
        for num in set(nums):
            if nums.count(num) > check:
                major = num
        return major


        