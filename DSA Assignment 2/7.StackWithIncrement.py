#https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/1341011376/

class CustomStack:
    def __init__(self, maxSize):
        self.stack = [0] * maxSize
        self.maxSize = maxSize
        self.top = -1

    def push(self, x):
        if self.top < self.maxSize - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.stack[self.top + 1]
        else:
            return -1

    def increment(self, k, val):
        for i in range(min(k, self.top + 1)):
            self.stack[i] += val