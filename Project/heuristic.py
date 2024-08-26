#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import itertools

def generate_random_2sat_problem(num_vars, num_clauses):
    clauses = []
    for _ in range(num_clauses):
        var1 = random.randint(0, num_vars - 1)
        var2 = random.randint(0, num_vars - 1)
        
        while var1 == var2:
            var2 = random.randint(0, num_vars - 1)
        
        sign1 = random.choice([True, False])
        sign2 = random.choice([True, False])
        
        clauses.append(((var1, sign1), (var2, sign2)))
    
    return clauses

def heuristic_max_2_sat(clauses, num_vars, k):
    assignment = [False] * num_vars

    # Loop through the first k clauses
    for i in range(min(k, len(clauses))):
        (var1, sign1), (var2, sign2) = clauses[i]
        
        # Set the first variable of each clause to true
        if not assignment[var1] and not assignment[var2]:
            assignment[var1] = sign1
        elif not assignment[var1]:
            assignment[var1] = sign1
        elif not assignment[var2]:
            assignment[var2] = sign2

    satisfied = 0

    # Count how many clauses are satisfied by this assignment
    for (var1, sign1), (var2, sign2) in clauses:
        if (assignment[var1] == sign1) or (assignment[var2] == sign2):
            satisfied += 1

    return assignment, satisfied

def run_test_case(test_num, num_vars, num_clauses, k):
    result = f"Test Case {test_num}:\n"
    result += f"Number of Variables: {num_vars}, Number of Clauses: {num_clauses}, k: {k}\n"
    
    clauses = generate_random_2sat_problem(num_vars, num_clauses)
    result += f"Generated Clauses: {clauses}\n"
    
    assignment, satisfied = heuristic_max_2_sat(clauses, num_vars, k)
    
    result += f"Assignment: {assignment}\n"
    result += f"Satisfied Clauses: {satisfied}/{num_clauses}\n\n"
    
    return result

# Open a file to write the output
with open('heuristic_test_cases_output.txt', 'w') as file:
    # Generate and run 20 test cases
    for i in range(1, 21):
        num_vars = random.randint(2, 6)  # Randomly select number of variables between 2 and 6
        num_clauses = random.randint(num_vars + 1, num_vars * 2)  # Clauses between num_vars+1 and num_vars*2
        k = random.randint(1, num_clauses)  # k can be up to num_clauses
        result = run_test_case(i, num_vars, num_clauses, k)
        file.write(result)


# In[ ]:




