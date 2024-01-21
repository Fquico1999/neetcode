#!/usr/bin/env python3


"""
Difficulty: Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:
    """
    Solution Class
    """

    def __init__(self):
        self.stack = []     # One stack for actual values
        self.minStack = []  # One stack for the minimum at the time of appending.

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif  val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None


if __name__ == "__main__":

    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(3)
    obj.push(1)
    obj.push(5)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    param_3 = obj.top()
