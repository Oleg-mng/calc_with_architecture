import model_sub
import view
import model_sum
import model_mult
import model_div



def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_sum.init(value_a, value_b)
    model_sub.init(value_a, value_b)
    model_mult.init(value_a, value_b)
    model_div.init(value_a, value_b)
    result = view.type_of_operation()
    view.view_data(result)
