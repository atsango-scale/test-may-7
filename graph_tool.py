class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        # Ensure both nodes exist in the graph
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)
        
        # Add the edge (and its reverse for an undirected graph)
        # For a directed graph, only the first part would be needed.
        # Storing as a tuple (neighbor, weight)
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight)) # Assuming undirected graph

    def display_graph(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

if __name__ == '__main__':
    # Basic test
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_edge("A", "B", 5)
    g.add_edge("B", "C", 3)
    g.add_edge("A", "C", 10)
    g.display_graph() 