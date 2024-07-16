# Movie Review Sentiment Analysis with Simple RNN
This project demonstrates the use of a Simple Recurrent Neural Network (SimpleRNN) to classify movie reviews as positive or negative. The classification is based on a threshold of 0.5, where a score above 0.5 indicates a positive review, and a score below 0.5 indicates a negative review.

### Project Overview
The goal of this project is to build a sentiment analysis model that can accurately predict the sentiment of movie reviews. We used the IMDb dataset, which contains 50,000 movie reviews labeled as either positive or negative. This dataset is widely used for binary sentiment classification tasks.

### Importance of SimpleRNN
Recurrent Neural Networks (RNNs) are powerful for processing sequences of data, making them particularly well-suited for tasks like natural language processing. Unlike traditional feedforward neural networks, RNNs have connections that form directed cycles, enabling them to maintain a 'memory' of previous inputs in the sequence.

### Why SimpleRNN?
Sequence Handling: SimpleRNN is capable of handling sequential data, making it ideal for text analysis where the order of words impacts the meaning.
Simplicity: As the name suggests, SimpleRNN is the simplest form of RNN, which makes it easier to understand and implement compared to more complex variants like LSTM or GRU.
Foundation for Learning: Understanding SimpleRNN provides a good foundation for learning more advanced RNN architectures.

## Implementation Details
### Data Loading and Preprocessing:

I have used the IMDb dataset from tensorflow.keras.datasets.
The reviews were tokenized and padded to ensure uniform input length.

### Model Architecture:

Embedding Layer: Converts word indices into dense vectors of fixed size.
SimpleRNN Layer: Processes the embedded sequences to capture temporal dependencies.
Dense Layer: A single neuron with a sigmoid activation function to output a probability score between 0 and 1.
Training:

The model was compiled using the Adam optimizer and binary cross-entropy loss function.
We used early stopping to prevent overfitting, monitoring the validation loss with a patience of 5 epochs.
Evaluation:

The model was evaluated on the test set to ensure its generalizability.

## Conclusion
This project highlights the utility of SimpleRNN for sentiment analysis. Despite its simplicity, SimpleRNN effectively captures the sequence of words in a review to predict its sentiment. This foundational understanding can be extended to more sophisticated models for improved performance.
