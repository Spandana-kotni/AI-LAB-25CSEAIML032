def bfs(graph, start_node): 
    visited = [] 
    queue = [start_node] 
    
    while queue: 
        current_node = queue.pop(0) 
        if current_node not in visited: 
            print(f"Exploring node: {current_node}") 
            visited.append(current_node) 
            
            # .get() prevents errors if a node has no outgoing edges 
            for neighbour in graph.get(current_node, []): 
                if neighbour not in visited and neighbour not in queue: 
                    queue.append(neighbour) 
    return visited 

# ---User Input Section --- 
print("--- Build Your Graph---") 
student_graph = {} 

# Get the total number of connections 
num_edges = int(input("How many edges (connections) does your graph have? ")) 
print("Enter each edge separated by a space (e.g., A B):") 

for i in range(num_edges): 
    # Read the input and split it into two variables 
    u, v = input(f"Edge {i+1}: ").split() 
    
    # Initialize the lists if the nodes don't exist yet 
    if u not in student_graph: 
        student_graph[u] = [] 
    if v not in student_graph: 
        student_graph[v] = [] 
        
    # Add the connection (undirected graph) 
    student_graph[u].append(v) 
    student_graph[v].append(u) 

# Get the starting point 
start = input("Enter the starting node for BFS: ") 

print(f"\nYour graph dictionary: {student_graph}") 
print("Starting BFS traversal...")

# FIX: Added the missing function call to execute the algorithm
traversal_result = bfs(student_graph, start)
print(f"Final BFS path: {traversal_result}")
