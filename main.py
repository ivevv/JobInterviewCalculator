from collections import namedtuple
import re

op_info = namedtuple('Operator', 'priority')
ops_order = {'*': op_info(1), '/': op_info(1), '+': op_info(2), '-': op_info(2)}


def execute_op(op, first, second):
    if op == '+':
        return first + second
    elif op == '-':
        return second - first
    elif op == '*':
        return first * second
    elif op == '/':
        return second / first


class Expression:
    def __init__(self):
        self.inp = None
        self.rpn = []
        self.result = []

    def get_input(self):
        self.inp = re.split(r"(\D+)", input("Input your expression:"))
        for i in self.inp:
            if i.isdigit() or i in ops_order.keys():
                continue
            else:
                print("Invalid input! Use only decimals and basic math operations w/o parentheses.")
                self.get_input()
                break

    def get_rpn(self):
        op_stack = []
        for i in self.inp:
            if i.isdigit():
                self.rpn.append(i)
            elif i in ops_order.keys():
                while len(op_stack) > 0 and ops_order[op_stack[-1]].priority <= ops_order[i].priority:
                    self.rpn.append(op_stack.pop())
                op_stack.append(i)
        while len(op_stack) > 0:
            self.rpn.append(op_stack.pop())

    def get_result(self):
        for i in self.rpn:
            if i.isdigit():
                self.result.append(int(i))
            elif i in ops_order.keys():
                first = self.result.pop()
                second = self.result.pop()
                if first == 0 and i == '/':
                    print("Invalid input! Can't perform division by zero.")
                    break
                else:
                    self.result.append(execute_op(i, first, second))
        if self.result:
            print(self.result.pop())


if __name__ == "__main__":
    while True:
        expr = Expression()
        expr.get_input()
        expr.get_rpn()
        expr.get_result()
        opt = input("Continue? y/n")
        if opt == "n":
            break
