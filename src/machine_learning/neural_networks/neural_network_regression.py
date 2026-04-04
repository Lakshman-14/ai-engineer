"""
Neural Network Regression with TensorFlow

This module covers the fundamentals of building regression models using neural networks:
- Creating and visualizing data
- Understanding input/output shapes
- Building, compiling, and fitting models
- Improving and evaluating models
- Comparing experiments
- Saving and loading models

Regression: Predicting a number (e.g., house prices, coordinates, costs)
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.metrics import MeanAbsoluteError, MeanSquaredError


def print_tf_version():
    """Print TensorFlow version."""
    print(f"TensorFlow version: {tf.__version__}")


# =============================================================================
# PART 1: CREATING DATA
# =============================================================================

def create_simple_data():
    """
    Create simple linear data for regression.
    
    Returns:
        X: Features (numpy array)
        y: Labels (numpy array)
    """
    # y = X + 10 relationship
    X = np.array([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
    y = np.array([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])
    return X, y


def create_simple_data_tensors():
    """
    Create simple linear data as TensorFlow tensors.
    
    Returns:
        X: Features (tensor)
        y: Labels (tensor)
    """
    X = tf.constant([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
    y = tf.constant([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])
    return X, y


def create_bigger_dataset():
    """
    Create a larger dataset for more comprehensive training.
    
    Returns:
        X: Features from -100 to 96 (step 4)
        y: Labels (X + 10)
    """
    X = np.arange(-100, 100, 4)
    y = X + 10
    return X, y


def visualize_data(X, y, title="Data Visualization"):
    """
    Visualize features vs labels as scatter plot.
    
    Args:
        X: Features
        y: Labels
        title: Plot title
    """
    plt.figure(figsize=(10, 7))
    plt.scatter(X, y)
    plt.xlabel("X (Features)")
    plt.ylabel("y (Labels)")
    plt.title(title)
    plt.show()


# =============================================================================
# PART 2: INPUT AND OUTPUT SHAPES
# =============================================================================

def demo_input_output_shapes():
    """Demonstrate input and output shape concepts."""
    print("=" * 60)
    print("Input and Output Shapes Demo")
    print("=" * 60)
    
    # Example: House price prediction
    house_info = tf.constant(["bedroom", "bathroom", "garage"])
    house_price = tf.constant([939700])
    
    print(f"\nHouse info shape (3 features): {house_info.shape}")
    print(f"House price shape (1 output): {house_price.shape}")
    
    # Our simple data
    X, y = create_simple_data_tensors()
    
    # Single example shapes
    input_shape = X[0].shape
    output_shape = y[0].shape
    
    print(f"\nSingle input shape: {input_shape}")  # Scalar (no shape)
    print(f"Single output shape: {output_shape}")  # Scalar (no shape)
    print(f"\nX[0] = {X[0].numpy()}, y[0] = {y[0].numpy()}")
    print("We're trying to predict: given X, what is y?")


# =============================================================================
# PART 3: TRAIN/TEST SPLIT
# =============================================================================

def split_data(X, y, train_ratio=0.8):
    """
    Split data into training and test sets.
    
    Args:
        X: Features
        y: Labels
        train_ratio: Proportion of data for training
        
    Returns:
        X_train, y_train, X_test, y_test
    """
    split_idx = int(len(X) * train_ratio)
    X_train, y_train = X[:split_idx], y[:split_idx]
    X_test, y_test = X[split_idx:], y[split_idx:]
    
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    
    return X_train, y_train, X_test, y_test


def visualize_train_test_split(X_train, y_train, X_test, y_test):
    """Visualize training and test data."""
    plt.figure(figsize=(10, 7))
    plt.scatter(X_train, y_train, c='b', label='Training data')
    plt.scatter(X_test, y_test, c='g', label='Testing data')
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Training vs Test Data Split")
    plt.legend()
    plt.show()


# =============================================================================
# PART 4: MODEL BUILDING
# =============================================================================

def build_simple_model(input_shape=1):
    """
    Build a simple single-layer regression model.
    
    Args:
        input_shape: Shape of input features
        
    Returns:
        Compiled Keras model
    """
    tf.random.set_seed(42)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=[input_shape])
    ])
    
    model.compile(
        loss=tf.keras.losses.mae,
        optimizer=tf.keras.optimizers.SGD(),
        metrics=["mae"]
    )
    
    return model


def build_two_layer_model(input_shape=1):
    """
    Build a two-layer regression model.
    
    Args:
        input_shape: Shape of input features
        
    Returns:
        Compiled Keras model
    """
    tf.random.set_seed(42)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=[input_shape]),
        tf.keras.layers.Dense(1)
    ])
    
    model.compile(
        loss=tf.keras.losses.mae,
        optimizer=tf.keras.optimizers.SGD(),
        metrics=["mae"]
    )
    
    return model


def train_model(model, X_train, y_train, epochs=100, verbose=1):
    """
    Train a model on the given data.
    
    Args:
        model: Keras model
        X_train: Training features
        y_train: Training labels
        epochs: Number of training epochs
        verbose: Verbosity level
        
    Returns:
        Training history
    """
    # TensorFlow 2.7+ requires expanding dimensions
    X_expanded = tf.expand_dims(X_train, axis=-1)
    history = model.fit(X_expanded, y_train, epochs=epochs, verbose=verbose)
    return history


# =============================================================================
# PART 5: PREDICTIONS AND VISUALIZATION
# =============================================================================

def make_predictions(model, X_test):
    """
    Make predictions using the model.
    
    Args:
        model: Trained Keras model
        X_test: Test features
        
    Returns:
        Predictions array
    """
    return model.predict(X_test)


def plot_predictions(train_data, train_labels, test_data, test_labels, predictions):
    """
    Plot training data, test data, and predictions.
    
    Args:
        train_data: Training features
        train_labels: Training labels
        test_data: Test features
        test_labels: Test labels (ground truth)
        predictions: Model predictions
    """
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", label="Training data")
    plt.scatter(test_data, test_labels, c="g", label="Testing data")
    plt.scatter(test_data, predictions, c="r", label="Predictions")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Predictions vs Ground Truth")
    plt.legend()
    plt.show()


# =============================================================================
# PART 6: EVALUATION METRICS
# =============================================================================

def calculate_mae(y_true, y_pred):
    """
    Calculate Mean Absolute Error.
    
    Args:
        y_true: Ground truth values
        y_pred: Predicted values
        
    Returns:
        MAE value
    """
    mae_metric = MeanAbsoluteError()
    return mae_metric(y_true, tf.squeeze(y_pred)).numpy()


def calculate_mse(y_true, y_pred):
    """
    Calculate Mean Squared Error.
    
    Args:
        y_true: Ground truth values
        y_pred: Predicted values
        
    Returns:
        MSE value
    """
    mse_metric = MeanSquaredError()
    return mse_metric(y_true, tf.squeeze(y_pred)).numpy()


def calculate_mae_manual(y_true, y_pred):
    """Calculate MAE using TensorFlow operations."""
    return tf.reduce_mean(tf.abs(y_true - tf.squeeze(y_pred))).numpy()


def evaluate_model(model, X_test, y_test, y_preds):
    """
    Evaluate model performance with multiple metrics.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        y_preds: Model predictions
        
    Returns:
        Dictionary with metrics
    """
    # Model's built-in evaluation
    loss, mae_metric = model.evaluate(X_test, y_test, verbose=0)
    
    # Manual calculations
    mae = calculate_mae(y_test, y_preds)
    mse = calculate_mse(y_test, y_preds)
    
    print(f"Loss: {loss:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    
    return {"loss": loss, "mae": mae, "mse": mse}


# =============================================================================
# PART 7: MODEL COMPARISON EXPERIMENTS
# =============================================================================

def run_experiment(model_name, model, X_train, y_train, X_test, y_test, epochs=100):
    """
    Run a training experiment and return results.
    
    Args:
        model_name: Name for the experiment
        model: Keras model
        X_train, y_train: Training data
        X_test, y_test: Test data
        epochs: Training epochs
        
    Returns:
        Dictionary with experiment results
    """
    print(f"\n{'='*60}")
    print(f"Running experiment: {model_name}")
    print(f"{'='*60}")
    
    # Train the model
    train_model(model, X_train, y_train, epochs=epochs, verbose=0)
    
    # Make predictions
    y_preds = make_predictions(model, X_test)
    
    # Calculate metrics
    mae = calculate_mae(y_test, y_preds)
    mse = calculate_mse(y_test, y_preds)
    
    print(f"MAE: {mae:.4f}, MSE: {mse:.4f}")
    
    return {
        "model_name": model_name,
        "mae": mae,
        "mse": mse,
        "predictions": y_preds
    }


def compare_models(results_list):
    """
    Compare results from multiple experiments.
    
    Args:
        results_list: List of experiment result dictionaries
        
    Returns:
        DataFrame with comparison
    """
    comparison_data = [
        [r["model_name"], r["mae"], r["mse"]] 
        for r in results_list
    ]
    
    df = pd.DataFrame(comparison_data, columns=["Model", "MAE", "MSE"])
    print("\n" + "=" * 60)
    print("Model Comparison Results")
    print("=" * 60)
    print(df.to_string(index=False))
    
    # Find best model
    best_idx = df["MAE"].idxmin()
    print(f"\nBest model: {df.loc[best_idx, 'Model']} (MAE: {df.loc[best_idx, 'MAE']:.4f})")
    
    return df


# =============================================================================
# PART 8: SAVING AND LOADING MODELS
# =============================================================================

def save_model_keras(model, filepath="saved_model.keras"):
    """
    Save model in Keras format (.keras).
    
    Args:
        model: Keras model to save
        filepath: Path to save the model
    """
    model.save(filepath)
    print(f"Model saved to: {filepath}")


def save_model_h5(model, filepath="saved_model.h5"):
    """
    Save model in HDF5 format (.h5).
    
    Args:
        model: Keras model to save
        filepath: Path to save the model
    """
    model.save(filepath)
    print(f"Model saved to: {filepath}")


def load_model(filepath):
    """
    Load a saved model.
    
    Args:
        filepath: Path to the saved model
        
    Returns:
        Loaded Keras model
    """
    model = tf.keras.models.load_model(filepath)
    print(f"Model loaded from: {filepath}")
    return model


# =============================================================================
# MAIN DEMO FUNCTION
# =============================================================================

def demo_regression_workflow():
    """
    Demonstrate complete neural network regression workflow.
    """
    print_tf_version()
    
    # STEP 1: Create and visualize data
    print("\n" + "=" * 60)
    print("STEP 1: Creating Data")
    print("=" * 60)
    X, y = create_bigger_dataset()
    print(f"Created dataset with {len(X)} samples")
    print(f"X range: [{X.min()}, {X.max()}]")
    print(f"y range: [{y.min()}, {y.max()}]")
    print(f"Relationship: y = X + 10")
    
    # STEP 2: Understand shapes
    demo_input_output_shapes()
    
    # STEP 3: Split data
    print("\n" + "=" * 60)
    print("STEP 3: Splitting Data")
    print("=" * 60)
    X_train, y_train, X_test, y_test = split_data(X, y, train_ratio=0.8)
    
    # STEP 4: Run experiments
    print("\n" + "=" * 60)
    print("STEP 4: Running Model Experiments")
    print("=" * 60)
    
    results = []
    
    # Experiment 1: Simple model, 100 epochs
    model_1 = build_simple_model()
    result_1 = run_experiment("Model_1 (1 layer, 100 epochs)", 
                              model_1, X_train, y_train, X_test, y_test, 
                              epochs=100)
    results.append(result_1)
    
    # Experiment 2: Two-layer model, 100 epochs
    model_2 = build_two_layer_model()
    result_2 = run_experiment("Model_2 (2 layers, 100 epochs)", 
                              model_2, X_train, y_train, X_test, y_test, 
                              epochs=100)
    results.append(result_2)
    
    # Experiment 3: Two-layer model, 500 epochs
    model_3 = build_two_layer_model()
    result_3 = run_experiment("Model_3 (2 layers, 500 epochs)", 
                              model_3, X_train, y_train, X_test, y_test, 
                              epochs=500)
    results.append(result_3)
    
    # STEP 5: Compare results
    comparison_df = compare_models(results)
    
    # STEP 6: Demonstrate saving (using best model)
    print("\n" + "=" * 60)
    print("STEP 6: Saving Best Model")
    print("=" * 60)
    save_model_keras(model_2, "best_regression_model.keras")
    
    print("\n" + "=" * 60)
    print("Regression Workflow Complete!")
    print("=" * 60)
    
    return comparison_df


def quick_demo():
    """
    Quick demonstration of neural network regression.
    """
    print_tf_version()
    
    # Create simple data
    X, y = create_simple_data()
    print(f"\nSimple data: X = {X}")
    print(f"Labels: y = {y}")
    print("Pattern: y = X + 10")
    
    # Build and train model
    print("\nBuilding and training model...")
    tf.random.set_seed(42)
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1)
    ])
    model.compile(
        loss=tf.keras.losses.mae,
        optimizer=tf.keras.optimizers.SGD(),
        metrics=["mae"]
    )
    model.fit(tf.expand_dims(X, axis=-1), y, epochs=100, verbose=0)
    
    # Make prediction
    test_value = 17.0
    prediction = model.predict(np.array([[test_value]]), verbose=0)[0][0]
    expected = test_value + 10
    
    print(f"\nPrediction for X={test_value}:")
    print(f"  Predicted: {prediction:.2f}")
    print(f"  Expected:  {expected:.2f}")
    print(f"  Error:     {abs(prediction - expected):.2f}")


if __name__ == "__main__":
    print("=" * 60)
    print("Neural Network Regression with TensorFlow")
    print("=" * 60)
    
    # Run quick demo first
    print("\n--- Quick Demo ---")
    quick_demo()
    
    # Run full workflow
    print("\n\n--- Full Workflow Demo ---")
    demo_regression_workflow()
