"""
Handwritten Digits Classification using Neural Network

This module classifies handwritten digits using TensorFlow/Keras.
- Simple neural network with no hidden layers
- Neural network with hidden layer
- Using Flatten layer for automatic reshaping

Dataset: MNIST (60,000 training images, 10,000 test images)
"""

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn


def load_and_preprocess_data():
    """
    Load MNIST dataset and preprocess it.
    
    Returns:
        X_train, y_train, X_test, y_test: Normalized datasets
        X_train_flattened, X_test_flattened: Flattened versions
    """
    # Load data
    (X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
    
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Image shape: {X_train[0].shape}")
    
    # Normalize pixel values to 0-1
    X_train = X_train / 255
    X_test = X_test / 255
    
    # Flatten for simple models
    X_train_flattened = X_train.reshape(len(X_train), 28 * 28)
    X_test_flattened = X_test.reshape(len(X_test), 28 * 28)
    
    print(f"Flattened shape: {X_train_flattened.shape}")
    
    return X_train, y_train, X_test, y_test, X_train_flattened, X_test_flattened


def visualize_sample(X_train, y_train, index=0):
    """Display a sample image from the dataset."""
    plt.matshow(X_train[index])
    plt.title(f"Label: {y_train[index]}")
    plt.show()


def build_simple_model():
    """
    Build a simple neural network with no hidden layers.
    Just input layer directly connected to output layer.
    """
    model = keras.Sequential([
        keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model


def build_model_with_hidden_layer():
    """
    Build a neural network with one hidden layer.
    Hidden layer has 100 neurons with ReLU activation.
    """
    model = keras.Sequential([
        keras.layers.Dense(100, input_shape=(784,), activation='relu'),
        keras.layers.Dense(10, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model


def build_model_with_flatten():
    """
    Build a neural network using Flatten layer.
    No need to manually reshape input data.
    """
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(100, activation='relu'),
        keras.layers.Dense(10, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model


def train_and_evaluate(model, X_train, y_train, X_test, y_test, epochs=5):
    """
    Train the model and evaluate on test data.
    
    Returns:
        Evaluation results (loss, accuracy)
    """
    model.fit(X_train, y_train, epochs=epochs)
    results = model.evaluate(X_test, y_test)
    return results


def predict_and_show_confusion_matrix(model, X_test, y_test):
    """
    Make predictions and display confusion matrix.
    """
    y_predicted = model.predict(X_test)
    y_predicted_labels = [np.argmax(i) for i in y_predicted]
    
    cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
    
    plt.figure(figsize=(10, 7))
    sn.heatmap(cm, annot=True, fmt='d')
    plt.xlabel('Predicted')
    plt.ylabel('Truth')
    plt.title('Confusion Matrix')
    plt.show()
    
    return y_predicted_labels


def main():
    """Run the complete digit recognition pipeline."""
    
    # Load data
    print("=" * 50)
    print("Loading MNIST Dataset")
    print("=" * 50)
    X_train, y_train, X_test, y_test, X_train_flattened, X_test_flattened = load_and_preprocess_data()
    
    # Visualize a sample
    visualize_sample(X_train, y_train, index=0)
    
    # Model 1: Simple model (no hidden layers)
    print("\n" + "=" * 50)
    print("Model 1: Simple Neural Network (No Hidden Layers)")
    print("=" * 50)
    model1 = build_simple_model()
    train_and_evaluate(model1, X_train_flattened, y_train, X_test_flattened, y_test, epochs=5)
    predict_and_show_confusion_matrix(model1, X_test_flattened, y_test)
    
    # Model 2: With hidden layer
    print("\n" + "=" * 50)
    print("Model 2: Neural Network with Hidden Layer")
    print("=" * 50)
    model2 = build_model_with_hidden_layer()
    train_and_evaluate(model2, X_train_flattened, y_train, X_test_flattened, y_test, epochs=5)
    predict_and_show_confusion_matrix(model2, X_test_flattened, y_test)
    
    # Model 3: Using Flatten layer
    print("\n" + "=" * 50)
    print("Model 3: Neural Network with Flatten Layer")
    print("=" * 50)
    model3 = build_model_with_flatten()
    train_and_evaluate(model3, X_train, y_train, X_test, y_test, epochs=10)
    

if __name__ == "__main__":
    main()
