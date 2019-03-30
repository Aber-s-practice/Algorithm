from datastruct.graph import GraphNode, DirectedGraph

import random

graph = DirectedGraph()
nodes = [GraphNode(i) for i in range(10)]
for x_node in nodes:
    for y_node in nodes:
        graph.set_relation(x_node, y_node, random.randint(0, 23))

print(graph)
