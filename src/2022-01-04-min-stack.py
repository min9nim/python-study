# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
      self.stack = []
        

    def push(self, val: int) -> None:
      self.stack.append(val)
        

    def pop(self) -> None:
        last = self.stack[-1]
        del self.stack[-1]
        return last

    def top(self) -> int:
      return self.stack[-1]
        

    def getMin(self) -> int:
      return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


s = MinStack()

s.push(1)
s.push(2)
s.push(5)

print(s.stack)

assert s.getMin() == 1
assert s.push(9) == None