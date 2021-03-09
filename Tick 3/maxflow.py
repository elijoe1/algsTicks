import queue
import math


def get_graph_info(graph):
    edges = graph
    vertices = set()
    neighbours = {}
    for edge in edges:
        for vertex in edge:
            vertices.add(vertex)
        neighbours.setdefault(edge[0], set()).add(edge[1])
        # neighbours.setdefault(edge[1], set()).add(edge[0])
        neighbours.setdefault(edge[1], set())
    return edges, vertices, neighbours


def bfs_pathfinder(graph, s, t):
    edges, vertices, neighbours = get_graph_info(graph)
    seen = {vertex: False for vertex in vertices}
    come_from = {vertex: None for vertex in vertices}
    seen[s] = True
    to_explore = queue.Queue()
    to_explore.put(s)

    while not to_explore.empty():
        v = to_explore.get()
        for w in neighbours[v]:
            if not seen[w]:
                to_explore.put(w)
                seen[w] = True
                come_from[w] = v

    if come_from[t] is None:
        return None, seen, None
    else:
        path = [t]
        while come_from[path[0]] != s:
            path.insert(0, come_from[path[0]])
        path.insert(0, s)

    return path, seen, come_from


"""
Args:
    capacity: a dictionary {(from,to):edge_capacity, ...}
    s, t: the source and sink vertices
Returns a triple  (flow_value, flow, cutset)  where:
    flow_value: the value of the flow, i.e. a number
    flow: a dictionary {(from,to):flow_amount, ...}
    cutset: a list or set of vertices
"""


def compute_max_flow(capacity, s, t):
    flow = {}
    last_accessible = set()

    for edge in capacity.keys():
        flow[edge] = 0

    while True:
        p, last_accessible = find_augmenting_path(capacity, flow, s, t)
        if p is None:
            break
        else:
            delta = math.inf
            for edge in p:
                if edge[1] == "inc":
                    delta = min(delta, capacity[edge[0]] - flow[edge[0]])
                else:
                    delta = min(delta, flow[(edge[0][1], edge[0][0])])
            for edge in p:
                if edge[1] == "inc":
                    flow[edge[0]] += delta
                else:
                    flow[(edge[0][1], edge[0][0])] -= delta

    last_accessible = {vertex for vertex in last_accessible.keys() if last_accessible[vertex]}

    flow_value = 0

    for edge in flow.keys():
        if edge[0] == s:
            flow_value += flow[edge]

    return flow_value, flow, last_accessible


def find_augmenting_path(capacity, flow, s, t):
    residual_graph = {}
    path_with_labels = []
    for edge in capacity.keys():
        if flow[edge] < capacity[edge]:
            residual_graph[edge] = "inc"
        if flow[edge] > 0:
            residual_graph[(edge[1], edge[0])] = "dec"
    path, seen, _ = bfs_pathfinder(residual_graph.keys(), s, t)
    if path is None:
        return None, seen
    for i in range(len(path) - 1):
        edge = (path[i], path[i + 1])
        edge_label = residual_graph[edge]
        path_with_labels.append((edge, edge_label))
    if len(path_with_labels) > 0:
        return path_with_labels, seen
    else:
        return None, seen
