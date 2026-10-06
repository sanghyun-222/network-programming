"""연습문제 2-2: 학번과 이름을 저장하는 딕셔너리"""

students = {}
print(
    "학번과 이름을 한 줄에 입력하세요 "
    "(예: 20123456 홍길동). 전체 입력 종료: 'Fin!', 프로그램 종료: 'Quit!'."
)

while True:
    line = input("학번과 이름을 입력하세요: ").strip()
    if line == "Quit!":
        print("종료합니다.")
        break
    if line == "Fin!":
        break

    parts = line.split()
    if len(parts) < 2:
        print("입력이 잘못되었습니다. 학번과 이름을 공백으로 구분해 입력하세요.")
        continue

    student_id, name = parts[0], parts[1]
    students[student_id] = name
    print(students[student_id])

print("만들어진 딕셔너리:", students)

while True:
    query = input("조회할 학번을 입력하세요(종료: 'Quit!'): ").strip()
    if query == "Quit!":
        print("종료합니다.")
        break
    print(students.get(query, "not found!"))
