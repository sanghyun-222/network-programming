"""연습문제 3-2: 최솟값과 최댓값 반환"""


def min_max(numbers):
    return min(numbers), max(numbers)


data = list(map(int, input("정수들을 공백으로 입력하세요: ").split()))
minimum, maximum = min_max(data)
print(f"min = {minimum}, max = {maximum}")
print(f"반환값: ({minimum}, {maximum})")
