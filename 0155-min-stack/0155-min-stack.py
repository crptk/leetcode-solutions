class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


'''
This solution uses a min stack and a stack to control
the getMin function in O(1) time. Essentially, one stack
is for the minimum, if it's less than the current minimum, then
append it to the min stack. If not, then keep appending the current
minimum (last val of minstack) onto the min stack so when
we pop it, it won't mess with the order of the minstack.
'''