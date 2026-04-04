"""
Perceptron 1 - Basic Perceptron Implementation

Demonstrates the fundamental components of a perceptron:
- Inputs and weights
- Sum function (weighted sum)
- Step function (activation)
"""


def weighted_sum(inputs, weights):
    """
    Sum function - calculates the weighted sum of inputs.
    
    Args:
        inputs: List of input values
        weights: List of weight values
    
    Returns:
        Weighted sum of inputs
    """
    s = 0
    for i in range(len(inputs)):
        s += inputs[i] * weights[i]
    return s


def step_function(sum_value):
    """
    Step function - activation function that returns 1 if sum >= 1, else 0.
    
    Args:
        sum_value: The weighted sum to evaluate
    
    Returns:
        1 if sum_value >= 1, else 0
    """
    if sum_value >= 1:
        return 1
    return 0


def perceptron(inputs, weights):
    """
    Complete perceptron that combines weighted sum and step activation.
    
    Args:
        inputs: List of input values
        weights: List of weight values
    
    Returns:
        Binary output (0 or 1)
    """
    s = weighted_sum(inputs, weights)
    return step_function(s)


if __name__ == "__main__":
    # Inputs and weights
    inputs = [35, 25]
    weights = [-0.8, 0.1]
    
    print("Inputs:", inputs)
    print("Weights:", weights)
    
    # Calculate weighted sum
    s = weighted_sum(inputs, weights)
    print("\nWeighted Sum:", s)
    
    # Apply step function
    result = step_function(s)
    print("Step Function Output:", result)
    
    # Complete perceptron
    print("\nPerceptron Output:", perceptron(inputs, weights))
