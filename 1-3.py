"""연습문제 1-3: 수식 계산"""

import math

# 1. 1 / (1 + a / b + c)
a, b, c = 3, 4, 5
answer1 = 1 / (1 + a / b + c)
print(f"1번: {answer1}")

# 2. 2차방정식의 근의 공식
a, b, c = 1, 1, -6
discriminant = b**2 - 4 * a * c
x1 = (-b + math.sqrt(discriminant)) / (2 * a)
x2 = (-b - math.sqrt(discriminant)) / (2 * a)
print(f"2번 (두 근): {x1}, {x2}")

# 3. 원의 면적
r = 5
area = math.pi * r**2
print(f"3번 (원의 면적): {area}")

# 4. beta * e^(-g)
beta, g = 2.0, 3.2
answer4 = beta * math.exp(-g)
print(f"4번: {answer4}")

# 5. 정규분포 식
x, mu, rho = 0, 1.5, 2.0
answer5 = (1 / (math.sqrt(2 * math.pi) * rho)) * math.exp(
    -((x - mu) ** 2) / (2 * rho**2)
)
print(f"5번: {answer5}")
