graph = {'A': ['B', 'C'],
             'B': ['C','D'],
             'C': ['D'],
             'D': ['F'],
             'E': ['F'],
             'F': ['C']}

def find_all_paths(graph,start,end,path=[]):
    path += [start]
    if start == end:
        return path
    for nodes in graph[start]:
        newpath = find_all_paths(graph,nodes,end,path)
        print newpath
    return None

print find_all_paths(graph,'A','D')
#print find_all_paths(graph,'A','C',[])
