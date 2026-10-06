"""연습문제 2-4: 1부터 100까지 3과 5의 배수 판별"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}은 3과 5의 배수입니다")
    elif number % 3 == 0:
        print(f"{number}은 3의 배수입니다")
    elif number % 5 == 0:
        print(f"{number}은 5의 배수입니다")
