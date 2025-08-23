import logging
import os
import time
from helpers.token_cleansing import TokenCleansing
from helpers.normalization import Normalizer
from utils.tokenutils import TokenUtils

logger = logging.getLogger("Token Cleansing")


class Preprocessor:
    def __init__(self, cfg):
        self.cfg = cfg
        self.token_utils = TokenUtils(cfg.model_name)
        self.normalizer = Normalizer()
        self.token_cleansing = TokenCleansing(self.token_utils)

    def process_file(self):
        start_time = time.perf_counter()  # start timer

        logger.info(f"Loading input: {self.cfg.input_file}")
        with open(self.cfg.input_file, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Normalize text
        normalized_text = self.normalizer.normalize(raw_text)

        # Cleanse tokens
        cleaned, removed = self.token_cleansing.cleanse(normalized_text)

        # Save cleaned Markdown
        output_path = self.cfg.output_file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        logger.info(f"Cleaned Markdown saved to: {output_path}")

        # Save removed tokens
        removed_path = os.path.join(os.path.dirname(output_path), "output_removed_tokens.md")
        with open(removed_path, "w", encoding="utf-8") as f:
            f.write(removed if removed else "")
        logger.info(f"Removed tokens saved to: {removed_path}")

        end_time = time.perf_counter()  # end timer
        duration = end_time - start_time

        logger.info(f"Pipeline finished successfully ✅ Time taken: {duration:.2f} seconds")
