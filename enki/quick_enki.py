# encoding: utf-8

"""
Simpler and (almost) self-contained version of Enki.
"""

import csv
import re
import numpy as np

from enki import enki_data

# TODO: add note on distribution, weight first, bar-separated values later
# TODO: add note that this has no information of segment weight
# TODO: note that this is for a quick result, with no phonotactics
# TODO: both here and in others, check if weight normalization is needed
#       now that we are using numpy
# TODO: here and in the others, add seed
def random_vowel_inv(distr=None):
    """
    Returns a random vowel inventory.

    This does not include probabilities for weighted random draws inside
    the inventory.
    """

    # If no distribution of inventories, with relative weights, is provided,
    # build one from `enki_data`.
    if not distr:
        # initialize an empty distribution
        distr = {}

        # copy the inventories as a `pop`ulation
        distr['pop'] = [entry[1] for entry in enki_data.VOWEL_INV]

        # get the ratio and copy the frequencies as `weights`
        weights = [entry[0] for entry in enki_data.VOWEL_INV]
        weight_sum = sum(weights)
        distr['weights'] = [weight/weight_sum for weight in weights]

    # get a random weighted individual
    vowel_inv = np.random.choice(
        distr['pop'],
        p=distr['weights'],
        size=1,
    )[0]

    return vowel_inv.split('|')


# TODO: rename to maximum syllable pattern
def random_syll_pattern(distr=None):
    """
    Returns a random syllable pattern.
    """

    # If no distribution of inventories, with relative weights, is provided,
    # build one from `enki_data`.
    if not distr:
        # initialize an empty distribution
        distr = {}

        # copy the patterns as a `pop`ulation
        distr['pop'] = [entry[1] for entry in enki_data.SYLL_PATTERN]

        # get the ratio and copy the frequencies as `weights`
        weights = [entry[0] for entry in enki_data.SYLL_PATTERN]
        weight_sum = sum(weights)
        distr['weights'] = [weight/weight_sum for weight in weights]

    # get a random weighted individual
    pat = np.random.choice(
        distr['pop'],
        p=distr['weights'],
        size=1,
    )[0]

    return pat


# TODO: allow without specifying syllable pattern
def random_cons_inv(distr):
    """
    Returns a random consonant inventory from a list of possibilities.
    """

    # numpy.random.choice only works with 1-dimensional values,
    # so we choose the index

    initials, medials, finals = distr[np.random.choice(
        len(distr),
        size=1
    )[0]]

    if initials:
        initials = initials.split('|')
    else:
        initials = []

    if medials:
        medials = medials.split('|')
    else:
        medials = []

    if finals:
        finals = finals.split('|')
    else:
        finals = []

    return initials, medials, finals


def random_cons_inv_from_pattern(pattern=None):
    if not pattern:
        pattern = random_syll_pattern()

    return random_cons_inv(enki_data.CONS_INV[pattern])


