from itertools import permutations
# function to solve TSP

def travelling_salesman(graph,start):
  cities =list(range(len(graph)))
  cities.remove(start)

  min_cost = float('inf')
  best_path = None


  #generate all possible tours 
  for perm in permutations(cities):
    current_cost =0
    current_path=[start]
    k = start


    #visit each city in the permutation
    for city in perm:
      current_cost += graph[k][city]
      current_path.append(city)
      k = city

    #return to the starting city
    current_cost += graph[k][start]
    current_path.append(start)



    # check if this is the minimum-cost tour
    if current_cost < min_cost:
      min_cost = current_cost
      best_path = current_path

  return best_path, min_cost


# main program 
n= int(input("Enter the number of cities: "))
print("enter the cost matrix :")
graph = []

for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)

start = int(input("Enter the starting city: "))
best_path, min_cost = travelling_salesman(graph,start)

print("\noptimal path:","->".join(map(str,best_path)))
print("minimum cost:",min_cost)