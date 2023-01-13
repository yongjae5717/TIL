import math
import sys
input = sys.stdin.readline


def main():
    dictionary = dict()
    count = 0
    while True:
        name = input().strip()
        if not name:
            break
        count += 1
        if not dictionary.get(name):
            dictionary[name] = 1
        else:
            dictionary[name] += 1
    tree_list = sorted(dictionary.items())

    for tree in tree_list:
        name, tree_count = tree
        print(name, f'{(tree_count/count) * 100:.4f}')


main()