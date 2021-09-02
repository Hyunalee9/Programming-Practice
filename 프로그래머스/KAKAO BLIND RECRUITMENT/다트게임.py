def solution(dartResult):  # 파이썬 버전
    trans = dartResult.replace("10", "+")  # 어차피 두자리 숫자는 10밖에 없어서 따로 예외처리
    stack, option = [], {"S":1,"D":2,"T":3}  # 처음에 생각했던 대로 옵션은 딕셔너리로 키:값을 정해줌
    for i in trans :
        if i.isdigit():  # 숫자는 int로 변환해서 스택에 넣음
            stack.append(int(i))
        elif i == "+":
            stack.append(10)
        elif i.isalpha():  # 알파벳 만나면 pop시켜서 각 key에 대한 value 승을 해줌
            stack.append(stack.pop() ** option[i])
        elif i == '*':
            score = stack.pop()  # 값 꺼내고 임시 저장
            if len(stack) != 0:  # 값 존재하면
                stack[-1] *= 2   # 직전의 값 * 2
            stack.append(2 * score)  # 임시 저장 * 2
        elif i == '#':
             stack[-1] *= -1
    return sum(stack)

    #####################################################
    #역시나 정규표현식 사용한 사람이 짱..다음에는 나도 써봐야지 
