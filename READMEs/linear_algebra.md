# Linear Algebra

Linear algebra is a foundational branch of mathematics that focuses on vector spaces and linear mappings between them. It is essential for numerous applications in science, engineering, and computer science.

---

## 1. **Vectors**

### **Abstract Definition of a Vector:**
Vectors are elements of a **vector space** $V$ over a field $F$, where the following operations are defined:

1. **Vector Addition**: A binary operation $+ : V \times V \to V$, such that for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$:
   - **Commutativity**: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
   - **Associativity**: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
   - **Existence of Zero Vector**: There exists a unique $\mathbf{0} \in V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$
   - **Existence of Additive Inverse**: For every $\mathbf{u} \in V$, there exists $-\mathbf{u} \in V$ such that $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$

2. **Scalar Multiplication**: A binary operation $\cdot : F \times V \to V$, such that for all $a, b \in F$ and $\mathbf{u}, \mathbf{v} \in V$:
   - **Distributivity over Vector Addition**: $a \cdot (\mathbf{u} + \mathbf{v}) = a \cdot \mathbf{u} + a \cdot \mathbf{v}$
   - **Distributivity over Scalar Addition**: $(a + b) \cdot \mathbf{u} = a \cdot \mathbf{u} + b \cdot \mathbf{u}$
   - **Compatibility with Scalar Multiplication**: $(ab) \cdot \mathbf{u} = a \cdot (b \cdot \mathbf{u})$
   - **Identity Element of Scalar Multiplication**: $1 \cdot \mathbf{u} = \mathbf{u}$, where $1$ is the multiplicative identity in $F$.


#### **Key Points:**
- The field $F$ is typically $\mathbb{R}$ (real numbers) or $\mathbb{C}$ (complex numbers), but it can be any field.
- The "abstract vector" definition does not rely on specific representations like arrows or tuples; instead, it focuses on the operations and their properties.

This abstraction unifies many structures in mathematics, including traditional geometric vectors, function spaces, and even polynomials.

---

### **Pragmatic Definition of a Vector:**
A vector is an ordered list of numbers, often used to represent quantities such as velocity, force, or position in space. 

The simplest approach for creating a vector in Python is using `List[float]`. Vectors, are usally represented as **column vectors**. 

```python

from typing import List
Vector = List[float]

petal_length: Vector = [
    9.23,
    2.58,
    7.98
]
```

Python Lists don't provide Vector operations, hence we will have to define our own. 

---

### **Operations on Vectors**
#### **1.1 Vector Addition**
- Vectors can be added component-wise.
- For two vectors $v = [v_1, v_2, \ldots, v_n]$ and $w = [w_1, w_2, \ldots, w_n]$, the sum is: $v + w = [v_1 + w_1, v_2 + w_2, \ldots, v_n + w_n]$
- **Example in Code:**
  ```python
  def add(v, w):
      return [v_i + w_i for v_i, w_i in zip(v, w)]
  ```

#### **1.2 Vector Subtraction**
- Subtraction is also component-wise.
  $
  v - w = [v_1 - w_1, v_2 - w_2, \ldots, v_n - w_n]
  $
- **Example in Code:**
  ```python
  def subtract(v, w):
      return [v_i - w_i for v_i, w_i in zip(v, w)]
  ```

#### **1.3 Scalar Multiplication**
- Multiplying a vector by a scalar scales each component by the scalar.
  $
  c \cdot v = [c \cdot v_1, c \cdot v_2, \ldots, c \cdot v_n]
  $
- **Example in Code:**
  ```python
  def scalar_multiply(c, v):
      return [c * v_i for v_i in v]
  ```

#### **1.4 Vector Mean**
- The component-wise mean of a list of vectors is calculated by averaging corresponding components.
  $
  \text{mean}([v_1, v_2, \ldots, v_m]) = \frac{1}{m} \cdot \text{sum}([v_1, v_2, \ldots, v_m])
  $
- **Example in Code:**
  ```python
  def vector_mean(vectors):
      return scalar_multiply(1 / len(vectors), vector_sum(vectors))
  ```

#### **1.5 Dot Product**
- The dot product $v.w$ tells you how much of $v$ lies in the direction of $w$ (via projection), scaled by the magnitude of $w$.



  $
  v \cdot w = \sum_{i=1}^n v_i \cdot w_i
  $
- **Example in Code:**
  ```python
  def dot_product(v, w):
      return sum(v_i * w_i for v_i, w_i in zip(v, w))
  ```

#### **1.6 Sum of Squares**
- The sum of squares of a vector is the dot product of the vector with itself.
  $
  \text{Sum of Squares}(v) = v \cdot v = \sum_{i=1}^n v_i^2
  $
- **Example in Code:**
  ```python
  def sum_of_squares(v):
      return dot_product(v, v)
  ```

#### **1.7 Magnitude**
- The magnitude (or length) of a vector is the square root of the sum of its squares.
  $
  \|v\| = \sqrt{v \cdot v}
  $
- **Example in Code:**
  ```python
  def magnitude(v):
      return sum_of_squares(v)**0.5
  ```

#### **1.8 Distance Between Two Vectors**
- The distance between two vectors is the magnitude of their difference.
  $
  \text{Distance}(v, w) = \|v - w\|
  $
- **Example in Code:**
  ```python
  def distance(v, w):
      return magnitude(subtract(v, w))
  ```

---

## 2. **Matrices**

### **Definition**
A matrix is a two-dimensional array of numbers arranged in rows and columns.

### **Operations on Matrices**
#### **2.1 Shape of a Matrix**
- The shape of a matrix is defined by its number of rows and columns.
  $
  \text{Shape}(A) = (\text{rows}, \text{columns})
  $
- **Example in Code:**
  ```python
  def shape(A):
      return len(A), len(A[0])
  ```

#### **2.2 Accessing Rows and Columns**
- **Row:**
  ```python
  def get_row(A, i):
      return A[i]
  ```
- **Column:**
  ```python
  def get_column(A, j):
      return [A_i[j] for A_i in A]
  ```

#### **2.3 Identity Matrix**
- An identity matrix is a square matrix with 1s on the diagonal and 0s elsewhere.
$$
I_{n \times n} = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}
$$

- **Example in Code:**
  ```python
  def identity_matrix(n):
      return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
  ```

---
