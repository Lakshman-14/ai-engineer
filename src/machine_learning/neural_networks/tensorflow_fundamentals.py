"""
TensorFlow Fundamentals

This module covers the fundamental concepts of TensorFlow:
- Introduction to tensors (creating tensors)
- Getting information from tensors (tensor attributes)
- Manipulating tensors (tensor operations)
- Tensors and NumPy
- Matrix multiplication and dot products
- Aggregation operations

What is TensorFlow?
- Open-source end-to-end machine learning library
- Turn data into numbers (tensors) and build ML algorithms to find patterns

Tensor Types:
- Scalar: rank 0 tensor (single number)
- Vector: rank 1 tensor (1D array)
- Matrix: rank 2 tensor (2D array)
- Tensor: rank n tensor (nD array)
"""

import datetime
import numpy as np
import tensorflow as tf


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ============================================================
# SECTION 1: Creating Tensors with tf.constant()
# ============================================================

def demo_tensor_creation():
    """Demonstrate creating different types of tensors."""
    print_section("Creating Tensors with tf.constant()")
    
    # Create a scalar (rank 0 tensor)
    scalar = tf.constant(7)
    print(f"Scalar: {scalar}")
    print(f"Scalar ndim: {scalar.ndim}")
    
    # Create a vector (rank 1 tensor)
    vector = tf.constant([10, 10])
    print(f"\nVector: {vector}")
    print(f"Vector ndim: {vector.ndim}")
    
    # Create a matrix (rank 2 tensor)
    matrix = tf.constant([[10, 7],
                          [7, 10]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Matrix ndim: {matrix.ndim}")
    
    # Create a matrix with specified dtype
    another_matrix = tf.constant([[10., 7.],
                                  [3., 2.],
                                  [8., 9.]], dtype=tf.float16)
    print(f"\nMatrix with float16 dtype:\n{another_matrix}")
    print(f"Another matrix ndim: {another_matrix.ndim}")
    
    # Create a 3D tensor
    tensor = tf.constant([[[1, 2, 3],
                           [4, 5, 6]],
                          [[7, 8, 9],
                           [10, 11, 12]],
                          [[13, 14, 15],
                           [16, 17, 18]]])
    print(f"\n3D Tensor:\n{tensor}")
    print(f"Tensor ndim: {tensor.ndim}")
    
    return scalar, vector, matrix, tensor


# ============================================================
# SECTION 2: tf.Variable() vs tf.constant()
# ============================================================

def demo_variable_vs_constant():
    """Demonstrate the difference between Variable and constant."""
    print_section("tf.Variable() vs tf.constant()")
    
    # tf.Variable - mutable (can be changed)
    changeable_tensor = tf.Variable([10, 7])
    # tf.constant - immutable (cannot be changed)
    unchangeable_tensor = tf.constant([10, 7])
    
    print(f"Changeable tensor (Variable): {changeable_tensor}")
    print(f"Unchangeable tensor (constant): {unchangeable_tensor}")
    
    # Change element using assign()
    changeable_tensor[0].assign(7)
    print(f"\nAfter assign(7) to index 0: {changeable_tensor}")
    
    # This would error: unchangeable_tensor[0].assign(7)
    print("Note: tf.constant() tensors cannot be changed!")


# ============================================================
# SECTION 3: Random Tensors
# ============================================================

def demo_random_tensors():
    """Demonstrate creating random tensors with seeds."""
    print_section("Random Tensors")
    
    # Create random tensors with same seed (reproducible)
    random_1 = tf.random.Generator.from_seed(42)
    random_1 = random_1.normal(shape=(3, 2))
    
    random_2 = tf.random.Generator.from_seed(42)
    random_2 = random_2.normal(shape=(3, 2))
    
    print("Random tensor 1 (seed=42):")
    print(random_1)
    print("\nRandom tensor 2 (seed=42):")
    print(random_2)
    print(f"\nAre they equal? {tf.reduce_all(random_1 == random_2).numpy()}")
    
    # Different seed = different values
    random_3 = tf.random.Generator.from_seed(11)
    random_3 = random_3.normal(shape=(3, 2))
    print(f"\nRandom tensor 3 (seed=11) - Different values:")
    print(random_3)


def demo_shuffle():
    """Demonstrate shuffling tensors."""
    print_section("Shuffling Tensors")
    
    not_shuffled = tf.constant([[10, 7],
                                [3, 4],
                                [2, 5]])
    print(f"Original tensor:\n{not_shuffled}")
    
    # Set global and operation seed for reproducible shuffle
    tf.random.set_seed(42)
    shuffled = tf.random.shuffle(not_shuffled, seed=42)
    print(f"\nShuffled tensor (with seeds):\n{shuffled}")


# ============================================================
# SECTION 4: Other Ways to Create Tensors
# ============================================================

def demo_ones_zeros_numpy():
    """Demonstrate tf.ones(), tf.zeros(), and NumPy conversion."""
    print_section("tf.ones(), tf.zeros(), NumPy conversion")
    
    # Tensor of ones
    ones = tf.ones(shape=(3, 2))
    print(f"Tensor of ones:\n{ones}")
    
    # Tensor of zeros
    zeros = tf.zeros(shape=(3, 2))
    print(f"\nTensor of zeros:\n{zeros}")
    
    # NumPy array to tensor
    numpy_A = np.arange(1, 25, dtype=np.int32)
    A = tf.constant(numpy_A, shape=[2, 4, 3])
    print(f"\nNumPy array: {numpy_A}")
    print(f"\nConverted to tensor with shape [2, 4, 3]:\n{A}")


# ============================================================
# SECTION 5: Getting Tensor Information
# ============================================================

def demo_tensor_info():
    """Demonstrate getting tensor attributes."""
    print_section("Getting Tensor Information")
    
    # Create a rank 4 tensor
    rank_4_tensor = tf.zeros([2, 3, 4, 5])
    
    print(f"Datatype of every element: {rank_4_tensor.dtype}")
    print(f"Number of dimensions (rank): {rank_4_tensor.ndim}")
    print(f"Shape of tensor: {rank_4_tensor.shape}")
    print(f"Elements along axis 0: {rank_4_tensor.shape[0]}")
    print(f"Elements along last axis: {rank_4_tensor.shape[-1]}")
    print(f"Total number of elements (2*3*4*5): {tf.size(rank_4_tensor).numpy()}")


# ============================================================
# SECTION 6: Basic Tensor Operations
# ============================================================

def demo_basic_operations():
    """Demonstrate basic tensor operations."""
    print_section("Basic Tensor Operations")
    
    tensor = tf.constant([[10, 7], [3, 4]])
    print(f"Original tensor:\n{tensor}")
    
    # Addition
    print(f"\nTensor + 10:\n{tensor + 10}")
    
    # Multiplication (element-wise)
    print(f"\nTensor * 10:\n{tensor * 10}")
    
    # Subtraction
    print(f"\nTensor - 10:\n{tensor - 10}")
    
    # Using TensorFlow function
    print(f"\ntf.multiply(tensor, 10):\n{tf.multiply(tensor, 10)}")
    
    # Original unchanged (immutable)
    print(f"\nOriginal tensor (unchanged):\n{tensor}")


# ============================================================
# SECTION 7: Matrix Multiplication
# ============================================================

def demo_matrix_multiplication():
    """Demonstrate matrix multiplication rules and methods."""
    print_section("Matrix Multiplication")
    
    print("Rules for matrix multiplication:")
    print("1. Inner dimensions must match: (a, b) @ (b, c) -> (a, c)")
    print("2. Result has shape of outer dimensions")
    
    tensor = tf.constant([[10, 7], [3, 4]])
    print(f"\nTensor (2x2):\n{tensor}")
    
    # Matrix multiplication with tf.matmul()
    result = tf.matmul(tensor, tensor)
    print(f"\ntf.matmul(tensor, tensor):\n{result}")
    
    # Using @ operator
    print(f"\ntensor @ tensor:\n{tensor @ tensor}")
    
    # Mismatched shapes example
    print("\n--- Handling Mismatched Shapes ---")
    X = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])  # Shape (3, 2)
    Y = tf.constant([[7, 8],
                     [9, 10],
                     [11, 12]])  # Shape (3, 2)
    
    print(f"X shape: {X.shape}, Y shape: {Y.shape}")
    print("X @ Y would fail - inner dimensions don't match!")
    
    # Using reshape
    print(f"\nX @ tf.reshape(Y, (2,3)) = (3,2) @ (2,3) -> (3,3):")
    print(X @ tf.reshape(Y, shape=(2, 3)))
    
    # Using transpose
    print(f"\ntf.transpose(X) @ Y = (2,3) @ (3,2) -> (2,2):")
    print(tf.matmul(tf.transpose(X), Y))


