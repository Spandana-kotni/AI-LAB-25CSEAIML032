from collections import deque

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()

    #queue stores: (jug1_water, jug2_water, path_history)
    queue.append((0, 0, []))

    while queue:
        j1, j2, path = queue.popleft()

        if(j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        #check if target state (e.g.,(2,3)) is reached
        if (j1, j2) == target_state:
            return current_path

        #generate all possible next moves
        next_moves = [
            (cap1,j2),      #fill jug1
            (j1,cap2),      #fill jug2
            (0,j2),         #empty jug 1
            (j1,0),         #empty jug 2
            (j1-min(j1,cap2-j2),j2+min(j1,cap2-j2)),    #pour jug 1 -> jug 2
            (j1+min(j2,cap1-j1),j2-min(j2,cap1-j1)),    #pour jug 2 -> jug 1
        ]

        for move in next_moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))
    return None

#solve for jug 1 capacity = 4l, jug 2 capacity = 3l, goal state = (2,3)
target_goal = (4,2)
solution = water_jug(4, 3, target_goal)

if solution:
    print(f"steps to reach target state {target_goal}:")
    for step in solution:
        print(step)
else:
    print("no solution exists.")