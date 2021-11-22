# 해당 로또 번호가 존재하는지 여부를 in 말고 좀 더 효율적인 방법을 생각해보자.
def solution(lottos, win_nums):
    cnt, zero, consis, answer = 0, 0, [6,6,5,4,3,2,1],[]
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            zero += 1
    answer.append(consis[cnt+zero])
    answer.append(consis[cnt])
    return answer
