operators = ["+", "-", "*", "/"]

def get_final_result(operation, num1, num2) :
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return -1

def get_second_result_right(operator, operator2, nested_list, num1, num2, print_func):
    if operator2 == "+":
        second_result = num1 + num2
        for operator3 in operators:
            final_result = get_final_result(operator3, nested_list[0], second_result)
            print_func(final_result, nested_list, operator, operator2, operator3)

    elif operator2 == "-":
        second_result = num1 - num2
        for operator3 in operators:
            final_result = get_final_result(operator3, nested_list[0], second_result)
            print_func(final_result, nested_list, operator, operator2, operator3)

    elif operator2 == "*":
        second_result = num1 * num2
        for operator3 in operators:
            final_result = get_final_result(operator3, nested_list[0], second_result)
            print_func(final_result, nested_list, operator, operator2, operator3)

    elif operator2 == "/":
        numerator = num1
        denominator = num2
        for operator3 in operators:
            final_result = final_result_division_right(operator3, numerator, denominator, nested_list[0])
            print_func(final_result, nested_list, operator, operator2, operator3)

def final_result_division_right(operation, a, b, c):
    if operation == "+":
        try:
            final_result = (a + (b * c)) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "-":
        try:
            final_result = (a - (b * c)) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "*":
        try:
            final_result = (a * c) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "/":
        try:
            final_result = a / (b * c)
        except ZeroDivisionError:
            final_result = -1
    return final_result