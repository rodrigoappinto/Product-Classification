from src.DistilBertForClassification import DistilBertForClassification
from src.exceptions import ModelNotReadyException
from transformers import DistilBertTokenizer
from pathlib import Path
import logging
import torch

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


classes = [
    "All Electronics",
    "Amazon Fashion",
    "Amazon Home",
    "Arts, Crafts & Sewing",
    "Automotive",
    "Books",
    "Camera & Photo",
    "Cell Phones & Accessories",
    "Computers",
    "Digital Music",
    "Grocery",
    "Health & Personal Care",
    "Home Audio & Theater",
    "Industrial & Scientific",
    "Movies & TV",
    "Musical Instruments",
    "Office Products",
    "Pet Supplies",
    "Sports & Outdoors",
    "Tools & Home Improvement",
    "Toys & Games",
    "Video Games",
]

model: DistilBertForClassification = None
tokenizer: DistilBertTokenizer = None

pretrained_classifier_path = Path("data", "model", "Amazon_Product_Classifier.pth")


def on_init() -> tuple[DistilBertForClassification, DistilBertTokenizer]:
    global model, tokenizer
    try:
        device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

        model = DistilBertForClassification(num_classes=22)
        tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        
        model.load_state_dict(torch.load(pretrained_classifier_path, map_location=torch.device(device)))
        model.eval()

    except Exception as e:
        logger.error(f"Error loading model and tokenizer: {e}")
        return None, tokenizer

    return model, tokenizer


def preprocess_request(title, desc, features, brand) -> str:

    processed_request = (
        "Title: "
        + title
        + " [SEP] "
        + "Brand: "
        + brand
        + " [SEP] "
        + "Description: "
        + str(desc)
        + " [SEP] "
        + "Features: "
        + str(features)
    )

    tokenized_request = tokenizer(
        processed_request,
        return_tensors="pt",
        max_length=128,
        truncation=True,
    )

    return tokenized_request


def classify_product(title, desc, features, brand) -> str:

    processed_request = preprocess_request(title, desc, features, brand)  # brand)

    with torch.no_grad():
        pred = model(
            processed_request["input_ids"], processed_request["attention_mask"]
        )

    predicted_class_idx = torch.argmax(pred, dim=1)

    return classes[predicted_class_idx]
