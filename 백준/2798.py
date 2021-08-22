n, m = list(map(int, input().split()))
cards, answer = list(map(int, input().split())), 0
for i in range(0, n):  # 첫 번째 숫자
    for j in range(i+1, n):  # 두 번째 숫자
        for k in range(j+1, n):  # 세 번째 숫자
            new_m = cards[i]+cards[j]+cards[k]
            if new_m <= m:
                answer = max(answer, new_m)  # m을 넘지 않으면서 제일 큰 값이 정답이 된다.
print(answer)
