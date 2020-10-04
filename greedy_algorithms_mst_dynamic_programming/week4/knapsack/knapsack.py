from collections import deque

def knapsack(sack_size,items):
    problem_array = deque()
    problem_array.append([0 for space_left in range(0,sack_size+1)])
    for item in items:
        problem_array.append([])
        for used_space in range(0,sack_size+1):
            problem_array[-1].append(None)
            item_weight = item[1]
            item_value = item[0]

            without_using_item = problem_array[-2][used_space]
            using_item = problem_array[-2][used_space-item_weight]+item_value if item_weight <= used_space else float("-inf")
            iteration_answer = max(without_using_item ,using_item)
            problem_array[-1][-1] = iteration_answer
        #cleaning the part of the array we will not use anymore
        problem_array.popleft()

    return problem_array[-1][-1]