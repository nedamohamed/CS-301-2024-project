#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import itertools


# In[2]:


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


# In[6]:


def max_2_sat_k(clauses, num_vars, k):
    for assignment in itertools.product([False, True], repeat=num_vars):
        satisfied = 0
        
        for (var1, sign1), (var2, sign2) in clauses:
            if (assignment[var1] == sign1) or (assignment[var2] == sign2):
                satisfied += 1
                
        if satisfied == k:
            return assignment
            
    return None


# In[11]:


def run_test_case(test_num, num_vars, num_clauses, k):
    result = f"Test Case {test_num}:\n"
    result += f"Number of Variables: {num_vars}, Number of Clauses: {num_clauses}, k: {k}\n"
    
    clauses = generate_random_2sat_problem(num_vars, num_clauses)
    result += f"Generated Clauses: {clauses}\n"
    
    assignment = max_2_sat_k(clauses, num_vars, k)
    
    if assignment:
        result += f"Assignment satisfying exactly {k} clauses: {assignment}\n\n"
    else:
        result += f"No assignment satisfies exactly {k} clauses.\n\n"
    
    return result


# In[12]:


# Open a file to write the output
with open('test_cases_output.txt', 'w') as file:
    # Generate and run 20 test cases
    for i in range(1, 21):
        num_vars = random.randint(2, 6)  # Randomly select number of variables between 2 and 6
        num_clauses = random.randint(num_vars + 1, num_vars * 2)  # Clauses between num_vars+1 and num_vars*2
        k = random.randint(1, num_clauses - 1)  # Ensure k < num_clauses
        result = run_test_case(i, num_vars, num_clauses, k)
        file.write(result)


# In[ ]:




