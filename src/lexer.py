import string


def is_valid(instance: str):
    gap_counter = 0
    S = State(False)
    I = State(True)
    R = State(True)
    B = State(True)
    F = State(False)
    X = State(True)

    current_state = S
    array_instance = []
    symbols = list(instance)
    component = ""
    for symbol in symbols:
        if current_state == S:
            if symbol in list("0123456789"):
                current_state = I
                component += symbol
            elif symbol == "(":
                gap_counter += 1
                array_instance.append(symbol)
            elif symbol == "-":
                array_instance.append("u")
            elif symbol in string.ascii_lowercase and symbol != "x":
                current_state = F
                component += symbol
            elif symbol == "x":
                current_state = X
                array_instance.append(symbol)
            else:
                return []
        elif current_state == I:
            if symbol in list("0123456789"):
                component += symbol
            elif symbol == ".":
                current_state = R
                component += symbol
            elif symbol == ")":
                gap_counter -= 1
                current_state = B
                array_instance.append(component)
                component = ""
                array_instance.append(symbol)
            elif symbol in list("+-*/^"):
                current_state = S
                array_instance.append(component)
                component = ""
                array_instance.append(symbol)
            else:
                return []
        elif current_state == R:
            if symbol in list("0123456789"):
                component += symbol
            elif symbol in list("+-*/^"):
                current_state = S
                array_instance.append(component)
                component = ""
                array_instance.append(symbol)
            elif symbol == ")":
                gap_counter -= 1
                current_state = B
                array_instance.append(component)
                component = ""
                array_instance.append(symbol)
            else:
                return []
        elif current_state == B:
            if symbol == ")":
                gap_counter -= 1
                array_instance.append(symbol)
            elif symbol in list("+-*/^"):
                current_state = S
                array_instance.append(symbol)
            else:
                return []
        elif current_state == F:
            if symbol in string.ascii_lowercase and symbol != "x":
                component += symbol
            elif symbol == "(":
                gap_counter += 1
                current_state = S
                array_instance.append(component)
                component = ""
                array_instance.append(symbol)
            else:
                return []
        elif current_state == X:
            if symbol in list("+-*/^"):
                current_state = S
                array_instance.append(symbol)
            elif symbol == ")":
                current_state = B
                gap_counter -= 1
                array_instance.append(")")
            else:
                return []
        else:
            return []
    if gap_counter == 0 and current_state.stopable:
        if len(component) != 0:
            array_instance.append(component)
        return array_instance
    else:
        return []


class State:
    stopable: bool

    def __init__(self, stopable: bool):
        self.stopable = stopable
