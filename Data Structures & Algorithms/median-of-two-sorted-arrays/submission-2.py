class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = b = 0
        median1 = median2 = 0
        len1, len2 = len(nums1), len(nums2)
        count = 0
        while count < (len1 + len2)//2 + 1:
            median2= median1
            if a < len1 and b < len2:
                if nums1[a] > nums2[b]:
                    median1 = nums2[b]
                    b += 1
                else: 
                    median1 = nums1[a]
                    a += 1
            elif a < len1:
                median1 = nums1[a]
                a += 1
            elif b < len2:
                median1 = nums2[b]
                b += 1
            count +=1 
        if (len1 +len2) % 2 == 0:
            return (median1 + median2)/2
        return median1




        

        