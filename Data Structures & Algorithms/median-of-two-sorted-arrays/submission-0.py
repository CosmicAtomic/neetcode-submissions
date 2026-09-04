class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combination = nums1 + nums2
        combination.sort()
        n = len(combination) 
        midpoint = (n-1)  //2
        if n % 2== 0:
            return (combination[midpoint] + combination[midpoint + 1])/2
        return combination[midpoint]


        