import sys
input = sys.stdin.readline
t = int(input())

sentences = list(list(input().split()) for _ in range(t))


def solution(sentences):
    for sentence in sentences:
        answer = ""
        for word in sentence:
            answer += reverse(word) + " "
        print(answer.strip())


def reverse(word):
    temp = list(reversed(word))
    result = "".join(temp)
    return result


solution(sentences)