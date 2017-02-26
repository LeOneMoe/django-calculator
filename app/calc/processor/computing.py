
def brackets_balance(expression):
    pass


def compute(expression):

    is_ok = True
    answer = None

    try:
        answer = eval(expression)
    except SyntaxError:
        is_ok = False
        answer = 'Ошибка синтаксиса'

    return is_ok, answer
