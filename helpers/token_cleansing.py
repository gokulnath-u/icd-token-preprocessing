import logging
import time
from utils.tokenutils import TokenUtils

logger = logging.getLogger("Token Cleansing")


class TokenCleansing:
    def __init__(self, token_utils: TokenUtils):
        self.token_utils = token_utils

    def cleanse(self, text: str):
        """
        Cleanses text by keeping as many paragraphs as possible within
        the tokenizer's max length. Remaining paragraphs are moved to
        'removed' output.
        Also logs token counts and time taken.
        """

        start_time = time.perf_counter()  # start timer for cleansing

        # Tokenize full input once to get total tokens
        all_tokens = self.token_utils.encode(text)
        total_tokens = len(all_tokens)

        # Split into paragraphs
        paragraphs = text.split("\n\n")
        kept_sections = []
        removed_sections = []

        token_count = 0
        limit = self.token_utils.max_length

        for paragraph in paragraphs:
            if not paragraph.strip():
                continue  # skip empty lines/paragraphs

            tokens = self.token_utils.encode(paragraph)
            paragraph_len = len(tokens)

            if token_count + paragraph_len <= limit:
                kept_sections.append(paragraph)
                token_count += paragraph_len
            else:
                removed_sections.append(paragraph)

        cleaned_text = "\n\n".join(kept_sections)
        removed_text = "\n\n".join(removed_sections)

        removed_count = total_tokens - token_count

        end_time = time.perf_counter()  # end timer
        duration = end_time - start_time

        logger.info(f"Token cleansing completed ")
        logger.info(f"Total tokens: {total_tokens}, Kept: {token_count}, Removed: {removed_count}")
        logger.info(f"Time taken for cleansing: {duration:.2f} seconds")

        return cleaned_text, removed_text
