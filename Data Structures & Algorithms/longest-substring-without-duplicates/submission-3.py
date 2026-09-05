class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        str_len = len(s)
        res = 0
        store = set()
        while r < str_len:
            if s[r] in store:
                res = max(res, r - l)
                while s[l] != s[r]:
                    store.remove(s[l])                    
                    l +=1
                l += 1
            else:
                store.add(s[r])
            r +=1  
        res = max(res, r - l)  
        return res           


        