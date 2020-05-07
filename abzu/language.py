import abzu.utils
import abzu.kiss

class Language:
    def __init__(self):
        self.name = None
        self.vocab = {}

    # TODO: proper concept generation, etc.
    def add_words(self, num_words, seed=None):

        words = abzu.kiss.random_words(num_words, {}, seed=seed)
        for idx, word in enumerate(words):
            self.vocab[f"concept-{idx+1}"] = word
