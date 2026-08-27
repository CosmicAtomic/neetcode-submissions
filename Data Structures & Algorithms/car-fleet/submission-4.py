class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(reverse = True)
        stack = []
        for car in cars:
            car_position, car_speed = car
            stack.append((target - car_position)/ car_speed)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



        
        