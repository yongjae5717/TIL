import sys
input = sys.stdin.readline


def main():
    n = int(input())
    m = int(input())
    ingredients = list(map(int, input().split()))
    ingredients.sort()
    result = 0
    i, j = 0, n-1
    while i < j:
        if ingredients[i] + ingredients[j] == m:
            result += 1
            i += 1
            j -= 1
        elif ingredients[i] + ingredients[j] < m:
            i += 1
        else:
            j -= 1
    print(result)


main()