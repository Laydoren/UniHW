class Word:
    def __init__(self, word):
        if not isinstance(word, str) or not word.isalpha() or not word:
            raise ValueError("Word must be any sequence of one or more Latin letters")
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        if not self.word:
            return ""
        return self.word[0].upper() + self.word[1:].lower()


    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) == len(other.word)

    def __ne__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) != len(other.word)

    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) < len(other.word)

    def __le__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) <= len(other.word)

    def __gt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) > len(other.word)

    def __ge__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) >= len(other.word)


word1 = Word("python")
word2 = Word("abba")
word3 = Word("FBKI")


print(repr(word1))
print(word1)
print(word3)
print(repr(word2))

print("")

print(f"python == abba: {word1 == word2}")
print(f"python != abba: {word1 != word2}")
print(f"python > abba: {word1 > word2}")
print(f"python < abba: {word1 < word2}")
print(f"abba == FBKI: {word2 == word3}")
print(f"abba != FBKI: {word2 != word3}")
print(f"abba >= FBKI: {word2 >= word3}")

print(f"word1 > 'string': {word1 > 'string'}")

