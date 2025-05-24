import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break

    a = b = c = d = 0  # 소문자, 대문자, 숫자, 공백 초기화

    for ch in line:
        if ch.islower():
            a += 1
        elif ch.isupper():
            b += 1
        elif ch.isdigit():
            c += 1
        elif ch == ' ':
            d += 1

    print(a, b, c, d)
