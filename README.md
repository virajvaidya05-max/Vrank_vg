# Graph Ranking with PageRank

A clean Python implementation of **PageRank-style graph ranking** using an iterative Markov-chain approach.

The project takes a directed graph, converts it into a stochastic transition matrix, handles dangling nodes, and iteratively computes a stable probability distribution that can be used to rank the nodes.

## Features

- Directed-graph ranking with PageRank
- Handles dangling nodes
- Sparse matrix support during iteration
- Configurable damping factor, tolerance, and iteration limit
- Input validation with useful errors
- Logging for convergence debugging
- Unit tests with `pytest`

## Project structure

```text
.
├── ranking.py
├── example.py
├── requirements.txt
├── tests/
│   └── test_ranking.py
├── .gitignore
└── README.md
```

## Installation

Clone the repository and install the dependencies:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
python -m venv .venv
```

Activate the virtual environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Then:

```bash
pip install -r requirements.txt
```

## Usage

Run the included example:

```bash
python example.py
```

Example graph:

```python
from ranking import calculate_rank

graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": ["C"],
}

ranking = calculate_rank(graph)

for node, score in ranking:
    print(node, score)
```

`calculate_rank()` returns a list of `(node, score)` pairs ordered from highest score to lowest.

## Parameters

```python
calculate_rank(
    graph,
    damp=0.85,
    eps=1e-4,
    max_iter=50,
)
```

- `graph`: directed graph represented as `{node: [outgoing_nodes]}`
- `damp`: probability of following graph links
- `eps`: convergence tolerance
- `max_iter`: maximum number of iterations

## How it works

1. The graph is converted into an adjacency matrix.
2. Nodes without outgoing edges are treated as dangling nodes and connected uniformly.
3. The adjacency matrix is normalized into a Markov transition matrix.
4. The algorithm starts with a uniform probability distribution.
5. Each iteration combines random jumping with following graph links.
6. Iteration stops when the distribution changes by less than `eps`, or `max_iter` is reached.
7. Nodes are returned in descending order of their final scores.

## Running tests

```bash
pytest -q
```

## Notes

The implementation is intended as an educational and reusable example of graph ranking with NumPy and SciPy.

## License

This project is released under the MIT License. See `LICENSE`.
