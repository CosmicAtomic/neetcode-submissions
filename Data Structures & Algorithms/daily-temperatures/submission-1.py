class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for t in temperatures]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                to_be_pop = stack.pop()
                res[to_be_pop[1]] = i - to_be_pop[1]
            stack.append([temp, i])
        return res
        
        