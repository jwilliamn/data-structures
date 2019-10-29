# Dijkstra Algorithm

from collections import defaultdict


class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
    
    def construct_graph(self, edges):
        for edge in edges:
            self.add_edge(*edge)

graph = Graph()

#edges = [(1, 2, 1),(2,3,1),(3,4,1)]
edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('H', 'G', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]


graph.construct_graph(edges)
#print('Edges:', graph.edges)
#print('Weights', graph.weights)

def dijkstra(graph, s, t):
    shortest_paths = {s: (None, 0)}
    current_node = s
    visited = set()

    while current_node != t:
        #print('current node... ', current_node)
        visited.add(current_node)
        #print('visited... ', visited)
        destinations = graph.edges[current_node]
        #print('destinatins... ', destinations)
        weight_to_current_node = shortest_paths[current_node][1]
        #print('weight to current node... ', weight_to_current_node)

        for next_node in destinations:
            #print('next node... ', next_node)
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            #print('weight... ', weight)
            #print('shortest paths... ', shortest_paths)
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
                #print('next shortest paths', shortest_paths)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        #print('next destinations... ', next_destinations)

        if not next_destinations:
            return "Route not possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        #print('current node .. ', current_node)

    # Working back
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # Reverse path
    path = path[::-1]
    return path
    
print(dijkstra(graph, 'X', 'Y'))
print(len(dijkstra(graph, 'X', 'Y')))