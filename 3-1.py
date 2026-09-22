"""연습문제 3-1: 여러 수의 덧셈과 곱셈"""


def calc(*args, op):
    if op == "+":
        return sum(args)
    if op == "*":
        result = 1
        for number in args:
            result *= number
        return result
    raise ValueError("op에는 '+' 또는 '*'만 사용할 수 있습니다.")


print(calc(1, 2, 5, op="+"))
print(calc(1, 2, op="*"))
