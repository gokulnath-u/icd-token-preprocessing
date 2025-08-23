import os


class Config:
    def __init__(self):
        self.input_file = os.getenv("INPUT_FILE", "Inputfiles/input.md")
        self.output_file = os.getenv("OUTPUT_FILE", "Outputfiles/output.md")
        self.model_name = os.getenv("MODEL_NAME", "microsoft/MediPhi-Clinical")
