def to_postfix(array: list):
    queue = []
    stack = []
    values = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, "^": 4, "cos": 4, "sin": 5, "tg": 4, "ctg": 4, "ln": 4, "exp": 4}
    for symbol in array:
        try:
            queue.append(float(symbol))
        except:
            try:
                if symbol == "(":
                    stack.append(symbol)
                elif symbol == ")":
                    i = len(stack) - 1
                    while stack[i] != "(":
                        queue.append(stack[i])
                        stack.pop(i)
                        i -= 1
                    stack.pop(i)
                elif len(stack) == 0 or values[stack[len(stack) - 1]] < values[symbol]:
                    stack.append(symbol)
                else:
                    i = len(stack) - 1
                    while len(stack) != 0 and values[stack[i]] >= values[symbol]:
                        queue.append(stack[i])
                        stack.pop(i)
                        i -= 1
                    stack.append(symbol)
            except:
                return []

    for i in range(len(stack) - 1, -1, -1):
        queue.append(stack[i])

    return queue
