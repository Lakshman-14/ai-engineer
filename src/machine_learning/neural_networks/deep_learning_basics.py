"""
Deep Learning Basics - Single Layer Perceptron

Formula:
z = w1*x1 + w2*x2+....wn*xn + b
f(z) -- Activation --- step function, relu, sigmoid
This is single neuron decision
"""

import numpy as np


def single_layer_perceptron_manual():
    """
    LAB 1: Single Layer Perceptron (Manual)
    Demonstrates basic perceptron with weighted sum and step activation.
    """
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


def perceptron_with_different_weights():
    """
    LAB 2: Change weights and bias
    Demonstrates how different weights and bias affect the output.
    """
    X = np.array([2, 3])

    # Try different weights
    W = np.array([1, -1])
    b = -1

    z = np.dot(X, W) + b

    output = 1 if z > 0 else 0

    print("z:", z)
    print("Output:", output)
    
    return z, output


if __name__ == "__main__":
    print("=" * 50)
    print("LAB 1: Single Layer Perceptron (Manual)")
    print("=" * 50)
    single_layer_perceptron_manual()
    
    print("\n" + "=" * 50)
    print("LAB 2: Change weights and bias")
    print("=" * 50)
    perceptron_with_different_weights()
