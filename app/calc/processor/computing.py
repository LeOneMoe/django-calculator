
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
    except ZeroDivisionError:
    	is_ok = False
    	answer = 'Деление на ноль недопустимо'
    except TypeError as e:
    	is_ok = False
    	answer = str(e)


    return is_ok, answer
