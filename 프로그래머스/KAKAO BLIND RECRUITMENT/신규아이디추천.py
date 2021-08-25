def solution(new_id):  # main
    one = to_lowercase(new_id)
    three = remove_theother(one)
    four = about_length(three)
    return four


def to_lowercase(new_id):  # 1 모든 문자를 소문자로 
    return new_id.lower()

def remove_theother(one):  
    two = ""
    three=""
    for i in one:   # 2
        if i.islower() or i.isdigit() or i in "-_.":
            two += i
    while two.count("..") >= 1:  # 3 ".." 의 수가 1 이상이면 
        two = two.replace("..",".")  # 그 수가 0이 될 때까지 "." 로 바꾸기
    result = two.strip(".")  # 4 양 끝 "." 없애기
    if result == "":
        result += "aaa"  # 5 최소 아이디 length에 맞춰 a를 채워넣어 줌
    return(result)    

def about_length(three):
    if(len(three) > 15): # 6
        three = three[0:15]
    result = three.strip(".")
    while len(result) <= 2 : # 7
        result += result[-1]
    return result
  
############################################################################

# 어떤 사람은 정규식 표현을 써서 훨~~~씬 짧게 짰더라. 정규식도 공부해보기,,
