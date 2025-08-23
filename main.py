import logging
import os
from utils.config import Config
from pipelines.pipeline import Preprocessor

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("Token Cleansing")


def main():
    cfg = Config()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(cfg.output_file), exist_ok=True)

    # Run pipeline
    preprocessor = Preprocessor(cfg)
    preprocessor.process_file()


if __name__ == "__main__":
    main()
