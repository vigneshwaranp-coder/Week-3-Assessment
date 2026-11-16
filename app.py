
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline

app = FastAPI()

# Load the saved model only once
sentiment_model = pipeline(
    "text-classification",
    model="./sentiment_model",
    tokenizer="./sentiment_model"
)

class TextRequest(BaseModel):
    text: str = Field(min_length=1)

@app.post("/predict")
def predict(request: TextRequest):
    result = sentiment_model(request.text)[0]

    label = "POSITIVE" if result["label"] == "LABEL_1" else "NEGATIVE"

    return {
        "label": label,
        "confidence": round(result["score"], 4)
    }
