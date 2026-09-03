class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.keyStore[key]
        l, r = 0, len(arr) -1
        while l <= r:
            mid = l + (r-l)//2
            mid_stamp = arr[mid][-1]
            if timestamp >= mid_stamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid -1
        return res


        
