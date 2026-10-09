import heapq

def a_star(graph, start, goal, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        f_cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbour, cost in graph[current]:

            new_g = g_cost[current] + cost

            if neighbour not in g_cost or new_g < g_cost[neighbour]:

                g_cost[neighbour] = new_g

                f_cost = new_g + heuristic[neighbour]

                heapq.heappush(open_list, (f_cost, neighbour))

                parent[neighbour] = current

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 0
}

start = 'A'
goal = 'E'

path = a_star(graph, start, goal, heuristic)

print("Shortest path:", path)