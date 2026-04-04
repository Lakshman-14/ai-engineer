"""
Small Image Classification Using Convolutional Neural Network (CNN)

This module classifies images from the CIFAR-10 dataset using both:
- Artificial Neural Network (ANN) - baseline comparison
- Convolutional Neural Network (CNN) - improved accuracy

CIFAR-10 Dataset:
- 50,000 training images
- 10,000 test images
- 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
- Image size: 32x32x3 (RGB)

Key Concepts:
- Conv2D layers for feature extraction
- MaxPooling2D for dimensionality reduction
- Flattening for dense layer input
- Softmax for multi-class classification
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report


# CIFAR-10 class labels
CLASSES = ["airplane", "automobile", "bird", "cat", "deer", 
           "dog", "frog", "horse", "ship", "truck"]


def load_cifar10_data():
    """
    Load and preprocess the CIFAR-10 dataset.
    
    Returns:
        X_train, y_train, X_test, y_test: Preprocessed data
    """
    print("Loading CIFAR-10 dataset...")
    (X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Test data shape: {X_test.shape}")
    print(f"Training labels shape: {y_train.shape}")
    
    # Reshape labels to 1D array
    y_train = y_train.reshape(-1,)
    y_test = y_test.reshape(-1,)
    
    print(f"Labels reshaped to 1D: {y_train.shape}")
    
    return X_train, y_train, X_test, y_test


def normalize_data(X_train, X_test):
    """
    Normalize image pixel values from 0-255 to 0-1.
    
    Args:
        X_train: Training images
        X_test: Test images
        
    Returns:
        Normalized X_train, X_test
    """
    print("Normalizing data (0-255 -> 0-1)...")
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    return X_train, X_test


def plot_sample(X, y, index, show=True):
    """
    Plot a sample image with its label.
    
    Args:
        X: Image array
        y: Labels array
        index: Index of image to plot
        show: Whether to display the plot
    """
    plt.figure(figsize=(15, 2))
    plt.imshow(X[index])
    plt.xlabel(CLASSES[y[index]])
    plt.title(f"Sample Image - Class: {CLASSES[y[index]]}")
    if show:
        plt.show()


def plot_multiple_samples(X, y, num_samples=10):
    """
    Plot multiple sample images in a grid.
    
    Args:
        X: Image array
        y: Labels array
        num_samples: Number of samples to plot
    """
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    axes = axes.flatten()
    
    for i in range(num_samples):
        axes[i].imshow(X[i])
        axes[i].set_title(CLASSES[y[i]])
        axes[i].axis('off')
    
    plt.suptitle("CIFAR-10 Sample Images", fontsize=14)
    plt.tight_layout()
    plt.show()


def build_ann_model():
    """
    Build a simple Artificial Neural Network (ANN) for comparison.
    
    Architecture:
    - Flatten: 32x32x3 -> 3072
    - Dense: 3000 neurons, ReLU
    - Dense: 1000 neurons, ReLU
    - Dense: 10 neurons, Softmax (output)
    
    Returns:
        Compiled ANN model
    """
    print("\n" + "="*60)
    print("Building ANN Model (Baseline)")
    print("="*60)
    
    ann = models.Sequential([
        layers.Flatten(input_shape=(32, 32, 3)),
        layers.Dense(3000, activation='relu'),
        layers.Dense(1000, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    ann.compile(
        optimizer='SGD',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    ann.summary()
    return ann


def build_cnn_model():
    """
    Build a Convolutional Neural Network (CNN) for image classification.
    
    Architecture:
    - Conv2D: 32 filters, 3x3 kernel, ReLU
    - MaxPooling2D: 2x2
    - Conv2D: 64 filters, 3x3 kernel, ReLU
    - MaxPooling2D: 2x2
    - Conv2D: 128 filters, 3x3 kernel, ReLU
    - MaxPooling2D: 2x2
    - Flatten
    - Dense: 64 neurons, ReLU
    - Dense: 10 neurons, Softmax (output)
    
    Returns:
        Compiled CNN model
    """
    print("\n" + "="*60)
    print("Building CNN Model")
    print("="*60)
    
    cnn = models.Sequential([
        # First Convolutional Block
        layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', 
                      input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        
        # Second Convolutional Block
        layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Third Convolutional Block
        layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Dense Layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    cnn.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    cnn.summary()
    return cnn


def train_model(model, X_train, y_train, epochs=5, model_name="Model"):
    """
    Train a model on the training data.
    
    Args:
        model: Keras model to train
        X_train: Training images
        y_train: Training labels
        epochs: Number of training epochs
        model_name: Name for display purposes
        
    Returns:
        Training history
    """
    print(f"\nTraining {model_name} for {epochs} epochs...")
    history = model.fit(X_train, y_train, epochs=epochs, verbose=1)
    return history


def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Evaluate model performance on test data.
    
    Args:
        model: Trained Keras model
        X_test: Test images
        y_test: Test labels
        model_name: Name for display purposes
        
    Returns:
        Dictionary with evaluation metrics
    """
    print(f"\n{'='*60}")
    print(f"Evaluating {model_name}")
    print("="*60)
    
    # Model evaluation
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Predictions
    y_pred = model.predict(X_test, verbose=0)
    y_pred_classes = [np.argmax(element) for element in y_pred]
    
    # Classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_classes, target_names=CLASSES))
    
    return {
        "loss": loss,
        "accuracy": accuracy,
        "predictions": y_pred_classes
    }


