"""연습문제 2-1: 리스트의 내적"""

a = [1, 0, 1]
b = [1, 1, 2]

dot_product = sum(x * y for x, y in zip(a, b))
print(f"{a} * {b} = {dot_product}")
