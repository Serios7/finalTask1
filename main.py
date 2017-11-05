# 3.Дан файл с каким-то математическим выражением,
# которое содержит скобки разных типов “{[()]}” в любом порядке.
# Проверить сбалансированны ли скобки.
# В случае сбалансированности вывести результат вычисления выражения,
# иначе вывести сообщение об ошибке.

import re


def is_balanced(brackets):
    stack = []
    balanced = True
    for index, bracket in enumerate(brackets):
        if bracket in '{[(':
            stack.append(bracket)
        else:
            if not stack:
                balanced = False
            else:
                open_bracket = stack.pop()
                if not is_matches(open_bracket, bracket):
                    balanced = False
        if not balanced:
            break

    if balanced and not stack:
        return True
    else:
        return False


def is_matches(open_bracket, close_bracket):
    open_brackets = '{[('
    close_brackets = '}])'
    return open_brackets.index(open_bracket) == close_brackets.index(close_bracket)


def count_words(text):
    result = re.findall(r"[{[(}\])]", text)
    return result


def qwe(string):
    brackets = ''

    return brackets


string = '{2+[2+3][]{*(2+9)+1}'

print(is_balanced(count_words(string)))
