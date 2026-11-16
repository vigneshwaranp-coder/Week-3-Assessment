# Week 3 Assessment – AI/ML Workflow Engineering

## Project Overview

This repository contains my Week 3 assessment, covering Neural Networks, PyTorch, Natural Language Processing (NLP), Transformers, and FastAPI.

The objective was to understand fundamental AI/ML concepts and apply them through practical coding exercises.

## Topics Covered

### 1. Neural Network Fundamentals
- XOR neural network implementation.
- Activation functions: ReLU, Sigmoid and Softmax.
- Loss functions and gradient calculations.
- Learning rate experiments.
- Dropout, Batch Normalization and Early Stopping.

### 2. PyTorch Training Pipeline
- Dataset preparation and preprocessing.
- Custom PyTorch Dataset and DataLoader.
- Building and training an MLP model.
- Validation and Early Stopping.
- Model saving and loading.
- Comparison with Logistic Regression.

### 3. Natural Language Processing (NLP)
- Text preprocessing and cleaning.
- TF-IDF with Logistic Regression.
- Accuracy, Macro F1 and Confusion Matrix.
- Word2Vec embeddings.
- Sentence vector generation and comparison.

### 4. Transformers and FastAPI
- DistilBERT tokenization.
- Sentiment Analysis and Named Entity Recognition (NER).
- Fine-tuning DistilBERT using the Hugging Face Trainer API.
- Model evaluation and comparison.
- FastAPI prediction endpoint.
- API testing with Swagger UI.

### 5. BERT vs GPT
- Understanding encoder-based and decoder-based Transformer architectures.
- Use cases of BERT and GPT.

## Technologies Used

- Python 3.12
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch
- Hugging Face Transformers
- Gensim
- FastAPI
- Uvicorn
- Jupyter Notebook
- Git and GitHub

## Project Files

| File / Folder | Description |
|---|---|
| `week3.ipynb` | Main assessment notebook |
| `app.py` | FastAPI sentiment prediction application |
| `.gitignore` | Excludes model files and unnecessary files |

## How to Run

1. Clone this repository.
2. Install the required Python packages.
3. Open `week3.ipynb` in VS Code or Jupyter Notebook.
4. Run the notebook cells to train and save the required models.
5. Make sure the fine-tuned DistilBERT model is saved in the `sentiment_model` folder.
6. Start the API using:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

7. Open the Swagger UI:

```text
http://127.0.0.1:8000/docs
```

8. Test the POST `/predict` endpoint.

**Note:** Model artifacts are excluded from this GitHub repository. Run the relevant notebook cells to generate them locally before starting the API.

## Learning Outcome

Through this assessment, I gained practical experience with neural networks, PyTorch model training, NLP techniques, Transformer models, model evaluation, and deploying a machine learning model using FastAPI.
