import numpy as np
import pytest

from ranking import as_markov_matrix, calculate_rank, discrete_uniform


def test_discrete_uniform():
    result = discrete_uniform(4)
    assert np.allclose(result, [0.25, 0.25, 0.25, 0.25])


def test_markov_matrix_handles_dangling_node():
    adjacency = np.array([[0, 1], [0, 0]], dtype=float)
    markov = as_markov_matrix(adjacency)
    assert np.allclose(markov.sum(axis=0), [1.0, 1.0])


def test_rank_returns_descending_scores():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }
    result = calculate_rank(graph)
    scores = [score for _, score in result]

    assert scores == sorted(scores, reverse=True)
    assert np.isclose(sum(scores), 1.0)


def test_unknown_target_raises_error():
    with pytest.raises(ValueError):
        calculate_rank({"A": ["missing"]})
