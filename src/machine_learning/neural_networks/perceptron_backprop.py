"""
Perceptron with Backpropagation and Gradient Descent

This module contains:
- Basic perceptron implementation
- Gradient Descent vs Backpropagation Demo (XOR problem)
"""

import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# Basic Perceptron Functions
# ==========================================

def weighted_sum(inputs, weights):
    """
    Sum function - calculates the weighted sum of inputs.
    """
    s = 0
    for i in range(len(inputs)):
        s += inputs[i] * weights[i]
    return s


def step_function(sum_value):
    """
    Step function - returns 1 if sum >= 1, else 0.
    """
    if sum_value >= 1:
        return 1
    return 0


# ==========================================
# Neural Network Helper Functions
# ==========================================

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """Derivative of sigmoid function."""
    return x * (1 - x)


# ==========================================
# Gradient Descent vs Backpropagation Demo
# ==========================================

def train_xor_network(lr=0.001, epochs=1000, plot_loss=True):
    """
    Demonstrates how backpropagation computes gradients
    and how gradient descent uses them to update weights.
    
    Solves the XOR problem using a simple neural network.
    
    Args:
        lr: Learning rate
        epochs: Number of training iterations
        plot_loss: Whether to plot the loss curve
    
    Returns:
        Final predictions and loss history
    """
    # Dataset (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # Initialize Weights
    np.random.seed(42)
    W1 = np.random.uniform(size=(2, 2))
    W2 = np.random.uniform(size=(2, 1))

    losses = []

    # Training Loop
    for epoch in range(epochs):
        # Forward pass
        hidden_input = np.dot(X, W1)
        hidden_output = sigmoid(hidden_input)

        final_input = np.dot(hidden_output, W2)
        final_output = sigmoid(final_input)

        # Loss (Mean Squared Error)
        loss = np.mean((y - final_output) ** 2)
        losses.append(loss)

        # --- Backpropagation (gradient calculation) ---
        error = y - final_output
        d_output = error * sigmoid_derivative(final_output)

        error_hidden = d_output.dot(W2.T)
        d_hidden = error_hidden * sigmoid_derivative(hidden_output)

        # --- Gradient Descent (weight update) ---
        W2 += hidden_output.T.dot(d_output) * lr
        W1 += X.T.dot(d_hidden) * lr

    # Results
    print("Final predictions after training:")
    print(final_output)

    # Plot Loss Curve
    if plot_loss:
        plt.plot(losses)
        plt.title("Loss Curve")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.show()

    return final_output, losses


if __name__ == "__main__":
    # Basic Perceptron Demo
    print("=" * 50)
    print("Basic Perceptron")
    print("=" * 50)
    inputs = [35, 25]
    weights = [-0.8, 0.1]
    
    print("Inputs:", inputs)
    print("Weights:", weights)
    
    s = weighted_sum(inputs, weights)
    print("Weighted Sum:", s)
    print("Step Function Output:", step_function(s))
    
    # XOR Network Demo
    print("\n" + "=" * 50)
    print("Gradient Descent vs Backpropagation Demo (XOR)")
    print("=" * 50)
    train_xor_network(lr=0.001, epochs=1000, plot_loss=True)
