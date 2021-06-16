# round 함수 ,  format method 이용해보기
import sys
c = int(input())
while c != 0:
    result, top = 0, 0
    arr = list(map(int, sys.stdin.readline().split()))
    avg = sum(arr[1:]) / arr[0]
    for i in range(1, arr[0] + 1):
        if arr[i] > avg:
            top += 1;
    result = (top / arr[0]) * 100
    print("{:.3f}%".format(result))    # 끝 자리가 0일 때, 000이렇게 나오게 해주기
    c -= 1;

