class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.min) == 0:
            self.min.append(val)
        else:
            idx = len(self.min) - 1
            insert = False
            while idx >= 0:
                if self.min[idx] > val:
                    insert = True
                    self.min.insert(idx + 1, val)
                    break
                idx -= 1
            if insert is False:
                self.min.insert(0, val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        self.min.remove(val)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
