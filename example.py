"""Small example showing how to rank a directed graph."""

from ranking import calculate_rank


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["A"],
        "D": ["C"],
    }

    for node, score in calculate_rank(graph):
        print(f"{node}: {score:.4f}")
