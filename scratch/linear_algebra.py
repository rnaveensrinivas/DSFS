from typing import List, Tuple, Callable

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Adds two vectors element-wise."""
    assert len(v) == len(w), "Vectors must be same length to be added."
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "Logical Error in add()"


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract two vectors element-wise."""
    assert len(v) == len(w), "Vectors must be same length to be subtracted."
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3], "Logical Error in subtract()"


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum all the vectors element-wise."""
    assert vectors, "No vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vectors are of different sizes!"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20], "Logical Error in vector_sum()"


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply every element of the vector by a scalar."""
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Compute the element-wise average of a list of vectors."""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4], "Logical Error in vector_mean()"


def dot(v: Vector, w: Vector) -> float:
    """Compute the dot product of two vectors."""
    assert len(v) == len(w), "Vectors must be the same size!"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32, "Logical Error in dot()"


def sum_of_squares(v: Vector) -> float:
    """Compute the sum of squares of each component in the vector."""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14, "Logical Error in sum_of_squares()"


def magnitude(v: Vector) -> float:
    """Return the magnitude (or length) of a given vector."""
    return sum_of_squares(v) ** 0.5


assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    """Compute the squared distance between two vectors."""
    assert len(v) == len(w), "Vectors must be the same length."
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Compute the distance between two vectors."""
    assert len(v) == len(w), "Vectors must be the same length."
    return magnitude(subtract(v, w))


Matrix = List[List[float]]

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns the (number of rows, number of columns) of a matrix."""
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of a matrix as a vector."""
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of a matrix as a vector."""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i, j)."""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns an n x n identity matrix."""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]