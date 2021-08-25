# bin() = 10진수 숫자를 2진수 문자열로 바꾸는 함수
# [2: ] 인 이유 0b 제외한 숫자만..
# 비트 연산자 써서 둘중 하나라도 1이면 1이게끔끔
# rjust(n, '0') n자리 수 확보 후 오른쪽 정렬 , 공백은 '0'로 채우기

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer