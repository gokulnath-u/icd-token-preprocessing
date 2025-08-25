import os
import logging
from helpers.token_cleansing import TokenCleansing
from helpers.normalization import Normalizer

logger = logging.getLogger("token_cleansing")

class Preprocessor:
    def __init__(self, cfg):
        self.cfg = cfg
        self.token_cleanser = TokenCleansing(cfg.model_name, cfg.max_tokens)
        self.normalizer = Normalizer()

    def run(self, text: str) -> str:
        # Step 1: Token cleansing
        cleaned, removed = self.token_cleanser.cleanse(text)

        # Step 2: Wordninja normalization (keep this exactly as is ✅)
        normalized = self.normalizer.normalize(cleaned)

        # Step 3: Save removed tokens
        removed_path = self.cfg.output_file.replace(".md", "_removed_tokens.md")
        os.makedirs(os.path.dirname(removed_path) or ".", exist_ok=True)
        with open(removed_path, "w", encoding="utf-8") as f:
            f.write(removed if removed else "")

        logger.info(f"Removed tokens saved to {removed_path}")

        return normalized
