# 3.Дан файл с каким-то математическим выражением,
# которое содержит скобки разных типов “{[()]}” в любом порядке.
# Проверить сбалансированны ли скобки.
# В случае сбалансированности вывести результат вычисления выражения,
# иначе вывести сообщение об ошибке.




def isBalanced(brackets):
    stack = []
    balanced = True
    for index, bracket in enumerate(brackets):
        if bracket in '{[(':
            stack.append(bracket)
        else:
            if not stack:
                balanced = False
            else:
                openBracket = stack.pop()
                if not isMatches(openBracket, bracket):
                    balanced = False
        if not balanced:
            break

    if balanced and not stack:
        return True
    else:
        return False

def isMatches (openBracket, closeBracket):
    openBrackets = '{[('
    closeBrackets = '}])'
    return openBrackets.index(openBracket) == closeBrackets.index(closeBracket)

print(isBalanced('(()(){}[])'))