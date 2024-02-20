def word_machine(operations):
    stack = []
    for op in operations.split():
        if op.isdigit():
            stack.append(int(op))
        elif op == "POP":
            if stack:
                stack.pop()
            else:
                return "ERROR: Pop operation on empty stack"
        elif op == "DUP":
            if stack:
                stack.append(stack[-1])
            else:
                return "ERROR: Dup operation on empty stack"
        elif op == "+":
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                result = a + b
                if result >= 2**20:
                    return "ERROR: Overflow"
                else:
                    stack.append(result)
            else:
                return "ERROR: Addition operation on insufficient elements in stack"
        elif op == "-":
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                result = a - b
                if result < 0:
                    return "ERROR: Underflow"
                else:
                    stack.append(result)
            else:
                return "ERROR: Subtraction operation on insufficient elements in stack"
    if not stack:
        return "ERROR: Empty stack"
    return stack[-1]

# Example usage:
operations = "5 6 + -"
print(word_machine(operations))  # Output should be 6
