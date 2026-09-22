"""연습문제 2-3: 1부터 100까지 홀짝 구분"""

for number in range(1, 101):
    if number % 2 == 1:
        print(f"{number}은 홀수입니다")
    else:
        print(f"{number}은 짝수입니다")
