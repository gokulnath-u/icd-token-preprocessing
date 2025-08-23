import logging
from transformers import AutoTokenizer

logger = logging.getLogger("Token Cleansing")


class TokenUtils:
    def __init__(self, model_name: str):
        logger.info(f"Loading tokenizer for: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # HuggingFace models usually expose max_model_input_sizes
        self.max_length = min(
            self.tokenizer.model_max_length, 131072
        )  # Cap at 128k safe
        logger.info(f"Tokenizer loaded. Max tokens set to {self.max_length}")

    def encode(self, text: str):
        return self.tokenizer.encode(text, add_special_tokens=False)

    def decode(self, tokens: list[int]):
        return self.tokenizer.decode(tokens, skip_special_tokens=True)
