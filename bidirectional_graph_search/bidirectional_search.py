from collections import defaultdict
import heapq as hq
import math

class Graph:
    graph = defaultdict(lambda: [])
    n = 0
    m = 0
    s = 0
    t = 0
    d = 0

    def __init__(self):
        self.reader()
    
    def reader(self):
        with open('input.txt', 'r') as file:
            lines = file.read().splitlines()
            for iline in range(len(lines)):
                if iline == 0:
                    self.n = lines[iline].split(' ')[0]
                    self.m = lines[iline].split(' ')[1]
                    print(self.n, self.m)
                elif iline == len(lines) - 1:
                    self.s = lines[iline].split(' ')[0]
                    self.t = lines[iline].split(' ')[1]
                    self.d = lines[iline].split(' ')[2]
                else:
                    subdict = {lines[iline].split(' ')[1]:lines[iline].split(' ')[2]}
                    self.graph[lines[iline].split(' ')[0]].append(subdict)
            
            print(self.graph)

class Queue:
    def __init__(self, v, p):
        self.v = v
        self.p = p

    def __lt__(self, other):
        return self.p < other.p

def traversal(T,pred):
    path = []
    while T:
        path.append(T)
        T = pred[T]
    return path[::-1]

def reverse_traversal(v, pre_S, pre_T):
    path = traversal(v, pre_S)
    v = pre_T[v]
    while v:
        path.append(v)
        v = pre_T[v]
    return path

def bidirectional_dijkstra(G, S, T):

    startS = [Queue(S, 0.0)]
    startT = [Queue(T, 0.0)]

    goal_S = set()
    goal_T = set()

    pre_S = dict()
    pre_T = dict()
    dist_S = dict()                                                 # Dictionary to store distance from source to target
    dist_T = dict()                                                 # Dictionary to store distance from target to source

    v_dist = {'weight': math.inf}                                         # Setting other vertex initial distance to inf
    node = {'weight': None}


    pre_S[S] = None
    pre_T[T] = None
    dist_S[S] = 0.0
    dist_T[T] = 0.0
    def update(v, weight,goal):
        if v in goal:
            distance = dist_T[v] + weight
            if v_dist['weight'] > distance:
                v_dist['weight'] = distance
                node['weight'] = v

    while startS and startT:
        if dist_S[startS[0].v] + dist_T[startT[0].v] >= v_dist['weight']:
            return reverse_traversal(node['weight'], pre_S, pre_T)

        if len(startS) + len(goal_S) < len(startT) + len(goal_T):
            C = hq.heappop(startS).v                #Pop the smallest item off the heap, maintaining the heap invariant.
            goal_S.add(C)                                                                             #C is current node
            for fwd in G[C]:
                if fwd in goal_S:
                    continue
                cur_dist = dist_S[C] + G[C][fwd]['weight']
                if fwd not in dist_S or cur_dist < dist_S[fwd]:
                    dist_S[fwd] = cur_dist
                    pre_S[fwd] = C
                    hq.heappush(startS, Queue(fwd, cur_dist))
                    update(fwd, cur_dist, goal_T)
        else:
            C = hq.heappop(startT).v                # Pop the smallest item off the heap, maintaining the heap invariant
            goal_T.add(C)
            for back in G[C]:
                if back in goal_T:
                    continue
                cur_dist = dist_T[C] + G[back][C]['weight']
                if back not in dist_T or cur_dist < dist_T[back]:
                    dist_T[back] = cur_dist
                    pre_T[back] = C
                    hq.heappush(startT, Queue(back, cur_dist))
                    update(back, cur_dist, goal_S)

    return []


gr = Graph()
