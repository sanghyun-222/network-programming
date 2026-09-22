"""연습문제 2-6: 2부터 100까지 소수 찾기"""

for number in range(2, 101):
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            break
    else:
        print(f"{number}은 소수입니다")
