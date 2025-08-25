# 🧼 ICD Token Cleansing Pipeline

A preprocessing pipeline for cleaning and normalizing text using HuggingFace tokenizers and Wordninja.  
It is designed for text with glued words and large token sequences, such as medical ICD notes.

---

## 🚀 Features

- Load input text from a file.
- Clean tokens using a HuggingFace tokenizer (removes tokens beyond a maximum token limit).
- Normalize glued words (e.g., `yourparents` → `your parents`) using Wordninja.
- Save outputs:
  - `output.md` → cleaned & normalized text
  - `output_removed_tokens.md` → tokens removed beyond the limit

---

## ⚙️ Configuration

Set these environment variables or rely on the defaults:

| Variable      | Default                      | Description                          |
|---------------|------------------------------|--------------------------------------|
| `INPUT_FILE`  | `Inputfiles/input.md`        | Path to input Markdown/text file     |
| `OUTPUT_FILE` | `Outputfiles/output.md`      | Path to save cleaned text            |
| `MODEL_NAME`  | `microsoft/MediPhi-Clinical` | HuggingFace model for tokenization   |
| `MAX_TOKENS`  | `131072`                     | Maximum number of tokens to keep     |

---

## ▶️ Running the Pipeline

```bash
python main.py

📦 Requirements

pip install transformers wordninja torch

📁 Output Files

output.md → cleaned and Wordninja-normalized text

output_removed_tokens.md → tokens removed due to exceeding MAX_TOKENS

📝 Example

Input (input.md):

yourparentsshouldknowaboutthis


Output (output.md):

your parents should know about this
