import sys
from collections import defaultdict

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
        self.edges_back = defaultdict(list)
        self.weights_back = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
        self.edges_back[to_node].append(from_node)
        self.weights_back[(to_node, from_node)] = weight
    
    def construct_graph(self, edge):
        self.add_edge(*edge)
    
    def remove_edge(self, edge):
        self.edges.pop(edge[0])
        self.weights.pop((edge[0], edge[1]))

graph = Graph()

edges = []
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#     n, m = lines[0].split(' ')
#     s, t, d = lines[int(m) + 1].split(' ')
#     d = int(d)
#     for i in range(1, int(m) + 1):
#         edge = lines[i].split(' ')
#         edge = (edge[0], edge[1], int(edge[2]))
#         graph.construct_graph(edge)

n, m = sys.stdin.readline().split(' ')
n, m = int(n), int(m)
c = m
while c:
    #print(c)
    edge = sys.stdin.readline().split(' ')
    edge = (edge[0], edge[1], int(edge[2]))
    graph.construct_graph(edge)
    c = c -1

s, t, d = sys.stdin.readline().split(' ')
d = int(d)

# print(graph.edges)
# print(graph.weights)

def binary_search_mod(arr2, x, val):
    #print('Iter', x)
    lo, hi = 0, len(arr2) -1
    cc = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        #print('lo hi mid', lo, hi, mid)
        if arr2[mid] + x + 1 <= val:
            #print('arr_mid x ', arr2[mid], x)
            cc = cc + (mid-lo + 1)
            lo = mid + 1
        elif arr2[mid] + x + 1 > val:
            hi = mid - 1
    return cc

def dijkstra(graph, s, t, d):
    n_possible = 0
    next_node_F = None
    next_node_B = None

    shortest_paths = {s: (None, 0)}
    current_node = s
    visited = set()
    dist_forw = []

    shortest_paths_back = {t: (None, 0)}
    current_node_back = t
    visited_back = set()
    dist_back = []

    while current_node != t and current_node_back != s:
        visited.add(current_node)
        visited_back.add(current_node_back)
        #destinations = graph.edges[current_node]

        destinations = graph.edges.get(current_node)
        destinations_back = graph.edges_back.get(current_node_back)

        if destinations == None:
           current_node = t
        else:
            weight_to_current_node = shortest_paths[current_node][1]
            #shorter_dist_forw.append(weight_to_current_node)

        if destinations_back == None:
            current_node_back = s
        else:
            weight_to_current_node_b = shortest_paths_back[current_node_back][1]
            #shorter_dist_back.append(weight_to_current_node_b)
        

        if current_node != t:
            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

                next_node_F = next_node

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            
            if not next_destinations:
                return "Route not possible"
            
            #print('shortest_paths_F',shortest_paths)
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            #print('current_ node', current_node)

        if current_node_back != s:
            for next_node_ in destinations_back:
                weight_ = graph.weights_back[(current_node_back, next_node_)] + weight_to_current_node_b
                if next_node_ not in shortest_paths_back:
                    shortest_paths_back[next_node_] = (current_node_back, weight_)
                else:
                    current_shortest_weight_back = shortest_paths_back[next_node_][1]
                    if current_shortest_weight_back > weight_:
                        shortest_paths_back[next_node_] = (current_node_back, weight_)

                next_node_B = next_node_
            next_destinations_back = {node_: shortest_paths_back[node_] for node_ in shortest_paths_back if node_ not in visited_back}

            if not next_destinations_back:
                return "Route back not possible"
            
            #print('shortest_paths_B',shortest_paths_back)
            current_node_back = min(next_destinations_back, key=lambda k: next_destinations_back[k][1])
    
    #shorter_dist_forw.append(shortest_paths[next_node_F][1])
    #shorter_dist_back.append(shortest_paths_back[next_node_B][1])

    dist_forw = [item[1] for item in list(shortest_paths.values())]
    dist_back = [item[1] for item in list(shortest_paths_back.values())]

    #possible_pairs = ([(d-k,k) for k in shorter_dist_forw if (d-k) in shorter_dist_back])
    s1 = list(set(dist_forw))
    s2 = list(set(dist_back))
    count = 0
    
    for i in s1:
        count = count + binary_search_mod(s2, i, d)

    #print('dist_forw',dist_forw)
    #print('dist_back',dist_back)
    
    # Working back
    # path = []
    # tweight = 0
    # while current_node is not None:
    #     path.append(current_node)
    #     next_node = shortest_paths[current_node][0]
    #     current_node = next_node

    # # Reverse path
    # path = path[::-1]
    # tweight = shortest_paths[path[len(path) - 1]][1]

    return count


# def possible_paths(s, t, d):
#     n_possible = 0
#     partial_paths = []
#     for i in range(1,int(n)+1):
#         for j in range(1,int(n)+1):
#             if i != j:
#                 if graph.weights.get((str(i), f'{j}')) == None:
#                     graph.construct_graph((str(i), str(j), 1))
#                     print(graph.edges)
#                     print(graph.weights)
#                 graph.weights[(f'{i}', f'{j}')] = 1
#                 if s != str(j):
#                     path1, w1 = dijkstra(graph, s, str(j))
#                     if path1 not in partial_paths:
#                         partial_paths.append(path1)  
#                         if w1 < d:
#                             path2, w2 = dijkstra(graph, str(j), t)
#                             if w1 + w2 <= d and len(path2)>0:
#                                 n_possible += 1
#                         if str(j) == t and w1 <= d:
#                             n_possible += 1
#     print('pasrtial', partial_paths)
#     return n_possible

# print(possible_paths(s, t, d))

print(dijkstra(graph, s, t, d))