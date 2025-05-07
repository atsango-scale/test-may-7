from graph_tool import Graph

def main():
    # Create a graph instance
    my_graph = Graph()

    # Add some nodes
    my_graph.add_node("Alice")
    my_graph.add_node("Bob")
    my_graph.add_node("Charlie")
    my_graph.add_node("David")

    # Add some edges with weights
    my_graph.add_edge("Alice", "Bob", 2)
    my_graph.add_edge("Alice", "Charlie", 1)
    my_graph.add_edge("Bob", "Charlie", 3)
    my_graph.add_edge("Bob", "David", 7)
    my_graph.add_edge("Charlie", "David", 4)

    # Display the graph
    print("Graph structure:")
    my_graph.display_graph()

if __name__ == "__main__":
    main() 