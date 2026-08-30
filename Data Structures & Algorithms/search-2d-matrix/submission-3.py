class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lo, hi = 0, len(matrix)-1
        while lo <= hi:
            mid = lo + ((hi - lo)// 2)
            if matrix[mid][0] < target :
                if matrix[mid][-1] >= target:
                    break
                lo = mid + 1
            elif matrix[mid][0]> target: 
                hi = mid - 1
            else:
                return True
        low, high = 0, len(matrix[mid])-1
        while low<= high:
            middle = low +(high - low)// 2
            if matrix[mid][middle] < target:
                low = middle + 1
            elif matrix[mid][middle] > target:
                high = middle-1
            else:
                return True
        return False
            


        
        