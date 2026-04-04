"""
Deep Learning Advanced - Multi-Layer Perceptron and Gradient Descent

This module contains:
- LAB 1: Single Layer Perceptron (Manual)
- LAB 2: Change weights and bias
- LAB 3: Activation Functions Comparison
- LAB 4: Multi-Layer Perceptron (Manual)
- LAB 5: Gradient Descent (Simple)

Formula:
z = w1*x1 + w2*x2+....wn*xn + b
f(z) -- Activation --- step function, relu, sigmoid
"""

import numpy as np


def lab1_single_layer_perceptron():
    """
    LAB 1: Single Layer Perceptron (Manual)
    """
    print("LAB 1: Single Layer Perceptron (Manual)")
    print("-" * 40)
    
    # Inputs
    X = np.array([2, 3])

    # Weights
    W = np.array([0.5, 0.5])

    # Bias
    b = 1

    # Weighted sum
    z = np.dot(X, W) + b

    # Activation (Step Function)
    output = 1 if z > 0 else 0

    print("Weighted Sum:", z)
    print("Output:", output)
    
    return z, output


def lab2_change_weights_and_bias():
    """
    LAB 2: Change weights and bias
    """
    print("\nLAB 2: Change weights and bias")
    print("-" * 40)
    
    X = np.array([2, 3])

    # Try different weights
    W = np.array([1, -1])
    b = -1

    z = np.dot(X, W) + b

    output = 1 if z > 0 else 0

    print("z:", z)
    print("Output:", output)
    
    return z, output


def lab3_activation_functions():
    """
    LAB 3: Compare activation functions
    """
    print("\nLAB 3: Activation Functions")
    print("-" * 40)
    
    z = 2.5

    # Step
    step = 1 if z > 0 else 0

    # Sigmoid
    sigmoid = 1 / (1 + np.exp(-z))

    # ReLU
    relu = max(0, z)

    print(f"Input z: {z}")
    print("Step:", step)
    print("Sigmoid:", round(sigmoid, 3))
    print("ReLU:", relu)
    
    return step, sigmoid, relu


def lab4_multi_layer_perceptron():
    """
    LAB 4: Multi-Layer Perceptron (Manual)
    """
    print("\nLAB 4: Multi-Layer Perceptron (Manual)")
    print("-" * 40)
    
    # Input
    X = np.array([1, 2])

    # Hidden layer weights
    W1 = np.array([[0.5, 0.2],
                   [0.3, 0.7]])

    b1 = np.array([0.1, 0.1])

    # Output layer weights
    W2 = np.array([0.6, 0.9])
    b2 = 0.1

    # Forward pass

    # Hidden layer
    z1 = np.dot(X, W1) + b1
    a1 = 1 / (1 + np.exp(-z1))  # sigmoid

    # Output layer
    z2 = np.dot(a1, W2) + b2
    output = 1 / (1 + np.exp(-z2))

    print("Hidden Output:", a1)
    print("Final Output:", output)
    
    return a1, output


def lab5_gradient_descent_simple():
    """
    LAB 5: Gradient Descent (Simple)
    """
    print("\nLAB 5: Gradient Descent (Simple)")
    print("-" * 40)
    
    # Initial weight
    w = 5

    # Learning rate
    lr = 0.1

    # Target value
    target = 2

    for i in range(10):
        # Prediction
        y = w

        # Loss (MSE)
        loss = (y - target) ** 2

        # Gradient
        grad = 2 * (y - target)

        # Update weight
        w = w - lr * grad

        print(f"Step {i}: w={round(w, 2)}, loss={round(loss, 2)}")
    
    return w


if __name__ == "__main__":
    print("=" * 50)
    print("Deep Learning Labs")
    print("=" * 50)
    
    lab1_single_layer_perceptron()
    lab2_change_weights_and_bias()
    lab3_activation_functions()
    lab4_multi_layer_perceptron()
    lab5_gradient_descent_simple()
