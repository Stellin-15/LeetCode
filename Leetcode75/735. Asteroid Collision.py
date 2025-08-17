class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for num in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and num < 0:
                if stack[-1] < -num:
                    stack.pop()
                    continue
                elif stack[-1] == -num:
                    stack.pop()
                    alive = False
                else:
                     alive = False
            if alive:
                 stack.append(num)      
        return stack

