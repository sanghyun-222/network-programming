"""연습문제 3-3: 문자열의 모음 개수 세기"""


def count_vowel(text):
    vowels = "aeiouAEIOU"
    return sum(1 for character in text if character in vowels)


text = input("문자를 입력하세요: ")
print(count_vowel(text))
