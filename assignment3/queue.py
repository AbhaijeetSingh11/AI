from collections import deque

def move(state, from_pile_index, to_pile_index):
    state = list(state)
    block = state.pop(from_pile_index)
    state.insert(to_pile_index, block)
    return ''.join(state)

def is_goal(state, goal):
    return state == goal

def bfs(initial, goal):
    visited = set()
    queue = deque([(initial, [])])

    while queue:
        current_state, path = queue.popleft()
        if is_goal(current_state, goal):
            return path + [current_state]

        visited.add(current_state)
        for action in range(len(current_state) - 1):
            for dest in range(action + 1, len(current_state)):
                new_state = move(current_state, action, dest)
                if new_state not in visited:
                    queue.append((new_state, path + [current_state]))
                    visited.add(new_state)
    return None

initial_state = "ABC"
goal_state = "CBA"

result = bfs(initial_state, goal_state)
if result:
    print("Path found:", result)
else:
    print("No solution found.")