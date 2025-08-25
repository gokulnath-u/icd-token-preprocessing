import logging
import time
from transformers import AutoTokenizer

logger = logging.getLogger("token_cleansing")

class TokenCleansing:
    def __init__(self, model_name: str, max_tokens: int):
        start = time.perf_counter()
        logger.info(f"Loading tokenizer for: {model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.max_tokens = max_tokens

        end = time.perf_counter()
        logger.info(
            f"Tokenizer loaded. Max tokens set to {self.max_tokens}. "
            f"Load time: {end - start:.2f} sec"
        )

    def cleanse(self, text: str):
        start_time = time.perf_counter()

        tokens = self.tokenizer.tokenize(text)
        total_tokens = len(tokens)
        removed_tokens = []

        if total_tokens > self.max_tokens:
            removed_tokens = tokens[self.max_tokens:]
            tokens = tokens[: self.max_tokens]

        cleaned = self.tokenizer.convert_tokens_to_string(tokens)
        removed = self.tokenizer.convert_tokens_to_string(removed_tokens)

        kept_count = len(tokens)
        removed_count = len(removed_tokens)

        end_time = time.perf_counter()
        duration = end_time - start_time

        logger.info(
            f"Token cleansing completed → Total: {total_tokens}, "
            f"Kept: {kept_count}, Removed: {removed_count}, "
            f"Time taken: {duration:.2f} sec"
        )

        return cleaned, removed
