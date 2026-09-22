"""연습문제 4-1: 파일 내용에 줄 번호를 붙여 출력하고 저장"""


def read_lines(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print("파일이 없습니다.")
        return None


def save_numbered_file(file_name, lines):
    save_name = (
        file_name.rsplit(".", 1)[0] + ".sav"
        if "." in file_name
        else file_name + ".sav"
    )
    with open(save_name, "w", encoding="utf-8") as file:
        for number, line in enumerate(lines, 1):
            file.write(f"{number} {line}")
    print(f"저장 완료: {save_name}")


while True:
    file_name = input("파일 이름을 입력하세요 (종료: quit): ").strip()
    if file_name.lower() == "quit":
        break

    lines = read_lines(file_name)
    if lines is None:
        continue

    for number, line in enumerate(lines, 1):
        print(f"{number} {line.rstrip()}")
    save_numbered_file(file_name, lines)
    break
