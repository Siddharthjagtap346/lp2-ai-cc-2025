import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, u = heapq.heappop(pq)
        for v, weight in graph[u]:
            if dist[v] > cost + weight:
                dist[v] = cost + weight
                heapq.heappush(pq, (dist[v], v))
    
    print("Shortest distances:", dist)

graph_dijkstra = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
dijkstra(graph_dijkstra, 0)
