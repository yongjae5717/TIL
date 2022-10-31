def solution(genres, plays):
    sumDict = dict()
    album = dict()
    count = 0
    for genre, play in zip(genres, plays):
        if genre not in sumDict:
            sumDict[genre] = play
        else:
            sumDict[genre] += play

        if genre not in album:
            album[genre] = [[play, count]]
        else:
            album[genre].append([play, count])
        count += 1

    sumList = sorted(sumDict.items(), key=lambda x: -x[1])

    answer = list()
    for (genre, totalPlay) in sumList:
        album[genre] = sorted(album[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in album[genre][:2]]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

print(solution(["classic", "pop", "classic", "classic", "pop", "jpop"], [500, 600, 150, 800, 2500, 3000]))