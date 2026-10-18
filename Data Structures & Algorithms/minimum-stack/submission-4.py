class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        # Your logic: Update global min, then store as a pair
        if self.min is None or val < self.min:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()
        # FIX: Update self.min to reflect the new top's recorded minimum
        if not self.stack:
            self.min = None
        else:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min # Or return self.stack[-1][1]