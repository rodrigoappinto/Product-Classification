from http import HTTPStatus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomHTTPException(Exception):
    status_code: int
    response_body: dict[str, any]

    def __init__(self, status_code: int, response_body: dict[str, any]) -> None:
        self.status_code = status_code
        self.response_body = response_body


class ModelNotReadyException(CustomHTTPException):
    def __init__(self):
        super().__init__(
            HTTPStatus.SERVICE_UNAVAILABLE,
            {
                "error": {
                    "title": "Model or Tokenizer are not ready.",
                    "detail": "Please check if the model and the tokenizer are loaded correctly.",
                }
            },
        )
