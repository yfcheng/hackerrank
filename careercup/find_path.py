graph = {'A': ['B', 'C'],
             'B': ['C','D'],
             'C': ['D'],
             'D': ['F'],
             'E': ['F'],
             'F': ['C']}

#find path from A-D
def find_path(graph,start,end,path=[]):
    path += [start]
    if start == end or (end in graph[start]):
        path += [end]
        return path
    for nodes in graph[start]:
        if nodes not in path:
            return find_path(graph,nodes,end,path)
    return None

#print find_path(graph,'A','D',[])
#print find_path(graph,'A','C',[])
#print find_path(graph,'A','F',[])

#find all paths from A-D
def find_all_paths(graph,start,end,path=[]):
    path += [start]
    if start == end:
        path += [end]
        return path
    for nodes in graph[start]:
        if nodes in path:
            newpath = find_all_paths(graph,nodes,end,path)
            if newpath:
                path.append(newpath)
    return None

print find_all_paths(graph,'A','D',[])
#print find_all_paths(graph,'A','C',[])
#print find_all_paths(graph,'A','F',[])

#find the shortest path from A-D




#print find_path(graph,'A','D',[])
#print find_path(graph,'A','C',[])
#print find_path(graph,'A','F',[])

#print find_all_paths(graph,'A','D')

#print find_shortest_path(graph,'A','D')
