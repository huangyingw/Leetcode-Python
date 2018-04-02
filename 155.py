class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min = min(x, self.min)
        self.stack.append((x, self.min))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
        self.min = self.stack[-1][1] if self.stack else float('inf')
        return

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()