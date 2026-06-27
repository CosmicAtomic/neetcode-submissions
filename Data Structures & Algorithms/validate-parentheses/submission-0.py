class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "{" :  "}",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                topElement = stack.pop()
                if mapping[topElement] == c:
                    continue
                else:
                    return False
        
        return len(stack) == 0