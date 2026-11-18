# 파이썬 연습문제풀이 업로드

## 1
p1-1.py 두 수를 입력해서 사칙연산

p1-3.py 여러 수식 계산

## 2
p2-1.py 두 리스트의 내적 계산

p2-2.py 학번이랑 이름을 딕셔너리로 저장하고 조회

p2-3.py 1부터 100까지 홀수 짝수 구분

p2-4.py 3과 5의 배수 구분

p2-5.py 입력한 연도가 윤년인지 확인

p2-6.py 2부터 100까지 소수 찾기

## 3
p3-1.py 여러 수의 덧셈과 곱셈 계산

p3-2.py 입력한 수들의 최솟값 최댓값 구하기

p3-3.py 문자열에서 모음 개수 세기

## 4
p4-1.py 파일 내용을 줄 번호와 함께 출력하고 저장

p4-2.py 파일의 문자 단어 줄 수 계산


---

# TFTP Client 과제

## 1. 프로그램 소개
Python Socket API를 사용하여 구현한 TFTP Client 프로그램입니다.
UDP 통신을 통해 서버와 파일 다운로드 및 업로드를 수행합니다.

## 2. 주요 기능
- GET: 서버에서 파일 다운로드
- PUT: 서버로 파일 업로드
- 서버 IP 주소 입력
- 포트 번호 설정 (-p)
- 서버 응답 시간 초과 처리
- TFTP 서버 오류 메시지 처리

## 3. 실행 방법

### 파일 다운로드
```bash
python mytftp.py 서버IP get 파일이름
```

### 파일 업로드
```bash
python mytftp.py 서버IP put 파일이름
```

### 포트 번호 지정
```bash
python mytftp.py 서버IP -p 포트번호 get 파일이름
python mytftp.py 서버IP -p 포트번호 put 파일이름
```

## 4. 실행 예시
다운로드:
```bash
python mytftp.py 203.250.133.88 get tftp.conf
```

업로드:
```bash
python mytftp.py 203.250.133.88 -p 69 put tftp.txt
```

## 5. 개발 환경
- Language: Python
- Protocol: TFTP
- Communication: UDP Socket
