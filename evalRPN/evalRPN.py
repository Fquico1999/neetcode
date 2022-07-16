#!/usr/bin/env python3

"""
Difficulty: Medium
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""

def evalRPN(tokens) -> int:

    operators = ['+', '-', '/', '*']
    stack = []

    for token in tokens:
        if token in operators:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
        else:
            stack.append(int(token))
    return stack.pop()



if __name__ == "__main__":

    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])==22
    assert evalRPN(["1", "1", "*"])==1