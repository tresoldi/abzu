# Enki

[![Build Status](https://travis-ci.org/tresoldi/enki.svg?branch=master)](https://travis-ci.org/tresoldi/enki)
[![codecov](https://codecov.io/gh/tresoldi/enki/branch/master/graph/badge.svg?token=o5ntv3ssOH)](https://codecov.io/gh/tresoldi/enki)

Enki system for simulating language evolution, which used the
[ngesh](https://github.com/tresoldi/ngesh) and
[alteruphono](https://github.com/tresoldi/alteruphono) libraries.
It is named after
[Enki](https://en.wikipedia.org/wiki/Enki), the Sumerian god of language and
confusion.

*Please remember that `enki` is a work-in-progress.*

## Installation

In any standard Python environment, `enki` can be installed with:

```
pip install enki
```

The `pip` instalation will also fetch dependencies, such as `ngesh` and
`alteruphono`, if necessary. Installation in a virtual environment is
recommended.

## How to use

The library is under development, and the best way to understand its
usage is to follow the
[tests](https://github.com/tresoldi/enki/blob/master/tests/test_enki.py).

A quick generation of a vocabulary following a random phonological
system can be performed from the command-line:

```
$ enki
Language: Aburo
  1:    oː e
  2:    i ŋ ẽ
  3:    f ɔ j ŋ
  4:    e h ɪ̃ s eː ʃ
  5:    i
  6:    k ɔː m ĩ ŋ uː
  7:    h a eː
  8:    u f
  9:    iː p
  10:   a o a ŋ
```

The utility accepts `size` (indicating the number of words in the
vocabulary) and `seed` (for reproducibility) parameters:

```
$ enki --size 15 --seed jena
Language: Rafvo
  1:    a m ã
  2:    e m e ɔ n ɨ n
  3:    p ɪ ʒ ɔ
  4:    ĩ b a ɔ
  5:    i n
  6:    ɪ a ŋ u j ʃ
  7:    t ɪ l u
  8:    n ɔ e
  9:    d u ɔ e ʃ
  10:   i s ɪ x
  11:   a b ẽ j
  12:   ɪ̃ ɪ b l a t u ʂ
  13:   e m ɔ n a ɪ ɲ e j s
  14:   n ɪ̃ tʃ ĩ ã
  15:   a ʃ a
```

## TODO

*See internal notes*

## How to cite

If you use `enki`, please cite it as:

> Tresoldi, Tiago (2019). Enki, a system for simulating language evolution.
Version 0.0.1dev. Jena. Available at [https://github.com/tresoldi/enki]

In BibTex:

```
@misc{Tresoldi2019enki,
  author = {Tresoldi, Tiago},
  title = {Enki, a system for simulating language evolution},
  howpublished = {\url{https://github.com/tresoldi/enki}},
  address = {Jena},
  year = {2019},
}
```

## Author

Tiago Tresoldi (tresoldi@shh.mpg.de)

The author was supported during development by the 
[ERC Grant #715618](https://cordis.europa.eu/project/rcn/206320/factsheet/en)
for the project [CALC](http://calc.digling.org)
(Computer-Assisted Language Comparison: Reconciling Computational and Classical
Approaches in Historical Linguistics), led by
[Johann-Mattis List](http://www.lingulist.de).

```
