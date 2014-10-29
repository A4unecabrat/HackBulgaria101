class DirectedGraph:

    def __init__(self):
        self.edges = {}

    def addEdge(self, nodeA, nodeB):

        if nodeA in self.edges:
            if nodeB not in self.edges[nodeA]:
                self.edges[nodeA].append(nodeB)
        else:
            self.edges[nodeA] = [nodeB]

    def getNeighborsFor(self, node):
        return self.edges[node]

    def pathBetween(self, nodeA, nodeB, path=[]):
        if path != []:
            raise ValueError("ebi se v guza")
        path = path + [nodeA]
        if nodeB in self.edges[nodeA]:
            return True
        if nodeA not in self.edges:
            return False
        for node in self.edges[nodeA]:
            if node not in path:
                newpath = self.pathBetween(node, nodeB, path)
                if newpath:
                    return newpath
        return False

    def toString(self):
        for key in self.edges:
            print(key + ":" + str(",".join(self.edges[key])))
