class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l< r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        def binary_search(lo, hi):
            while lo <= hi:
                m = lo + (hi - lo)//2
                if nums[m] > target:
                    hi = m -1
                elif nums[m] < target:
                    lo = m + 1
                else:
                    return m
            return -1
        first_search = binary_search(0, pivot -1)
        if first_search != -1:
            return first_search
        return binary_search(pivot, len(nums)- 1)
        