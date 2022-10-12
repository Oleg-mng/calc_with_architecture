import model_sum
import model_sub
import model_div
import model_mult


def view_data(data):
    print(f'result= {data}')


def get_value():
    return int(input('value='))


def type_of_operation():
    global result
    op = input('введите тип операции (+,-,*,/)   ')
    if op == '+':
        result = model_sum.sum()
    elif op == '-':
        result = model_sub.sub()
    elif op == '*':
        result = model_mult.mult()
    elif op == '/':
        result = model_div.div()
    return result
