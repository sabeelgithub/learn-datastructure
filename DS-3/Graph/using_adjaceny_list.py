# Represntaipon using Adjaceny list
graph = {}
print(graph)
def add_node(v):
    if v in graph:
        print(f'its {v} already present')
        return
    else:
        graph[v] = []

# in the case undirected and unweighted
def add_edge(v1,v2):
    if v1 not in graph:
        print(f'vertx {v1} not in graph')
    elif v2 not in graph:
        print(f'vertx {v2} not in graph')
    
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

# in the case directed and unweighted
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(f'vertx {v1} not in graph')
#     elif v2 not in graph:
#         print(f'vertx {v2} not in graph')
    
#     else:
#         graph[v1].append(v2)

# in the case undirected and weighted
# def add_edge(v1,v2,val):
#     if v1 not in graph:
#         print(f'vertx {v1} not in graph')
#     elif v2 not in graph:
#         print(f'vertx {v2} not in graph')
    
#     else:
#         graph[v1].append([v2,val])
#         graph[v2].append([v1,val])

# in the case directed and weighted
# def add_edge(v1,v2,val):
#     if v1 not in graph:
#         print(f'vertx {v1} not in graph')
#     elif v2 not in graph:
#         print(f'vertx {v2} not in graph')
    
#     else:
#         graph[v1].append([v2,val])
        
def delete_node(v):
    if v not in graph:
        print(f'item with key {v} not in graph')
    else:
        graph.pop(v)
        for i in graph:
            list = graph[i]
            for j in list:
                if j[0] == v:
                    list.remove(j)
                    break

# in the case of undirected and unweighted
def delete_edge(v1,v2):
    if v1 not in graph:
        print(f'cant delete edget,beacuse {v1} not found')       
    elif v2 not in graph:
        print(f'cant delete edget,beacuse {v2} not found')
    else:
        if v2 in graph[v1] and v1 in graph[v2]:
          graph[v1].remove(v2)
          graph[v2].remove(v1)
        elif v2 in graph[v1]:
            graph[v1].remove(v2)
        elif v1 in graph[v2]:
            graph[v2].remove(v1)

# in the case of directed and unweighted
# def delete_edge(v1,v2):
#     if v1 not in graph:
#         print(f'cant delete edget,beacuse {v1} not found')       
#     elif v2 not in graph:
#         print(f'cant delete edget,beacuse {v2} not found')
#     else:
#         if v2 in graph[v1] and v1 in graph[v2]:
#           graph[v1].remove(v2)
#           graph[v2].remove(v1)
#         elif v2 in graph[v1]:
#             graph[v1].remove(v2)
#         elif v1 in graph[v2]:
#             graph[v2].remove(v1)

# in the case of undirected and weighted
# def delete_edge(v1,v2,val):
#     if v1 not in graph:
#         print(f'cant delete edget,beacuse {v1} not found')       
#     elif v2 not in graph:
#         print(f'cant delete edget,beacuse {v2} not found')
#     else:
#         if [v2,val] in graph[v1] and [v1,val] in graph[v2]:
#           graph[v1].remove([v2,val])
#           graph[v2].remove([v1,val])
#         elif [v2,val] in graph[v1]:
#             graph[v1].remove([v2,val])
#         elif [v1,val] in graph[v2]:
#             graph[v2].remove([v1,val])

# def delete_edge(v1,v2,val):
#     if v1 not in graph:
#         print(f'cant delete edget,beacuse {v1} not found')       
#     elif v2 not in graph:
#         print(f'cant delete edget,beacuse {v2} not found')
#     else:
#         if [v2,val] in graph[v1] and [v1,val] in graph[v2]:
#           graph[v1].remove([v2,val])
#           graph[v2].remove([v1,val])
#         elif [v2,val] in graph[v1]:
#             graph[v1].remove([v2,val])
#         elif [v1,val] in graph[v2]:
#             graph[v2].remove([v1,val])
visited = set()
print(visited,'k')
def DFSRecursive(node,visited,graph):
    if node not in graph:
        print('node not in graph')
        return
    elif node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFSRecursive(i,visited,graph)

def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print('node not in graph')
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

def BFS(node,graph):
    visited = set()
    if node not in graph:
        print('node not in graph')
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                queue.append(i)


        


add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A','B')
add_edge('A','C')
add_edge('C','D')
BFS('A',graph)
print()
DFSRecursive('A',visited,graph)
print()
DFSiterative('A',graph)
# add_edge('A','B',9)
# add_edge('A','C',10)
# add_edge('C','D',11)

delete_node('B')
delete_edge('A','C')
# delete_edge('A','C',10)
print(graph)
