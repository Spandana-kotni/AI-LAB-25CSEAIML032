from collections import deque

# function to check whether a block is clear
def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True

# generate possible moves
def generate_moves(state, blocks):
    moves = []
    for block in blocks:
        # block must be clear
        if not is_clear(state, block):
            continue

        # find current position
        current_position = None
        for b, position in state:
            if b == block:
                current_position = position
                break

        if current_position is None:
            continue

        # move block to table
        if current_position != 'table':
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, 'table'))
            moves.append((
                frozenset(new_state),
                f"Move {block} from {current_position} to table"
            ))

        # move block on to another block
        for destination in blocks:
            if block == destination:
                continue
            if not is_clear(state, destination):
                continue
            # dont move to the same position
            if current_position == destination:
                continue

            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))
            moves.append((
                frozenset(new_state),
                f"Move {block} from {current_position} to {destination}"
            ))
    return moves

# bfs function
def block_world(initial_state, goal_state, blocks):
    initial_state_frozen = frozenset(initial_state)
    goal_state_frozen = frozenset(goal_state)

    queue = deque()
    queue.append((initial_state_frozen, []))

    visited = set()
    visited.add(initial_state_frozen)

    while queue:
        state, path = queue.popleft()

        if state == goal_state_frozen:
            return path

        for next_state, action in generate_moves(state, blocks):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return None

# Example usage:
if __name__ == '__main__':
    # Example: A on B on Table -> B on A on Table
    # State representation: set of tuples (block, what_it_is_on)
    blocks_list = ['A', 'B']
    start = frozenset([('A', 'B'), ('B', 'table')])
    goal = frozenset([('B', 'A'), ('A', 'table')])

    solution = block_world(start, goal, blocks_list)
    print("Steps to reach the goal:")
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")