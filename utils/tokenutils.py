def count_tokens(text: str, tokenizer) -> int:
    """Utility to count tokens for debugging."""
    return len(tokenizer.tokenize(text))