def random_phonology(inventory, param, base_freq=None):
    """
    Returns consonant and vowel inventories with random frequencies.
    """

    # load parameters
    perturbation = param.get('perturbation', 1.5)

    # load the base frequency, if it was not provided
    if not base_freq:
        base_freq = enki_data.PHONEME_FREQ

    # the perturbation is basically done by selecting a random number in
    # the requested range, for which we compute the lower and upper bound,
    # and taking the original frequency to that power; a pertubation of zero
    # samples in [1.0, 1.0], which means using the base_freq
    perturb_low = 1.0 - (perturbation/2.0)
    perturb_high = 1.0 + (perturbation/2.0)

    # get the mean frequency divided by 1.5, so we have something to default
    # in case of missing graphemes (especially clusters)
    # TODO: this is applying to all clusters right now, as we have a space
    #       between the graphemes in enki_data but not in phoible
    default_freq = np.mean(list(base_freq.values())) / 1.5

    # compute random frequencies
    vowels = {
        vowel : base_freq.get(vowel, default_freq) ** np.random.uniform(low=perturb_low, high=perturb_high)
        for vowel in inventory['vowels']
    }

    initials = {
        cons : base_freq.get(cons, default_freq) ** np.random.uniform(low=perturb_low, high=perturb_high)
        for cons in inventory['initials']
    }

    medials = {
        cons : base_freq.get(cons, default_freq) ** np.random.uniform(low=perturb_low, high=perturb_high)
        for cons in inventory['medials']
    }

    finals = {
        cons : base_freq.get(cons, default_freq) ** np.random.uniform(low=perturb_low, high=perturb_high)
        for cons in inventory['finals']
    }

    # correct the new probabilities, so they sum 1.0
    new_inventory = {}
    new_inventory['vowels'] = {k:v/sum(vowels.values()) for k, v in vowels.items()}
    new_inventory['initials'] = {k:v/sum(initials.values()) for k, v in initials.items()}
    new_inventory['medials'] = {k:v/sum(medials.values()) for k, v in medials.items()}
    new_inventory['finals'] = {k:v/sum(finals.values()) for k, v in finals.items()}

    return new_inventory


def random_words(num_words, param, seed=None):
    # set the seed
    np.random.seed(seed)

    # get parameters as specified or default
    # TODO: default `no_consonant` should depend on the system entropy
    no_cons_low = param.get('no_cons_low', 0.33)
    no_cons_high = param.get('no_cons_high', 0.66)
    base_syl_lambda = param.get('base_syl_lambda', 10)
    remove_length = param.get('remove_length', 0.33)

    # get the 'phonotactics' of the language
    pattern = random_syll_pattern()
    inv = {}
    inv['vowels'] = random_vowel_inv()
    inv['initials'], inv['medials'], inv['finals'] = \
        random_cons_inv(enki_data.CONS_INV[pattern])
    phonology = random_phonology(inv, param)
    no_consonant = np.random.uniform(low=no_cons_low, high=no_cons_high)

    # cache keys/values/lengths
    v_keys = list(phonology['vowels'].keys())
    v_values = list(phonology['vowels'].values())
    v_len = len(v_keys)
    v_range = list(range(len(v_keys)))

    i_keys = list(phonology['initials'].keys())
    i_values = list(phonology['initials'].values())
    i_len = len(i_keys)
    i_range = list(range(len(i_keys)))

    m_keys = list(phonology['medials'].keys())
    m_values = list(phonology['medials'].values())
    m_len = len(m_keys)
    m_range = list(range(len(m_keys)))

    f_keys = list(phonology['finals'].keys())
    f_values = list(phonology['finals'].values())
    f_len = len(f_keys)
    f_range = list(range(len(f_keys)))

    # generate all words
    words = []
    for word_idx in range(num_words):
        # get the number of syllables from a poisson distribution; we try to
        # correct for entropy by manipulating the lambda, so that languages with
        # simpler phonotactics will tend to have more syllables; we also
        # currently restrict to at most 5 syllables
        syl_lambda = base_syl_lambda / np.sqrt(v_len+m_len)
        num_syl = min(np.random.poisson(syl_lambda) + 1, 5)

        # if we got a single syllable, increase it with another one 66% of the
        # time -- not very chinese like
        # TODO: this is needed because the syllable length distribution in
        #       world languages does not seem to be a Poisson distirbution,
        #       but one whose shape is closer to a gamma one, with many other
        #       factors involved (such as size of inventory)
        if num_syl == 1:
            if np.random.random() < 0.66:
                num_syl = 2

        syl_sounds = []
        for syl in range(num_syl):
            # get a random initial or medial (or nothing)
            if np.random.random() < no_consonant:
                if syl == 0:
                    _ = np.random.choice(i_len, p=i_values)
                    syl_sounds.append(i_keys[_])
                else:
                    _ = np.random.choice(m_len, p=m_values)
                    syl_sounds.append(m_keys[_])

            # get a random vowel
            _ = np.random.choice(v_len, p=v_values)
            syl_sounds.append(v_keys[_])

            # get a random final (or not) if at last syllable and if
            # finals are used
            if syl == num_syl-1 and f_len:
                if np.random.random() < no_consonant:
                    _ = np.random.choice(f_len, p=f_values)
                    syl_sounds.append(f_keys[_])

        # collect
        words.append(' '.join(syl_sounds))

    # apply basic, "universal", phonotactics
    words = [
        apply_basic_phonotactics(word)
        for word in words]

    # remove all length symbols by random decision
    if np.random.random() < remove_length:
        words = [word.replace('ː', '') for word in words]

    words = [word.replace(' ', '') for word in words]

    return words

