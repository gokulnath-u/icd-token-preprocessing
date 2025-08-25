import os

class Config:
    def __init__(self):
        # IO paths
        self.input_file = os.getenv("INPUT_FILE", "Inputfiles/input.md")
        self.output_file = os.getenv("OUTPUT_FILE", "Outputfiles/output.md")

        # Tokenizer settings
        self.model_name = os.getenv("MODEL_NAME", "microsoft/MediPhi-Clinical")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "131072"))
