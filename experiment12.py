'''
from collections import deque

# Function to check whether a block is clear
def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True

# Generate possible moves
def generate_moves(state, blocks):
    moves = []
    
    for block in blocks:
        # Block must be clear
        if not is_clear(state, block):
            continue
            
        # Find current position
        current_position = None
        for b, position in state:
            if b == block:
                current_position = position
                break
                
        # Move block to Table
        if current_position != "Table":
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, "Table"))
            moves.append(
                (frozenset(new_state), 
                 f"Move {block} from {current_position} to Table")
            )
            
        # Move block onto another block
        for destination in blocks:
            if block == destination:
                continue
                
            # Destination must be clear
            if not is_clear(state, destination):
                continue
                
            # Don't move to the same position
            if current_position == destination:
                continue
                
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))
            moves.append(
                (frozenset(new_state), 
                 f"Move {block} from {current_position} to {destination}")
            )
            
    return moves

# BFS function
def block_world(initial_state, goal_state, blocks):
    queue = deque()
    queue.append((frozenset(initial_state), []))
    
    visited = set()
    visited.add(frozenset(initial_state))
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check goal
        if current_state == frozenset(goal_state):
            return path
            
        # Generate next states
        for next_state, action in generate_moves(current_state, blocks):
            if next_state not in visited:
                visited.add(next_state)
                # Append the action taken to the current path list
                queue.append((next_state, path + [action]))
                
    return None  # Return None if no solution is found

# --- Example Usage ---
if __name__ == "__main__":
    # Define available blocks
    all_blocks = ["A", "B", "C"]
    
    # State format: (block, what_it_is_on_top_of)
    # Initial: A is on Table, B is on Table, C is on A
    init = {("A", "Table"), ("B", "Table"), ("C", "A")}
    
    # Goal: Stack them linearly: A on B, B on C, C on Table
    goal = {("C", "Table"), ("B", "C"), ("A", "B")}
    
    solution = block_world(init, goal, all_blocks)
    
    if solution:
        print("Steps to reach the goal:")
        for step, move in enumerate(solution, 1):
            print(f"{step}. {move}")
    else:
        print("No solution found.")

'''        

import heapq

# Uniform Cost Search
def ucs(graph, start, goal):
    # Priority queue
    priority_queue = []
    # (cost, node, path)
    heapq.heappush(priority_queue, (0, start, [start]))
    
    # Store the lowest cost found for each node
    visited = {}
    
    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)
        
        # If node was already reached with lower cost
        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost
        
        # Goal found
        if current == goal:
            return path, cost
            
        # Explore neighbors
        for neighbor, edge_cost in graph[current]:
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )
            
    return None, float('inf')

# Main Program
if __name__ == "__main__":
    print("===== UNIFORM COST SEARCH =====")
    n = int(input("Enter number of nodes: "))
    graph = {}
    
    for i in range(n):
        graph[i] = []
        
    # Enter edges
    e = int(input("Enter number of edges: "))
    print("Enter edges as:")
    print("source destination cost")
    for i in range(e):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        
    start = int(input("Enter starting node: "))
    goal = int(input("Enter goal node: "))
    
    # Perform UCS
    path, cost = ucs(graph, start, goal)
    
    # Display result
    if path:
        print("\nGoal Found!")
        print("Optimal Path:", " -> ".join(map(str, path)))
        print("Minimum Cost:", cost)
    else:
        print("\nGoal not found or unreachable from the starting node.")
