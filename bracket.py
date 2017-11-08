import re

BRACKETS = {'{': '}', '[': ']', '(': ')'}


def is_balanced(sequence_brackets):
    stack = []
    balanced = True
    for index, bracket in enumerate(sequence_brackets):
        if bracket in BRACKETS.keys():
            stack.append(bracket)
        else:
            if not stack:
                balanced = False
            else:
                open_bracket = stack.pop()
                if bracket != BRACKETS.get(open_bracket):
                    balanced = False
        if not balanced:
            break

    if balanced and not stack:
        return True
    else:
        return False


def get_sequence_brackets(expression):
    return re.findall(r"[{[(}\])]", expression)


def solution_expression(expression):
    expression = re.sub(r"[{[]", '(', expression)
    expression = re.sub(r"[}\]]", ')', expression)
    try:
        return eval(expression)
    except Exception as e:
        return e.args[0]
