import itertools
import nltk
import sys

from wordfreq import zipf_frequency


def all_words():
     _vocab = set(w.lower() for w in nltk.corpus.words.words())
     return _vocab


def search_space(_beehive, _vocab):
    test_lengths = [4, 5, 6, 7, 8, 9]
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
                        _w = ''.join(list(k))
                        score = zipf_frequency(_w, 'en')
                        if score > 0.0:
                            print('{}: {}'.format(_w, score))


if __name__ == "__main__":
    beehive = ['e', 'j', 'o', 'c', 't', 'b', 'd']
    vocab = all_words()
    search_space(beehive, vocab)