def demo_reshape_vs_transpose():
    """Demonstrate the difference between reshape and transpose."""
    print_section("Reshape vs Transpose")
    
    Y = tf.constant([[7, 8],
                     [9, 10],
                     [11, 12]])
    
    print(f"Original Y:\n{Y}")
    print(f"\ntf.reshape(Y, (2, 3)) - fills in order:")
    print(tf.reshape(Y, (2, 3)))
    print(f"\ntf.transpose(Y) - swaps axes:")
    print(tf.transpose(Y))
    
    print("\nKey Difference:")
    print("- reshape(): Changes shape, fills values in order")
    print("- transpose(): Swaps the axes (rows become columns)")


def demo_dot_product():
    """Demonstrate dot product with tf.tensordot()."""
    print_section("Dot Product with tf.tensordot()")
    
    X = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])
    Y = tf.constant([[7, 8],
                     [9, 10],
                     [11, 12]])
    
    result = tf.tensordot(tf.transpose(X), Y, axes=1)
    print(f"tf.tensordot(tf.transpose(X), Y, axes=1):\n{result}")


# ============================================================
# SECTION 8: Changing Datatype
# ============================================================

def demo_type_casting():
    """Demonstrate changing tensor datatypes."""
    print_section("Changing Datatype with tf.cast()")
    
    B = tf.constant([1.7, 7.4])
    print(f"Original B (float32): {B}")
    
    # Cast to float16 (reduced precision)
    B_float16 = tf.cast(B, dtype=tf.float16)
    print(f"B as float16: {B_float16}")
    
    C = tf.constant([1, 7])
    print(f"\nOriginal C (int32): {C}")
    
    # Cast to float32
    C_float32 = tf.cast(C, dtype=tf.float32)
    print(f"C as float32: {C_float32}")


