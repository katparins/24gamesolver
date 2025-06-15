from math import *
import random
import copy

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
operators = ["plus", "minus", "multiply", "divide"]
random_times = 0
target_random_times = 0
no_duplicates_list = []
duplicates_list = []
cases = 0

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

while random_times < cases:
    random.shuffle(lst)
    if lst not in random_list:
        random_list.append(copy.copy(lst))
        random_times += 1

print("\nSolution:")

# Left to right
for nested_list in random_list:
    for operator in operators:

        if operator == "plus":
            first_result = nested_list[0] + nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[2]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                                                   
                elif operator2 == "minus":
                    second_result = first_result - nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")

                elif operator2 == "multiply":
                    second_result = first_result * nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator = first_result
                    denominator = nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
          
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                    
        elif operator == "minus":
            first_result = nested_list[0] - nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[2]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                                                       
                elif operator2 == "minus":
                    second_result = first_result - nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
     
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                        
                elif operator2 == "multiply":
                    second_result = first_result * nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator = first_result
                    denominator = nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")

        elif operator == "multiply":
            first_result = nested_list[0] * nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[2]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                                               
                elif operator2 == "minus":
                    second_result = first_result - nested_list[2]
                        
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                        
                elif operator2 == "multiply":
                    second_result = first_result * nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                        
                elif operator2 == "divide":
                    numerator = first_result
                    denominator = nested_list[2]

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")

        elif operator == "divide":
            numerator1 = nested_list[0]
            denominator = nested_list[1]

            for operator2 in operators:
                if operator2 == "plus":
                    numerator2 = numerator1 + (denominator * nested_list[2])

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                                                       
                elif operator2 == "minus":
                    numerator2 = numerator1 - (denominator * nested_list[2])
                
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")

                elif operator2 == "multiply":
                    numerator2 = numerator1 * nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (denominator * nested_list[3])) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (numerator2 * 1) / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")
                
                elif operator2 == "divide":
                    denominator2 = denominator * nested_list[2]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator1 + (denominator2 * nested_list[3])) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator1 - (denominator2 * nested_list[3])) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator1 * nested_list[3]) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator1 / (denominator2 * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"((({nested_list[0]} {operator} {nested_list[1]}) {operator2} {nested_list[2]}) {operator3} {nested_list[3]})")

