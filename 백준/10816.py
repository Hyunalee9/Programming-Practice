import sys
from collections import Counter
n = int(input())  # 상근이가 가지고 있는 숫자 카드의 갯수
card = Counter(list(map(int, sys.stdin.readline().split())))  # Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})
m = int(input())  # 구해야 할 카드의 갯수
card_two = list(map(int, sys.stdin.readline().split()))
for i in card_two:
    if i in card:
        print(card.get(i), end=" ")  # 해당 숫자 카드가 있다면, 딕셔너리에서 해당하는 값을 가져오기
    else:
        print(card.get(i, 0), end=" ") # 없다면 0을 출력하기.
