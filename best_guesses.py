import itertools
import nltk
import sys


def all_words():
     _vocab = list(set(w.lower() for w in nltk.corpus.words.words()))
     _vocab_five = [k for k in _vocab if len(k) == 5]
     return _vocab_five


def search_space(_known_positions, _known_letters, _bad_letters, _vocab):
    init_guesses = []
    if len(_known_positions) > 0:
        for j in range(len(_known_positions)):
            if j == 0:
                known_candidates = _vocab
                _kno = _known_positions[j]
                known_candidates = [k for k in known_candidates if k[_kno[1]] == _kno[0]]
            else:
                _kno = _known_positions[j]
                known_candidates = [k for k in known_candidates if k[_kno[1]] == _kno[0]]
        for kc in known_candidates:
            if all([_l in kc for _l in _known_letters]):
                init_guesses.append(kc)
    else:
        for kc in _vocab:
            if all([_l in kc for _l in _known_letters]):
                init_guesses.append(kc)
    final_guesses = []
    for _g in init_guesses:
        if any(_b in _g for _b in _bad_letters):
            pass
        else:
            final_guesses.append(_g)
    print(final_guesses)


if __name__ == "__main__":
    vocab = all_words()
    search_space([['o', 2], ['r', 3], ['n', 4]], [], ['a', 'c', 'e' 'w', 's'], vocab)
