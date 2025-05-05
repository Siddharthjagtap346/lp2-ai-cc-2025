def find(parent, i):            #kruskals
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(nodes, edges):
    result = []
    parent = []
    rank = []

    for node in range(nodes):
        parent.append(node)
        rank.append(0)

    edges = sorted(edges, key=lambda item: item[2])

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            result.append((u, v, w))
            union(parent, rank, x, y)

    for u, v, weight in result:
        print(f"{u} -- {v} == {weight}")

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
kruskal(4, edges)
