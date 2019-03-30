class GraphNode:

    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return f"[{self.data}]"


class DirectedGraph:
    """有向图"""

    def __init__(self):
        self.__relationship = {}

    def __str__(self):
        nodes = [each for each in self.__relationship.keys()]
        s = 'Graph\t'
        for node in nodes:
            s += (str(node) + "\t")
        else:
            s += "\r\n"
        for x_node in nodes:
            s += (str(x_node) + "\t")
            for y_node in nodes:
                s += (str(self.get_relation(x_node, y_node)) + "\t")
            s += '\r\n'
        return s

    def set_relation(self, x: GraphNode, y: GraphNode, side):
        if self.__relationship.get(x) is None:
            self.__relationship[x] = {}
        self.__relationship[x][y] = side

    def get_relation(self, x: GraphNode, y: GraphNode):
        if self.__relationship.get(x) is not None and self.__relationship[x].get(y) is not None:
            return self.__relationship[x][y]
        return None
