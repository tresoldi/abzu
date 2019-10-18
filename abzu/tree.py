import random
import numpy as np

import abzu
import ngesh

def tree_test():
    CONCEPTS = 10

    # generate a fixed tree for the tests
    tree = ngesh.gen_tree(1.0, 0.5, max_time=1.0, labels="human", seed=13)

    # TODO: need to add seed to `add_characters`
    # TODO: need to sort the taxa in output in `tree2nexus`
    tree = ngesh.add_characters(tree, CONCEPTS, 3.0, 0.5, seed=13)

    # collect all taxa and their characters, provided the characters exist
    # TODO: reuse code? already in tree2nexus
    data = {leaf.name:leaf.chars for leaf in tree.get_leaves()}

    # get the number of words to generate -- we generate all those that
    # will be used at the beginning, following their path as if they
    # always existed
    # TODO: generate based on phonology of current available ones?
    num_words = max([max(chars) for chars in data.values()]) + 1
    words = abzu.kiss.random_words(num_words, param={})

    print(tree)
    print(ngesh.tree2nexus(tree))
    print(data)
    print(words, len(words))

    for node in tree.iter_descendants():
        print([node.name], node.dist)
        print(dir(node))

    #output_wordlist(data, words)

def output_wordlist(data, words):
    # attribute
    # TODO: copying directly here, needs sound changes, HTG, etc.
    wordlist = {
        taxon : [words[i] for i in chars]
        for taxon, chars in data.items()
    }

    CONCEPTS = len(list(data.values())[0])

    # wordlist output
    row_id = 1
    for taxon in sorted(wordlist):
        for i in range(CONCEPTS):
            buf = [
                str(row_id),
                taxon,
                "concept-%i" % (i+1),
                wordlist[taxon][i],
                str(data[taxon][i]+1), # cogid
            ]
            print(",".join(buf))

            row_id += 1

if __name__ == "__main__":
    tree_test()
