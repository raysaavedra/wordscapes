import itertools
import enchant

from argparse import ArgumentParser

def word_generator(letters, length):
    return itertools.permutations(letters, length)

def main(letters, min_length=3):
    enchant_dict = enchant.Dict("en_US")
    final_list = []

    for i in range(min_length, len(letters)+1):
        for word in word_generator(letters, i):
            word = ''.join(word)
            
            if enchant_dict.check(word):
                if word not in final_list:
                    final_list.append(word)

    print([x for x in final_list])

if __name__ == '__main__':
    parser = ArgumentParser(__doc__)

    parser.add_argument("-l", "--letters", nargs="+", required=True, help="List of letters to generate from")
    parser.add_argument("-m", "--min", required=False, type=int, help="Min length of word")

    args = parser.parse_args()

    min_length = 3 if not args.min else args.min

    main(args.letters, min_length=min_length)
