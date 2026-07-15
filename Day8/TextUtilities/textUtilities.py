class TextUtilities:

    def word_count(self, text):
        return len(text.split())

    def unique_words(self, text, case_sensitive=True):
        words = text.split()

        if not case_sensitive:
            words = [word.lower() for word in words]

        duplicates = []
        for word in words:
            if words.count(word) > 1 and word not in duplicates:
                duplicates.append(word)

        if duplicates:
            return duplicates

        return list(dict.fromkeys(words))

    def reverse_string(self, text):
        return text[::-1]