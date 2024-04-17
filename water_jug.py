def water_jug_problem(a_capacity, b_capacity, target):
    visited_states = set()
    state = (0, 0)
    while state[0] != target:
        # Check if the current state has been visited before
        if state in visited_states:
            print("Error: Infinite loop detected!")
            return
        visited_states.add(state)
        state = (a_capacity, state[1])
        print("Jug A:", state[0], "liters | Jug B:", state[1], "liters")
        pour_amount = min(state[0], b_capacity - state[1])
        state = (state[0] - pour_amount, state[1] + pour_amount)
        print("Jug A:", state[0], "liters | Jug B:", state[1], "liters")
        if state[0] == target:
            break
        if state[0] == 0:
            break
    print("Target of", target, "liters achieved in jug A!")

a_capacity = 4
b_capacity = 3
target = 2
print("Jug A: 0 liters | Jug B: 0 liters")
water_jug_problem(a_capacity, b_capacity, target)

