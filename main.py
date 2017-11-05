# 3.Дан файл с каким-то математическим выражением,
# которое содержит скобки разных типов “{[()]}” в любом порядке.
# Проверить сбалансированны ли скобки.
# В случае сбалансированности вывести результат вычисления выражения,
# иначе вывести сообщение об ошибке.

import bracket as b

path = 'test.txt'

try:
    with open(path) as file:
        expression = file.read()
        brackets = b.get_sequence_brackets(expression)
        if brackets:
            if b.is_balanced(brackets):
                solution = b.solution_expression(expression)
                print(solution)
            else:
                print('Сбалансированность скобок нарушена!')
        else:
            print('Выражение не содержит скобок!')
            solution = b.solution_expression(expression)
            print(solution)
except IOError as e:
    print(e.strerror)