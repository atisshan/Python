def dijkstra(graph, start):
    distances={node:float('inf') for node in graph}
    distances[start]=0

    visited=set()
    while len(visited) < len(graph):
        min_distances=float('inf')
        min_node=None

        for node in graph:
            if distances[node] < min_distances and node not in visited:
                min_distances=distances[node]
                min_node=node
        if min_node is None:
            break
        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            distance=distances[min_node] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor]=distance
  
    return distances
graph={
    
    "A":{"B":1, "C":4},
    "B":{"A":1, "C":2, "D":5},
    "C":{"A":4, "B":2, "D":1},
    "D":{"B":5, "C":1}
}
result=dijkstra(graph, "A")
print(result)



















































            