# Left and right grouping
for nested_list in random_list:
    for operator in operators:

        if operator == "plus":
            first_result = nested_list[0] + nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[2] + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                                                   
                elif operator2 == "minus":
                    second_result = nested_list[2] - nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")

                elif operator2 == "multiply":
                    second_result = nested_list[2] * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator = nested_list[2]
                    denominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((first_result * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((first_result * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (first_result * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (first_result * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                    
        elif operator == "minus":
            first_result = nested_list[0] - nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[2] + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                                                       
                elif operator2 == "minus":
                    second_result = nested_list[2] - nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                        
                elif operator2 == "multiply":
                    second_result = nested_list[2] * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"

                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator = nested_list[2]
                    denominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((first_result * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((first_result * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (first_result * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (first_result * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")

        elif operator == "multiply":
            first_result = nested_list[0] * nested_list[1]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[2] + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                                               
                elif operator2 == "minus":
                    second_result = nested_list[2] - nested_list[3]
                        
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                        
                elif operator2 == "multiply":
                    second_result = nested_list[2] * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = first_result + second_result
                        elif operator3 == "minus":
                            final_result = first_result - second_result
                        elif operator3 == "multiply":
                            final_result = first_result * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = first_result / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                        
                elif operator2 == "divide":
                    numerator = nested_list[2]
                    denominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((first_result * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((first_result * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (first_result * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (first_result * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")

        elif operator == "divide":
            numerator1 = nested_list[0]
            denominator1 = nested_list[1]

            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[2] + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator1 + (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator1 - (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator1 * second_result) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator1 / (denominator1 * second_result)
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                                                       
                elif operator2 == "minus":
                    second_result = nested_list[2] - nested_list[3]
                
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator1 + (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator1 - (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator1 * second_result) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator1 / (denominator1 * second_result)
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")

                elif operator2 == "multiply":
                    second_result = nested_list[2] * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator1 + (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator1 - (second_result * denominator1)) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator1 * second_result) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator1 / (denominator1 * second_result)
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator2 = nested_list[2]
                    denominator2 = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((numerator1 * denominator2) + (numerator2 * denominator1)) / (denominator1 * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((numerator1 * denominator2) - (numerator2 * denominator1)) / (denominator1 * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator1 * numerator2) / (denominator1 * denominator2)
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (numerator1 * denominator2) / (denominator1 * numerator2)
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator} {nested_list[1]}) {operator3} ({nested_list[2]} {operator2} {nested_list[3]})")
        
# Middle grouping (left first)
for nested_list in random_list:
    for operator in operators:

        if operator == "plus":
            first_result = nested_list[1] + nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[0] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
        
                elif operator2 == "minus":
                    second_result = nested_list[0] - first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

                elif operator2 == "multiply":
                    second_result = nested_list[0] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                      
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                  
                elif operator2 == "divide":
                    numerator = nested_list[0]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                  
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                
        elif operator == "minus":
            first_result = nested_list[1] - nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[0] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                 
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                                         
                elif operator2 == "minus":
                    second_result = nested_list[0] - first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

                elif operator2 == "multiply":
                    second_result = nested_list[0] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                 
                elif operator2 == "divide":
                    numerator = nested_list[0]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

        elif operator == "multiply":
            first_result = nested_list[1] * nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[0] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
               
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                         
                elif operator2 == "minus":
                    second_result = nested_list[0] - first_result
                        
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                 
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                        
                elif operator2 == "multiply":
                    second_result = nested_list[0] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = second_result + nested_list[3]
                        elif operator3 == "minus":
                            final_result = second_result - nested_list[3]
                        elif operator3 == "multiply":
                            final_result = second_result * nested_list[3]
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = second_result / nested_list[3]
                            except ZeroDivisionError:
                                final_result = -1
                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                        
                elif operator2 == "divide":
                    numerator = nested_list[0]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

        elif operator == "divide":
            numerator1 = nested_list[1]
            denominator = nested_list[2]

            for operator2 in operators:
                if operator2 == "plus":
                    numerator2 = (nested_list[0] * denominator) + numerator1

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
               
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                                  
                elif operator2 == "minus":
                    numerator2 = (nested_list[0] * denominator) - numerator1
                
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
         
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

                elif operator2 == "multiply":
                    numerator2 = nested_list[0] * numerator1
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (nested_list[3] * denominator)) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")
                           
                elif operator2 == "divide":
                    numerator2 = nested_list[0] * denominator
                    denominator2  = numerator1
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = (numerator2 + (nested_list[3] * denominator2)) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = (numerator2 - (nested_list[3] * denominator2)) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (numerator2 * nested_list[3]) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = numerator2 / (denominator2 * nested_list[3])
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
            
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"({nested_list[0]} {operator2} ({nested_list[1]} {operator} {nested_list[2]})) {operator3} {nested_list[3]}")

# Middle grouping (right first)
for nested_list in random_list:
    for operator in operators:

        if operator == "plus":
            first_result = nested_list[1] + nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                                                   
                elif operator2 == "minus":
                    second_result = first_result - nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

                elif operator2 == "multiply":
                    second_result = first_result * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

                elif operator2 == "divide":
                    numerator = first_result
                    denominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

        elif operator == "minus":
            first_result = nested_list[1] - nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                            
                elif operator2 == "minus":
                    second_result = first_result - nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                          
                elif operator2 == "multiply":
                    second_result = first_result * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
  
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                            
                elif operator2 == "divide":
                    numerator = first_result
                    denominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                            
        elif operator == "multiply":
            first_result = nested_list[1] * nested_list[2]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = first_result + nested_list[3]

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"

                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                        
                elif operator2 == "minus":
                    second_result = first_result - nested_list[3]
                        
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"                          
                            
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                        
                elif operator2 == "multiply":
                    second_result = first_result * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

                elif operator2 == "divide":
                    numerator = first_result
                    dominator = nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

        elif operator == "divide":
            numerator1 = nested_list[1]
            denominator = nested_list[2]

            for operator2 in operators:
                if operator2 == "plus":
                    numerator2 = numerator1 + (nested_list[3] * denominator)

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"

                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                            
                elif operator2 == "minus":
                    numerator2 = numerator1 - (nested_list[3] * denominator)
                
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

                elif operator2 == "multiply":
                    numerator2 = numerator1 * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")

                elif operator2 == "divide":
                    denominator2 = denominator * nested_list[3]
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator2) + numerator1) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator2) - numerator1) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator1) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator2) / numerator1
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} (({nested_list[1]} {operator} {nested_list[2]}) {operator2} {nested_list[3]})")
                    
# Right grouping (reverse)
for nested_list in random_list:
    for operator in operators:

        if operator == "plus":
            first_result = nested_list[2] + nested_list[3]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[1] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                                                   
                elif operator2 == "minus":
                    second_result = nested_list[1] - first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")

                elif operator2 == "multiply":
                    second_result = nested_list[1] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                            
                elif operator2 == "divide":
                    numerator = nested_list[1]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                    
        elif operator == "minus":
            first_result = nested_list[2] - nested_list[3]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[1] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                                                       
                elif operator2 == "minus":
                    second_result = nested_list[1] - first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                        
                elif operator2 == "multiply":
                    second_result = nested_list[1] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                            
                elif operator2 == "divide":
                    numerator = nested_list[1]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")

        elif operator == "multiply":
            first_result = nested_list[2] * nested_list[3]
            
            for operator2 in operators:
                if operator2 == "plus":
                    second_result = nested_list[1] + first_result

                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                                               
                elif operator2 == "minus":
                    second_result = nested_list[1] - first_result
                        
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")

                elif operator2 == "multiply":
                    second_result = nested_list[1] * first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            final_result = nested_list[0] + second_result
                        elif operator3 == "minus":
                            final_result = nested_list[0] - second_result
                        elif operator3 == "multiply":
                            final_result = nested_list[0] * second_result
                        elif operator3 == "divide": # not affected
                            try:
                                final_result = nested_list[0] / second_result
                            except ZeroDivisionError:
                                final_result = -1
                                
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
            
                elif operator2 == "divide":
                    numerator = nested_list[1]
                    denominator = first_result
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator) + numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator) - numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator) / denominator
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator) / numerator
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")

        elif operator == "divide":
            numerator1 = nested_list[2]
            denominator1 = nested_list[3]

            for operator2 in operators:
                if operator2 == "plus":
                    numerator2 = (nested_list[1] * denominator1) + numerator1

                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator1) + numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator1) - numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator1) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                                                       
                elif operator2 == "minus":
                    numerator2 = (nested_list[1] * denominator1) - numerator1
                
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator1) + numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator1) - numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator1) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                            
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")

                elif operator2 == "multiply":
                    numerator2 = nested_list[1] * numerator1
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator1) + numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator1) + numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator1
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator1) / numerator2
                            except ZeroDivisionError:
                                final_result = -1

                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")
                            
                elif operator2 == "divide":
                    numerator2 = nested_list[1] * denominator1
                    denominator2 = numerator1
                    
                    for operator3 in operators:
                        if operator3 == "plus":
                            try:
                                final_result = ((nested_list[0] * denominator2) + numerator2) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "minus":
                            try:
                                final_result = ((nested_list[0] * denominator2) - numerator2) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "multiply":
                            try:
                                final_result = (nested_list[0] * numerator2) / denominator2
                            except ZeroDivisionError:
                                final_result = -1
                        elif operator3 == "divide":
                            try:
                                final_result = (nested_list[0] * denominator2) / numerator2
                            except ZeroDivisionError:
                                final_result = -1
                        
                        if final_result == 24 or final_result == 24.0:
                            if operator == "plus":
                                operator = "+"
                            elif operator == "minus":
                                operator = "-"
                            elif operator == "multiply":
                                operator = "*"
                            elif operator == "divide":
                                operator = "/"
                                
                            if operator2 == "plus":
                                operator2 = "+"
                            elif operator2 == "minus":
                                operator2 = "-"
                            elif operator2 == "multiply":
                                operator2 = "*"
                            elif operator2 == "divide":
                                operator2 = "/"
                                
                            if operator3 == "plus":
                                operator3 = "+"
                            elif operator3 == "minus":
                                operator3 = "-"
                            elif operator3 == "multiply":
                                operator3 = "*"
                            elif operator3 == "divide":
                                operator3 = "/"
                                
                            print(f"{nested_list[0]} {operator3} ({nested_list[1]} {operator2} ({nested_list[2]} {operator} {nested_list[3]}))")