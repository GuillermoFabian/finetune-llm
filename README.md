# Sentiment Analysis with Fine-tuned GPT-2

This project demonstrates the process of fine-tuning the GPT-2 model for sentiment analysis on movie reviews. Utilizing the IMDb dataset, we adjust GPT-2, a model originally designed for text generation, to classify text inputs into positive or negative sentiment categories. This README outlines the steps to prepare the data, fine-tune the model, evaluate its performance, and compare the fine-tuned model against the original GPT-2 model.

## Requirements

- Python 3.8 or later
- PyTorch
- Transformers library by Hugging Face
- Datasets library by Hugging Face
- Accelerate library for efficient training

## Installation

First, ensure that Python and pip are already installed. Then, install the necessary Python packages using the following command:

```bash
pip install torch transformers datasets accelerate
```

## Dataset
The IMDb dataset is used, comprising movie reviews labeled as either positive or negative. The dataset is split into training, validation, and test sets, with labels encoded as 0 (negative) and 1 (positive).

## Model Training and Evaluation
Data Preparation: Load the IMDb dataset and prepare it for training by tokenizing the text data and encoding the labels.

Model Fine-tuning: Utilize the Trainer class from the Transformers library to fine-tune the GPT-2 model on the sentiment analysis task.

Evaluation: Assess the performance of the fine-tuned model on the test dataset, calculating metrics such as accuracy, precision, recall, and F1 score.

Comparison: Compare the performance of the fine-tuned GPT-2 model against the original, pre-trained GPT-2 model to understand the impact of fine-tuning.

## Running the Code
To execute the project, run the Jupyter Notebook script provided, ensuring that the dataset path and other configurations are correctly set according to your environment.

## Visualization
The project includes code for visualizing the performance comparison between the original and fine-tuned models, showcasing the effectiveness of the fine-tuning process.

# Conclusion
This project highlights the adaptability of pre-trained models like GPT-2 for specific tasks such as sentiment analysis, demonstrating the power of fine-tuning in achieving significant improvements in model performance.

