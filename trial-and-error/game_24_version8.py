from math import *
import random

lst = []

first_number = input("First number: ")
second_number = input("Second number: ")
third_number = input("Third number: ")
fourth_number = input("Fourth number: ")

lst.append(int(first_number))
lst.append(int(second_number))
lst.append(int(third_number))
lst.append(int(fourth_number))

random_list = []
operators = ["+", "-", "*", "/"]
random_times = 1
no_duplicates_list = []
duplicates_list = []

for number in lst:
    if number not in no_duplicates_list:
        no_duplicates_list.append(number)
    else:
        duplicates_list.append(number)

if len(no_duplicates_list) == 4:
    cases = factorial(4) # 24
elif len(no_duplicates_list) == 3:
    cases = factorial(4)//factorial(2) # 12
elif len(no_duplicates_list) == 2:
    if duplicates_list[0] == duplicates_list[1]:
        cases = factorial(4)//factorial(3) # 4
    else:
        cases = factorial(4)//(factorial(2)*factorial(2)) # 6
elif len(no_duplicates_list) == 1:
    cases = 1

while random_times <= cases:
    random.shuffle(lst)
    if lst not in random_list:
        random_list.append(lst[:])
        random_times += 1

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
    
def get_second_result_left(operator, operator2, nested_list, num1, num2, print_func):
    if operator2 == "+":
        second_result = num1 + num2
        for operator3 in operators:
            final_result = get_final_result(operator3, second_result, nested_list[3])
            print_func(final_result, nested_list, operator, operator2, operator3)
                                       
    elif operator2 == "-":
        second_result = num1 - num2
        for operator3 in operators:
            final_result = get_final_result(operator3, second_result, nested_list[3])
            print_func(final_result, nested_list, operator, operator2, operator3)

    elif operator2 == "*":
        second_result = num1 * num2
        for operator3 in operators:
            final_result = get_final_result(operator3, second_result, nested_list[3])       
            print_func(final_result, nested_list, operator, operator2, operator3)
                
    elif operator2 == "/":
        numerator = num1
        denominator = num2
        for operator3 in operators:
            final_result = final_result_division_right(operator3, numerator, denominator, nested_list[3])
            print_func(final_result, nested_list, operator, operator2, operator3)
            
def get_second_result_middle(operator, operator2, nested_list, num1, num2, print_func):
    if operator2 == "+":
        second_result = num1 + num2
        for operator3 in operators:
            final_result = get_final_result(operator3, first_result, second_result)
            print_func(final_result, nested_list, operator, operator2, operator3)
                                       
    elif operator2 == "-":
        second_result = num1 - num2
        for operator3 in operators:
            final_result = get_final_result(operator3, first_result, second_result)
            print_func(final_result, nested_list, operator, operator2, operator3)

    elif operator2 == "*":
        second_result = num1 * num2
        for operator3 in operators:
            final_result = get_final_result(operator3, first_result, second_result)       
            print_func(final_result, nested_list, operator, operator2, operator3)
                
    elif operator2 == "/":
        numerator = num1
        denominator = num2
        for operator3 in operators:
            final_result = final_result_division_right(operator3, numerator, denominator, first_result)
            print_func(final_result, nested_list, operator, operator2, operator3)

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
        
def final_result_division_left(operation, a, b, c):
    if operation == "+":
        try:
            final_result = ((c * b) + a) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "-":
        try:
            final_result = ((c * b) - a) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "*":
        try:
            final_result = (c * a) / b
        except ZeroDivisionError:
            final_result = -1
    elif operation == "/":
        try:
            final_result = (c * b) / a
        except ZeroDivisionError:
            final_result = -1
    return final_result

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

# print_func
def left_to_right_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        print(f"(({nested_list[0]} {op1} {nested_list[1]}) {op2} {nested_list[2]}) {op3} {nested_list[3]}")

def left_and_right_group_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        print(f"({nested_list[0]} {op1} {nested_list[1]}) {op3} ({nested_list[2]} {op2} {nested_list[3]})")

def middle_group_left_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        print(f"({nested_list[0]} {op2} ({nested_list[1]} {op1} {nested_list[2]})) {op3} {nested_list[3]}")
        
