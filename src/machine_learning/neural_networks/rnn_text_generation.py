"""
Simple RNN Text Generation with TensorFlow

This module demonstrates text generation using a Recurrent Neural Network (RNN):
- Tokenization and sequence preparation
- Building an Embedding + SimpleRNN model
- Next word prediction for text generation

Key Concepts:
- Tokenizer: Converts text to numerical sequences
- Embedding Layer: Learns word representations
- SimpleRNN: Processes sequential data with memory
- Text Generation: Predicts next words iteratively
"""

import tensorflow as tf
import numpy as np


def create_training_corpus():
    """
    Create a simple training corpus.
    
    Returns:
        List of training documents
    """
    docs = [
        "go india",
        "india will win", 
        "hip hip hooray",
        "bharat mata jai"
    ]
    return docs


def tokenize_text(docs):
    """
    Tokenize text documents into numerical sequences.
    
    Args:
        docs: List of text documents
        
    Returns:
        tokenizer: Fitted Keras tokenizer
        sequences: List of tokenized sequences
    """
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(docs)
    sequences = tokenizer.texts_to_sequences(docs)
    
    print("Vocabulary:")
    for word, idx in tokenizer.word_index.items():
        print(f"  '{word}': {idx}")
    print(f"\nTotal vocabulary size: {len(tokenizer.word_index)}")
    
    return tokenizer, sequences


def prepare_training_data(sequences):
    """
    Prepare input-output pairs for next word prediction.
    
    For each sequence, creates pairs where:
    - X: All words up to position i
    - y: The word at position i (next word to predict)
    
    Args:
        sequences: List of tokenized sequences
        
    Returns:
        X: Padded input sequences
        y: Target words (next word to predict)
    """
    X = []
    y = []
    
    for seq in sequences:
        for i in range(1, len(seq)):
            X.append(seq[:i])
            y.append(seq[i])
    
    # Pad sequences to same length
    X = tf.keras.preprocessing.sequence.pad_sequences(X, padding='pre')
    y = np.array(y)
    
    print(f"\nTraining pairs created: {len(X)}")
    print(f"Input sequence shape: {X.shape}")
    print(f"Max sequence length: {X.shape[1]}")
    
    return X, y


def build_rnn_model(vocab_size, input_length, embedding_dim=10, rnn_units=50):
    """
    Build a simple RNN model for text generation.
    
    Architecture:
    - Embedding Layer: Converts word indices to dense vectors
    - SimpleRNN: Processes sequences with recurrent connections
    - Dense Layer: Outputs probability distribution over vocabulary
    
    Args:
        vocab_size: Size of vocabulary (+1 for padding)
        input_length: Maximum sequence length
        embedding_dim: Dimension of embedding vectors
        rnn_units: Number of RNN units
        
    Returns:
        Compiled RNN model
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=input_length),
        tf.keras.layers.SimpleRNN(rnn_units),
        tf.keras.layers.Dense(vocab_size, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model


def train_model(model, X, y, epochs=200, verbose=0):
    """
    Train the RNN model.
    
    Args:
        model: Keras model
        X: Input sequences
        y: Target words
        epochs: Number of training epochs
        verbose: Verbosity level
        
    Returns:
        Training history
    """
    print(f"\nTraining model for {epochs} epochs...")
    history = model.fit(X, y, epochs=epochs, verbose=verbose)
    print(f"Final loss: {history.history['loss'][-1]:.4f}")
    return history


def generate_text(model, tokenizer, seed_text, max_sequence_length, next_words=4):
    """
    Generate text by predicting next words.
    
    Args:
        model: Trained RNN model
        tokenizer: Fitted tokenizer
        seed_text: Starting text
        max_sequence_length: Maximum sequence length for padding
        next_words: Number of words to generate
        
    Returns:
        Generated text string
    """
    result = seed_text
    
    for _ in range(next_words):
        # Tokenize current text
        seq = tokenizer.texts_to_sequences([result])[0]
        
        # Pad to expected length
        seq = tf.keras.preprocessing.sequence.pad_sequences(
            [seq], maxlen=max_sequence_length, padding='pre'
        )
        
        # Predict next word
        pred = np.argmax(model.predict(seq, verbose=0))
        
        # Convert prediction to word
        word = tokenizer.index_word.get(pred, '')
        
        if word:
            result += " " + word
    
    return result


def demo_rnn_text_generation():
    """
    Demonstrate RNN text generation workflow.
    """
    print("=" * 60)
    print("RNN Text Generation Demo")
    print("=" * 60)
    
    # Step 1: Create corpus
    print("\nStep 1: Creating training corpus")
    docs = create_training_corpus()
    print(f"Training documents: {docs}")
    
    # Step 2: Tokenize
    print("\nStep 2: Tokenizing text")
    tokenizer, sequences = tokenize_text(docs)
    print(f"Sequences: {sequences}")
    
    # Step 3: Prepare training data
    print("\nStep 3: Preparing training data")
    X, y = prepare_training_data(sequences)
    
    # Step 4: Build model
    print("\nStep 4: Building RNN model")
    vocab_size = len(tokenizer.word_index) + 1
    model = build_rnn_model(vocab_size, X.shape[1])
    model.summary()
    
    # Step 5: Train model
    print("\nStep 5: Training model")
    train_model(model, X, y, epochs=200, verbose=0)
    
    # Step 6: Generate text
    print("\nStep 6: Generating text")
    print("-" * 40)
    
    test_seeds = ["india", "go", "hip", "bharat"]
    for seed in test_seeds:
        generated = generate_text(model, tokenizer, seed, X.shape[1], next_words=3)
        print(f"Seed: '{seed}' -> Generated: '{generated}'")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
    
    return model, tokenizer


def quick_demo():
    """
    Quick demonstration matching the original notebook.
    """
    print("=" * 60)
    print("Quick RNN Text Generation")
    print("=" * 60)
    
    # Training corpus
    docs = ["go india", "india will win", "hip hip hooray", "bharat mata jai"]
    
    # Tokenize
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(docs)
    sequences = tokenizer.texts_to_sequences(docs)
    
    # Prepare training data
    X = []
    y = []
    for seq in sequences:
        for i in range(1, len(seq)):
            X.append(seq[:i])
            y.append(seq[i])
    
    X = tf.keras.preprocessing.sequence.pad_sequences(X, padding='pre')
    y = np.array(y)
    
    # Build model
    vocab_size = len(tokenizer.word_index) + 1
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, 10, input_length=X.shape[1]),
        tf.keras.layers.SimpleRNN(50),
        tf.keras.layers.Dense(vocab_size, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
    print("Training RNN model (200 epochs)...")
    model.fit(X, y, epochs=200, verbose=0)
    
    # Generate text
    print("\nText Generation Results:")
    print("-" * 40)
    
    seed_text = "india"
    result = seed_text
    for _ in range(4):
        seq = tokenizer.texts_to_sequences([result])[0]
        seq = tf.keras.preprocessing.sequence.pad_sequences([seq], maxlen=X.shape[1], padding='pre')
        pred = np.argmax(model.predict(seq, verbose=0))
        word = tokenizer.index_word[pred]
        result += " " + word
    
    print(f"Input: '{seed_text}'")
    print(f"Output: '{result}'")
    
    return model, tokenizer


if __name__ == "__main__":
    print("Simple RNN Text Generation with TensorFlow")
    print("=" * 60)
    
    # Run quick demo
    model, tokenizer = quick_demo()
    
    print("\n\nFor detailed demo, call demo_rnn_text_generation()")
