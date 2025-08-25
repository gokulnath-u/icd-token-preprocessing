import wordninja

class Normalizer:
    def normalize(self, text: str) -> str:
        """
        Fix glued words like 'yourparents' -> 'your parents'
        while keeping structure (line breaks, bullets).
        """
        normalized_lines = []
        for line in text.splitlines():
            words = line.split()
            fixed_words = []
            for word in words:
                if len(word) > 12:  # heuristic: long glued words
                    split = wordninja.split(word)
                    fixed_words.extend(split)
                else:
                    fixed_words.append(word)
            normalized_lines.append(" ".join(fixed_words))
        return "\n".join(normalized_lines)
