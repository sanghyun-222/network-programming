"""연습문제 4-2: 파일의 문자, 단어, 줄 수 세기"""


def count_file_info(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("파일이 없습니다.")
        return

    characters = len(text.replace(" ", "").replace("\n", ""))
    words = len(text.split())
    lines = len(text.splitlines())

    print(f"characters : {characters}")
    print(f"words : {words}")
    print(f"lines : {lines}")


file_name = input("파일 이름을 입력하세요: ")
count_file_info(file_name)
