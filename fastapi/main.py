from src.exceptions import ModelNotReadyException
from src.items import ProductClassificationItem
from fastapi.responses import JSONResponse
from src.model_helper import on_init, classify_product as product_classification
from fastapi import FastAPI
from http import HTTPStatus

import uvicorn
import logging

app = FastAPI()

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


@app.get("/health")
def health_check() -> JSONResponse:
    if not model or not tokenizer:
        raise ModelNotReadyException()

    return JSONResponse(
        content={"Model and Tokenizer are Alive": True}, status_code=HTTPStatus.OK
    )


@app.post("/classify_product")
def classify_product(item: ProductClassificationItem) -> JSONResponse:

    title = item.title
    description = item.description
    features = item.features
    brand = item.brand

    result = product_classification(title, description, features, brand)

    return JSONResponse(
        content={"This product's category is: ": result}, status_code=HTTPStatus.OK
    )


if __name__ == "__main__":
    model, tokenizer = on_init()
    uvicorn(app, host="0.0.0.0", port=8080)
else:
    model, tokenizer = on_init()