def middle_group_right_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        print(f"{nested_list[0]} {op3} (({nested_list[1]} {op1} {nested_list[2]}) {op2} {nested_list[3]})")
        
def right_to_left_solution(final_result, nested_list, op1, op2, op3):
    if final_result == 24.0:
        print(f"{nested_list[0]} {op3} ({nested_list[1]} {op2} ({nested_list[2]} {op1} {nested_list[3]}))")

print("\nSolution:")

# Left to right
for nested_list in random_list:
    for operator in operators:
        if operator == "+":
            first_result = nested_list[0] + nested_list[1]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, first_result, nested_list[2], left_to_right_solution)

        elif operator == "-":
            first_result = nested_list[0] - nested_list[1]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, first_result, nested_list[2], left_to_right_solution)

        elif operator == "*":
            first_result = nested_list[0] * nested_list[1]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, first_result, nested_list[2], left_to_right_solution)
    
        elif operator == "/":
            numerator = nested_list[0]
            denominator = nested_list[1]

            for operator2 in operators:
                if operator2 == "+":
                    numerator2 = numerator + (denominator * nested_list[2])

                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        left_to_right_solution(final_result, nested_list, operator, operator2, operator3)
                                                       
                elif operator2 == "-":
                    numerator2 = numerator - (denominator * nested_list[2])
                
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        left_to_right_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "*":
                    numerator2 = numerator * nested_list[2]
                    
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        left_to_right_solution(final_result, nested_list, operator, operator2, operator3)
                
                elif operator2 == "/":
                    denominator2 = denominator * nested_list[2]
                    
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator, denominator2, nested_list[3])
                        left_to_right_solution(final_result, nested_list, operator, operator2, operator3)

# Left and right grouping
for nested_list in random_list:
    for operator in operators:
        if operator == "+":
            first_result = nested_list[0] + nested_list[1]
            
            for operator2 in operators:
                get_second_result_middle(operator, operator2, nested_list, nested_list[2], nested_list[3], left_and_right_group_solution)
    
        elif operator == "-":
            first_result = nested_list[0] - nested_list[1]
            
            for operator2 in operators:
                get_second_result_middle(operator, operator2, nested_list, nested_list[2], nested_list[3], left_and_right_group_solution)

        elif operator == "*":
            first_result = nested_list[0] * nested_list[1]
            
            for operator2 in operators:
                get_second_result_middle(operator, operator2, nested_list, nested_list[2], nested_list[3], left_and_right_group_solution)

        elif operator == "/":
            numerator = nested_list[0]
            denominator = nested_list[1]

            for operator2 in operators:
                if operator2 == "+":
                    second_result = nested_list[2] + nested_list[3]

                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator, denominator, second_result)
                        left_and_right_group_solution(final_result, nested_list, operator, operator2, operator3)
                                                       
                elif operator2 == "-":
                    second_result = nested_list[2] - nested_list[3]
                
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator, denominator, second_result)
                        left_and_right_group_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "*":
                    second_result = nested_list[2] * nested_list[3]
                    
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator, denominator, second_result)
                        left_and_right_group_solution(final_result, nested_list, operator, operator2, operator3)
                            
                elif operator2 == "/":
                    numerator2 = nested_list[2]
                    denominator2 = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "+":
                            try:
                                final_result = ((numerator * denominator2) + (numerator2 * denominator)) / (denominator * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "-":
                            try:
                                final_result = ((numerator * denominator2) - (numerator2 * denominator)) / (denominator * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "*":
                            try:
                                final_result = (numerator * numerator2) / (denominator * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "/":
                            try:
                                final_result = (numerator * denominator2) / (denominator * numerator2)
                            except ZeroDivisionError:
                                final_result = -1
                        left_and_right_group_solution(final_result, nested_list, operator, operator2, operator3)
        
# Middle grouping (left first)
for nested_list in random_list:
    for operator in operators:
        if operator == "+":
            first_result = nested_list[1] + nested_list[2]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, nested_list[0], first_result, middle_group_left_solution)
             
        elif operator == "-":
            first_result = nested_list[1] - nested_list[2]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, nested_list[0], first_result, middle_group_left_solution)

        elif operator == "*":
            first_result = nested_list[1] * nested_list[2]
            
            for operator2 in operators:
                get_second_result_left(operator, operator2, nested_list, nested_list[0], first_result, middle_group_left_solution)

        elif operator == "/":
            numerator = nested_list[1]
            denominator = nested_list[2]

            for operator2 in operators:
                if operator2 == "+":
                    numerator2 = (nested_list[0] * denominator) + numerator

                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        middle_group_left_solution(final_result, nested_list, operator, operator2, operator3)
                                  
                elif operator2 == "-":
                    numerator2 = (nested_list[0] * denominator) - numerator
                
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        middle_group_left_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "*":
                    numerator2 = nested_list[0] * numerator
                    
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator, nested_list[3])
                        middle_group_left_solution(final_result, nested_list, operator, operator2, operator3)
                           
                elif operator2 == "/":
                    numerator2 = nested_list[0] * denominator
                    denominator2  = numerator
                    
                    for operator3 in operators:
                        final_result = final_result_division_right(operator3, numerator2, denominator2, nested_list[3])
                        middle_group_left_solution(final_result, nested_list, operator, operator2, operator3)

