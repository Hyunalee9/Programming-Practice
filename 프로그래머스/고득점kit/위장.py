from collections import defaultdict
import math
def solution(clothes):
    answer, style, cal = len(clothes), defaultdict(int), 1
    for c in clothes:
        style[c[1]] += 1  # 각 종류가 몇 개 있는지 count
    for count in style.values():
        cal *= math.comb(count+1,1)  # 아예 안 입는 경우도 하나 추가해서 1 pick
        if len(style) == 1:  #  종류가 하나 뿐이면 안입을경우 누드가 되니 1일1p
            return answer
    return cal -1  #  마찬가지로 누드로 다닐 경우 1을 빼주기
