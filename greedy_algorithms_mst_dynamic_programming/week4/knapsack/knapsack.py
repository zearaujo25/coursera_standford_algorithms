def knapsack(sack_size,items):
    problem_array = []
    problem_array.append([0 for space_left in range(0,sack_size+1)])
    for item in items:
        problem_array.append([])
        for used_space in range(0,sack_size+1):
            item_weight = item[0]
            item_value = item[1]
            iteration_answer = max(problem_array[-2][used_space],problem_array[-2][-item_weight]+item_value)
            problem_array[-1].append(iteration_answer)
    return problem_array[-1][-1]