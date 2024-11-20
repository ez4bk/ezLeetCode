def apply_op(operands, op):
    right = operands.pop()
    left = operands.pop()
    if op == '+':
        operands.append(left + right)
    elif op == '-':
        operands.append(left - right)
    return operands
        
def precedence(c):
    if c in ('+', '-'):
        return 1
    return 0

def calculator(exp):
    operands = []
    ops = []
    i = 0
    while i < len(exp):
        char = exp[i]
        if char.isdigit():
            num = 0
            while i < len(exp) and exp[i].isdigit():
                num = num*10 + int(exp[i])
                i += 1
            operands.append(num)
            i -= 1
        elif char == '(':
            ops.append(char)
        elif char == ')':
            while ops and ops[-1] != '(':
                operands = apply_op(operands, ops.pop())
            ops.pop()
        elif char in ('+', '-'):
            while (ops and ops[-1] != '(' and precedence(ops[-1]) >= precedence(char)):
                operands = apply_op(operands, ops.pop())
            ops.append(char)
        i += 1
    while ops:
        operands = apply_op(operands, ops.pop())
    return operands[0]

print(calculator("(1+(4+5+2)-3)+(6+8)"))