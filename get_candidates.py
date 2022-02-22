import itertools
import nltk
import sys


def all_words():
     _vocab = set(w.lower() for w in nltk.corpus.words.words())
     return _vocab


def search_space(_beehive, _vocab):
    test_lengths = [4,5,6,7,8,9]
    if len(_beehive) != 7:
        print('Not enough letters!')
        sys.exit()
    else:
        center_letter = _beehive[-1]
        for j in test_lengths:
            holder = [_beehive] * j
            cands = list(itertools.product(*holder))
            for k in cands:
                if center_letter in k:
                    if ''.join(list(k)) in _vocab:
                        print(''.join(list(k)))


if __name__ == "__main__":
    beehive = ['h', 'l', 'i', 'c', 'd', 'e', 'k']
    vocab = all_words()
    search_space(beehive, vocab)
