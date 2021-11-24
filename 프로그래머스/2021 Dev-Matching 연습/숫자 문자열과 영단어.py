def solution(s):
    al = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    di = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i, j in zip(al, di):
        if i in s:
            s = s.replace(i, j)
    return int(s)