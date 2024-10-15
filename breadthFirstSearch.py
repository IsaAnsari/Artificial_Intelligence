class first:
    def __init__(self,graph,start,goal):
        self.start = start
        self.goal = goal
        self.graph=graph
        
    def bfs_shortest_path(self):
        explored = []
        queue = [[self.start]]
        
        if self.start == self.goal:
            return "That was easy! Start = goal"
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            neighbours = self.graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == self.goal:
                    return new_path
                
            explored.append(node)
            
        return "path doesn't exist"
    
graph = {'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Bucharest': ['Urziceni','Pitesti', 'Giurgiu','Fagaras'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Dobreta': ['Mehadia'],
    'Eforie': ['Hirsova'],
    'Iasai': ['Vaslui','Neamt'],
    'Lugoj': ['Timisoara','Mehadia'],
    'Oradea': ['Zerind','Sibiu'],
    'Pitesti': ['Rimnicu Vilcea'],
    'Urziceni': ['Vaslui'],
    'Zerind': ['Oradea','Arad'],
    'Sibiu': ['Oradea','Arad','Rimnicu Vilcea','Fagaras'],
    'Timisoara': ['Arad','Lugoj'],
    'Mehadia': ['Lugoj','Dobreta'],
    'Rimnicu Vilcea': ['Sibiu','Pitesti','Craiova'],
    'Fagaras': ['Sibiu','Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Vaslui': ['Urziceni','Iasai'],
    'Neamt': ['Iasai']
    }

f=first(graph,'Arad','Bucharest')
print(f.bfs_shortest_path())
