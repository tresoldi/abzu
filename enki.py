# encoding: utf-8

import random

def random_word():
    c = "kgtdszfvpb"
    v = "aeiou"

    syl = [
        random.choice(c),
        random.choice(v),
        random.choice(c),
        random.choice(v),
        random.choice(c)
    ]

    return "".join(syl)

def main():
    epoch = 0

    lang_a = [random_word() for r in range(5)]
    print("Creating random langs at epoch 0")
    print(lang_a)

    for i in range(10):
        epoch += 1
        if random.randint(0, 10) == 7:
            w = random_word()
            lang_a[random.randint(0, len(lang_a)-1)] = w
            print("Random new word in lang_a at epoch %i" % epoch)

    print(lang_a)

if __name__ == "__main__":
    main()
