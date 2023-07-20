# Represntaipon using Adjaceny matrix
nodes = []
graph = []
node_count = 0
print(nodes)
print(graph)
print(node_count)
def add_node(v):
    if v in nodes:
        print(f'its {v} already present')
        return
    else:
        global node_count
        node_count +=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# in the case of undirected and unweighted graph   
def add_vertex(v1,v2):
    if v1 not in nodes:
        print(f'its {v1} not  present')
        return
    elif v2 not in nodes:
        print(f'its {v2} not  present')
        return
    else:
        indexV1 = nodes.index(v1)
        indexV2 = nodes.index(v2)
        graph[indexV1][indexV2] = 1
        graph[indexV2][indexV1] = 1

# in the case of directed and unweigted graph
# def add_vertex(v1,v2):
#     if v1 not in nodes:
#         print(f'its {v1} not  present')
#         return
#     elif v2 not in nodes:
#         print(f'its {v2} not  present')
#         return
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = 1

# in the case of undirected and weigted graph
# def add_vertex(v1,v2,val):
#     if v1 not in nodes:
#         print(f'its {v1} not  present')
#         return
#     elif v2 not in nodes:
#         print(f'its {v2} not  present')
#         return
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = val
#         graph[indexV2][indexV1] = val

# in the case of directed and weigted graph
# def add_vertex(v1,v2,val):
#     if v1 not in nodes:
#         print(f'its {v1} not  present')
#         return
#     elif v2 not in nodes:
#         print(f'its {v2} not  present')
#         return
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = val
      
def delete_node(v):
    if v not in nodes:
        print(f'cant delete {v},becuse it not found')
    else:
        global node_count
        indexV = nodes.index(v)
        nodes.remove(v)
        node_count -= 1
        graph.pop(indexV)
        for i in graph:
            i.pop(indexV)

# in the case of undirected and unweighted
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(f'cant delete {v1},becuse it not found')
    elif v2 not in nodes:
        print(f'cant delete {v2},becuse it not found')
    else:
        indexV1 = nodes.index(v1)
        indexV2 = nodes.index(v2)
        graph[indexV1][indexV2] = 0
        graph[indexV2][indexV1] = 0

# # in the case of directed and unweighted
# def delete_edge(v1,v2):
#     if v1 not in nodes:
#         print(f'cant delete {v1},becuse it not found')
#     elif v2 not in nodes:
#         print(f'cant delete {v2},becuse it not found')
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = 0

# in the case of undirected and weighted
# def delete_edge(v1,v2):
#     if v1 not in nodes:
#         print(f'cant delete {v1},becuse it not found')
#     elif v2 not in nodes:
#         print(f'cant delete {v2},becuse it not found')
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = 0
#         graph[indexV2][indexV1] = 0

# in the case of directed and weighted
# def delete_edge(v1,v2):
#     if v1 not in nodes:
#         print(f'cant delete {v1},becuse it not found')
#     elif v2 not in nodes:
#         print(f'cant delete {v2},becuse it not found')
#     else:
#         indexV1 = nodes.index(v1)
#         indexV2 = nodes.index(v2)
#         graph[indexV1][indexV2] = 0
        

       

        
    





def printg(graph):
    for i in graph:
        print(i)


add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_vertex('A','B')
add_vertex('A','C')
# add_vertex('A','B',7)
# add_vertex('A','C',9)
delete_node('E')
delete_edge('A','C')
print(nodes)
print(graph)
print(node_count)
printg(graph)