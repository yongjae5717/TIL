def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        reversedSkill = list(reversed(skill))
        temp = list(i)
        flag = False
        for s in temp:
            if s in reversedSkill:
                if s == reversedSkill[-1]:
                    reversedSkill.pop()
                else:
                    flag = True
        if flag:
            # print(temp)
            answer -= 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))