def compare_predictions(X_test, y_test, y_pred_classes, num_samples=5):
    """
    Compare predictions with actual labels.
    
    Args:
        X_test: Test images
        y_test: Actual labels
        y_pred_classes: Predicted classes
        num_samples: Number of samples to display
    """
    print(f"\nComparing {num_samples} predictions:")
    print("-" * 40)
    
    for i in range(num_samples):
        actual = CLASSES[y_test[i]]
        predicted = CLASSES[y_pred_classes[i]]
        match = "✓" if actual == predicted else "✗"
        print(f"Sample {i}: Actual={actual:12} | Predicted={predicted:12} {match}")


def demo_ann_vs_cnn():
    """
    Demonstrate the difference between ANN and CNN for image classification.
    """
    print("="*60)
    print("CIFAR-10 Image Classification: ANN vs CNN")
    print("="*60)
    
    # Load and preprocess data
    X_train, y_train, X_test, y_test = load_cifar10_data()
    X_train, X_test = normalize_data(X_train, X_test)
    
    # Build and train ANN (baseline)
    ann = build_ann_model()
    train_model(ann, X_train, y_train, epochs=5, model_name="ANN")
    ann_results = evaluate_model(ann, X_test, y_test, model_name="ANN")
    
    # Build and train CNN
    cnn = build_cnn_model()
    train_model(cnn, X_train, y_train, epochs=10, model_name="CNN")
    cnn_results = evaluate_model(cnn, X_test, y_test, model_name="CNN")
    
    # Compare results
    print("\n" + "="*60)
    print("COMPARISON SUMMARY")
    print("="*60)
    print(f"ANN Accuracy: {ann_results['accuracy']*100:.2f}%")
    print(f"CNN Accuracy: {cnn_results['accuracy']*100:.2f}%")
    print(f"Improvement:  {(cnn_results['accuracy'] - ann_results['accuracy'])*100:.2f}%")
    
    # Show some predictions
    compare_predictions(X_test, y_test, cnn_results['predictions'], num_samples=10)
    
    return ann, cnn, ann_results, cnn_results


def quick_demo():
    """
    Quick demonstration using only CNN with fewer epochs.
    """
    print("="*60)
    print("Quick CNN Demo - CIFAR-10 Classification")
    print("="*60)
    
    # Load and preprocess data
    X_train, y_train, X_test, y_test = load_cifar10_data()
    X_train, X_test = normalize_data(X_train, X_test)
    
    # Build and train CNN
    cnn = build_cnn_model()
    train_model(cnn, X_train, y_train, epochs=3, model_name="CNN")
    
    # Evaluate
    results = evaluate_model(cnn, X_test, y_test, model_name="CNN")
    
    # Show predictions
    compare_predictions(X_test, y_test, results['predictions'], num_samples=5)
    
    return cnn, results


if __name__ == "__main__":
    print("CIFAR-10 Image Classification with CNN")
    print("="*60)
    print("\nRunning quick demo (3 epochs for faster execution)...")
    print("For full comparison, call demo_ann_vs_cnn()\n")
    
    cnn, results = quick_demo()
