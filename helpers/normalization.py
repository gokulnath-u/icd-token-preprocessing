class Normalizer:
    def normalize(self, text: str) -> str:
        """
        Basic normalization:
        - Strip trailing spaces
        - Normalize line breaks
        """
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = "\n".join([line.rstrip() for line in text.split("\n")])
        return text