# ============================================================
# SECTION 9: Absolute Values
# ============================================================

def demo_absolute():
    """Demonstrate getting absolute values."""
    print_section("Absolute Values with tf.abs()")
    
    D = tf.constant([-7, -10])
    print(f"Original D: {D}")
    print(f"tf.abs(D): {tf.abs(D)}")


# ============================================================
# SECTION 10: Aggregation Functions
# ============================================================

def demo_aggregation():
    """Demonstrate aggregation functions."""
    print_section("Aggregation Functions")
    
    # Create random tensor
    np.random.seed(42)
    E = tf.constant(np.random.randint(low=0, high=100, size=50))
    print(f"Random tensor E (first 10): {E[:10].numpy()}")
    
    print(f"\ntf.reduce_min(E): {tf.reduce_min(E).numpy()}")
    print(f"tf.reduce_max(E): {tf.reduce_max(E).numpy()}")
    print(f"tf.reduce_mean(E): {tf.reduce_mean(E).numpy()}")
    print(f"tf.reduce_sum(E): {tf.reduce_sum(E).numpy()}")
    
    # argmax
    F = tf.constant(np.random.random(10))
    print(f"\nTensor F: {F.numpy()}")
    print(f"tf.argmax(F) (index of max): {tf.argmax(F).numpy()}")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """Run all demonstrations."""
    print(f"Notebook last run: {datetime.datetime.now()}")
    print(f"TensorFlow version: {tf.__version__}")
    
    # Run all demos
    demo_tensor_creation()
    demo_variable_vs_constant()
    demo_random_tensors()
    demo_shuffle()
    demo_ones_zeros_numpy()
    demo_tensor_info()
    demo_basic_operations()
    demo_matrix_multiplication()
    demo_reshape_vs_transpose()
    demo_dot_product()
    demo_type_casting()
    demo_absolute()
    demo_aggregation()
    
    print_section("EXERCISES")
    print("""
    1. Create a vector, scalar, matrix and tensor with values of your choosing using tf.constant()
    2. Find the shape, rank and size of the tensors you created in 1
    3. Create two tensors containing random values between 0 and 1 with shape [5, 300]
    4. Multiply the two tensors you created in 3 using matrix multiplication
    5. Multiply the two tensors you created in 3 using dot product
    6. Create a tensor with random values between 0 and 1 with shape [224, 224, 3]
    7. Find the min and max values of the tensor you created in 6
    8. Create a tensor with random values of shape [1, 224, 224, 3] then squeeze it to [224, 224, 3]
    9. Create a tensor with shape [10] using your own choice of values, then find the index with max value
    10. One-hot encode the tensor you created in 9
    """)


if __name__ == "__main__":
    main()
