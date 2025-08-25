import logging
from config.config import Config
from pipelines.pipeline import Preprocessor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - token_cleansing - %(levelname)s - %(message)s",
)

def main():
    cfg = Config()
    preprocessor = Preprocessor(cfg)

    # Load input
    with open(cfg.input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()

    logger = logging.getLogger("token_cleansing")
    logger.info("Starting token cleansing pipeline...")

    # Run pipeline
    cleaned_text = preprocessor.run(raw_text)

    # Save cleaned output
    with open(cfg.output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    logger.info(f"Pipeline finished. Output written to {cfg.output_file}")

if __name__ == "__main__":
    main()
