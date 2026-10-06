"""연습문제 2-5: 윤년 찾기"""

while True:
    line = input("윤년을 확인할 연도를 입력하세요 (종료: 'Quit!'): ").strip()
    if line == "Quit!":
        print("프로그램을 종료합니다.")
        break
    if not line.isdigit():
        print("연도는 숫자만 입력하세요.")
        continue

    year = int(line)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year}년은 윤년입니다")
    else:
        print(f"{year}년은 평년입니다")
