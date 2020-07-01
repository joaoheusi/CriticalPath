import networkx as nx

g = nx.DiGraph()

""" g.add_nodes_from(['A','B','C','D','E','F','G'])

g.add_weighted_edges_from([('A','B',14),
                           ('B','C',20),
                           ('B','D',20),
                           ('C','D',3),
                           ('D','E',8),
                           ('D','F',13),
                           ('E','F',11),
                           ('F','G',20)])      
"""


nodeList = ['1','2','3','4','5','6','Fim']
weightsList = [10,4,7,5,5,2,0]
predecessorsList = [[],['1'],['1'],['3'],['2','4'],['3'],['5','6']]


def addNodes(graph,nodeList= nodeList):
    try:
        graph.add_nodes_from(nodeList)
        return True
    except:
        print('Erro ao adicionar vértices')
        return False

def addEdges(graph,nodeList = nodeList, weightsList = weightsList,predecessorsList=predecessorsList):
    for i,individualPredecessors in enumerate(predecessorsList):
        node = nodeList[i]
        for predecessor in individualPredecessors:
            graph.add_edge(predecessor,node, weight = weightsList[nodeList.index(predecessor)])


def path_weight(graph,path):
    weight = 0
    for i,node in enumerate(path):
        if (i+1) in range(len(path)):
            weight += graph.get_edge_data(path[i],path[i+1]).get('weight')
    return weight

def take_second(elem):
    return elem[1]

def critical_path(graph,paths):
    paths_and_weights = []
    for path in paths:
        paths_and_weights.append((path,path_weight(graph,path)))

    paths_and_weights.sort(key=take_second,reverse=True)
    return paths_and_weights[0]

def find_gaps(graph,paths):
    paths_and_weights = []
    for path in paths:
        paths_and_weights.append((path,path_weight(graph,path)))

    paths_and_weights.sort(key=take_second,reverse=True)

    gaps = []
    for i,path in enumerate(paths_and_weights):
        if i != 0:
            gap = set(paths_and_weights[0][0]) - set(paths_and_weights[i][0])
            gap_value = paths_and_weights[0][1] - paths_and_weights[i][1]
            gaps.append([gap,gap_value])

    for i,gap in enumerate(gaps):
        for x,gap in enumerate(gaps):
            if i != x:
                a_set = set(gaps[i][0])
                b_set = set(gaps[x][0])
                if(a_set & b_set):
                    gaps[i][0] = a_set - (a_set & b_set)
                    gaps[x][0] = b_set - (a_set & b_set)

    return gaps


addNodes(g)
addEdges(g)


""" print(list(g.nodes())) """

paths = [path for path in nx.all_simple_paths(g,'1','Fim')]


print(critical_path(g,paths))
print(find_gaps(g,paths))
print(paths)

""" for edge in g.edges():
    print(edge)
    print(g.get_edge_data(edge[0],edge[1]))
"""