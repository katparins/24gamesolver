def left_to_right_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        return f"(({nested_list[0]} {op1} {nested_list[1]}) {op2} {nested_list[2]}) {op3} {nested_list[3]}"


def left_and_right_group_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        return f"({nested_list[0]} {op1} {nested_list[1]}) {op3} ({nested_list[2]} {op2} {nested_list[3]})"


def middle_group_left_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        return f"({nested_list[0]} {op2} ({nested_list[1]} {op1} {nested_list[2]})) {op3} {nested_list[3]}"


def middle_group_right_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        return f"{nested_list[0]} {op3} (({nested_list[1]} {op1} {nested_list[2]}) {op2} {nested_list[3]})"


def right_to_left_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        return f"{nested_list[0]} {op3} ({nested_list[1]} {op2} ({nested_list[2]} {op1} {nested_list[3]}))"