def apply_basic_phonotactics(word):
    rules = [
        # remove runs of three equal sounds, lengthening
        [r' (.) \1 \1 ',    r'\1ː '],
        # remove runs of two equal sounds, lengthening
        [r' (.) \1 ',       r' \1ː '],
        # remove runs of two equal sounds, the first long, lengthening
        [r' (.)ː \1 ',      r' \1ː '],
        # converts most vowel clusters to vowel+glide or glide + vowel
        [r' (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ) (i|y|ɨ|ʏ) ',
         r' \1 j'],
        [r' (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ) (ɯ|u|ʊ) ',
         r' \1 w'],
        [r' (i|y|ɨ|ʏ) (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ)  ',
         r' j \1 '],
        [r' (ɯ|u|ʊ) (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ)  ',
         r' w \1 '],
        # don't allow long glides
        [r' (j|w)ː ',       r' \1 '],
        # remove less stable glide+vowel combinations
        [r' (i|y|ɨ|ʏ) j ', r' \1 '],
        [r' (ɯ|u|ʊ) w ', r' \1 '],
        [r' j (i|y|ɨ|ʏ) ', r' \1 '],
        [r' w (ɯ|u|ʊ) ', r' \1 '],
        # aspiration
        [r' (p|t|k) h ',    r' \1ʰ '],
        # intervocalic /j/ to /ʒ/
        [r' (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ) j (i|y|ɨ|ʉ|ɯ|u|ɪ|ʏ|ʊ|e|o|ɛ|ɜ|ʌ|ɔ|æ|ɐ|a|ɑ|ɒ) ',
         r' \1 ʒ \2 '],
    ]

    # add boundaries for manipulation
    word = ' # %s # ' % word

    # apply regexes
    for rule in rules:
        word = re.sub(rule[0], rule[1], word)

    # remove boundaries, strip, and return
    word = word.replace('#', '').strip()

    return word


def quick_test():
    param = {}

    print("--> random_vowel_inv()")
    for i in range(4):
        print('  %i %s' % (i, random_vowel_inv()))
    print()

    print("--> random_syll_pattern()")
    for i in range(4):
        print('  %i %s' % (i, random_syll_pattern()))
    print()

    print("--> random_cons_inv()")
    for i in range(4):
        pattern = random_syll_pattern()
        distr = enki_data.CONS_INV[pattern]
        initials, medials, finals = random_cons_inv(distr)
        print('  %i %i/%i/%i (%s)' % (
            i,
            len(initials),
            len(medials),
            len(finals),
            pattern
            ))
    print()

    print('--> random_frequency()')
    for i in range(4):
        pattern = random_syll_pattern()
        inv = {}
        inv['vowels'] = random_vowel_inv()
        inv['initials'], inv['medials'], inv['finals'] = \
            random_cons_inv(enki_data.CONS_INV[pattern])
        phonology = random_phonology(inv, param)

        print('  items: %i/%i/%i/%i' % (
            len(phonology['vowels']),
            len(phonology['initials']),
            len(phonology['medials']),
            len(phonology['finals'])
        ))
    print()

    print('--> random_words()')
    for i in range(4):
        print('  l:', random_words(5, param))
    print()
