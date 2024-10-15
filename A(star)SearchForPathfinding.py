graph = {'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Bucharest': ['Urziceni','Pitesti', 'Giurgiu','Fagaras'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Dobreta': ['Mehadia'],
    'Eforie': ['Hirsova'],
    'Iasai': ['Vaslui','Neamt'],
    'Lugoj': ['Timisoara','Mehadia'],
    'Oradea': ['Zerind','Sibiu'],
    'Pitesti': ['Rimnicu Vilcea','Bucharest','Craiova'],
    'Urziceni': ['Vaslui'],
    'Zerind': ['Oradea','Arad'],
    'Sibiu': ['Oradea','Arad','Rimnicu Vilcea','Fagaras'],
    'Timisoara': ['Arad','Lugoj'],
    'Mehadia': ['Lugoj','Dobreta'],
    'Rimnicu Vilcea': ['Sibiu','Pitesti','Craiova'],
    'Fagaras': ['Sibiu','Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Vaslui': ['Urziceni','Iasai'],
    'Neamt': ['Iasai']}

pc = {('Arad','Zerind'):75,
    ('Arad','Timisoara'):118,
    ('Arad','Sibiu'):140,
    ('Zerind','Oradea'):71,
    ('Zerind','Arad'):75,
    ('Timisoara','Arad'):118,
    ('Timisoara','Lugoj'):111,
    ('Sibiu','Arad'):140,
    ('Sibiu','Rimnicu Vilcea'):80,
    ('Sibiu','Fagaras'):99,
    ('Sibiu','Oradea'):151,
    ('Oradea','Zerind'):71,
    ('Oradea','Sibiu'):151,
    ('Lugoj','Timisoara'):111,
    ('Lugoj','Mehadia'):70,
    ('Rimnicu Vilcea','Sibiu'):80,
    ('Rimnicu Vilcea','Pitesti'):97,
    ('Rimnicu Vilcea','Craiova'):146,
    ('Fagaras','Sibiu'):99,
    ('Fagaras','Bucharest'):211,
    ('Mehadia','Lugoj'):70,
    ('Mehadia','Dobreta'):75,
    ('Pitesti','Rimnicu Vilcea'):97,
    ('Pitesti','Bucharest'):101,
    ('Pitesti','Craiova'):138,
    ('Craiova','Rimnicu Vilcea'):146,
    ('Craiova','Dobreta'):120,
    ('Craiova','Pitesti'):138,
    ('Bucharest','Fagaras'):211,
    ('Bucharest','Bucharest'):0,
    ('Bucharest','Pitesti'):101,
    ('Bucharest','Giurgiu'):90,
    ('Bucharest','Urziceni'):85,
    }

locs={'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Iasai': 226,
    'Lugoj': 244,
    'Oradea': 380,
    'Pitesti': 100,
    'Urziceni': 80,
    'Zerind': 374,
    'Sibiu': 253,
    'Timisoara': 329,
    'Mehadia': 241,
    'Rimnicu Vilcea': 193,
    'Fagaras':176,
    'Giurgiu': 77,
    'Vaslui': 199,
    'Neamt': 234
    }

def DFS(g, v, goal, explored, path_so_far,m):
    explored.add(v)
    node=[]
    
    if v == goal:
        return path_so_far +" -> "+ v
    
    for w in g[v]:
        if w not in explored:
            f=locs.get(w)+pc.get((v,w))
            
            if m>f:
                m=f
                print("%i - %s - %s " %(m,v,w))
                node=w
                
    p = DFS(g, node, goal, explored, path_so_far +" -> "+ v,m)
    if p:
        return p
    return ""

print(DFS(graph, 'Arad', 'Bucharest', set(), "",1000))