# Middle grouping (right first)
for nested_list in random_list:
    for operator in operators:
        if operator == "+":
            first_result = nested_list[1] + nested_list[2]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, first_result, nested_list[3], middle_group_right_solution)

        elif operator == "-":
            first_result = nested_list[1] - nested_list[2]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, first_result, nested_list[3], middle_group_right_solution)
                            
        elif operator == "*":
            first_result = nested_list[1] * nested_list[2]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, first_result, nested_list[3], middle_group_right_solution)

        elif operator == "/":
            numerator = nested_list[1]
            denominator = nested_list[2]

            for operator2 in operators:
                if operator2 == "+":
                    numerator2 = numerator + (nested_list[3] * denominator)

                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])
                        middle_group_right_solution(final_result, nested_list, operator, operator2, operator3)
                            
                elif operator2 == "-":
                    numerator2 = numerator - (nested_list[3] * denominator)
                
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])
                        middle_group_right_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "*":
                    numerator2 = numerator * nested_list[3]
                    
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])     
                        middle_group_right_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "/":
                    denominator2 = denominator * nested_list[3]
                    
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator, denominator2, nested_list[0])
                        middle_group_right_solution(final_result, nested_list, operator, operator2, operator3)
                    
# Right grouping (reversed)
for nested_list in random_list:
    for operator in operators:
        if operator == "+":
            first_result = nested_list[2] + nested_list[3]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, nested_list[1], first_result, right_to_left_solution)
                    
        elif operator == "-":
            first_result = nested_list[2] - nested_list[3]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, nested_list[1], first_result, right_to_left_solution)

        elif operator == "*":
            first_result = nested_list[2] * nested_list[3]
            
            for operator2 in operators:
                get_second_result_right(operator, operator2, nested_list, nested_list[1], first_result, right_to_left_solution)

        elif operator == "/":
            numerator = nested_list[2]
            denominator = nested_list[3]

            for operator2 in operators:
                if operator2 == "+":
                    numerator2 = (nested_list[1] * denominator) + numerator

                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])
                        right_to_left_solution(final_result, nested_list, operator, operator2, operator3)
                                                       
                elif operator2 == "-":
                    numerator2 = (nested_list[1] * denominator) - numerator
                
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])
                        right_to_left_solution(final_result, nested_list, operator, operator2, operator3)

                elif operator2 == "*":
                    numerator2 = nested_list[1] * numerator
                    
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator, nested_list[0])
                        right_to_left_solution(final_result, nested_list, operator, operator2, operator3)
                            
                elif operator2 == "/":
                    numerator2 = nested_list[1] * denominator
                    denominator2 = numerator
                    
                    for operator3 in operators:
                        final_result = final_result_division_left(operator3, numerator2, denominator2, nested_list[0])
                        right_to_left_solution(final_result, nested_list, operator, operator2, operator3)