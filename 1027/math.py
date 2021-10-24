import math

input_angle = float(input('角度を入力してください（度）：'))

input_angle=str(input_angle)

print(input_angle + "度->", end="")

input_angle=float(input_angle)

print(math.radians(input_angle), end="")

print(" " + "ラジアン")

input_angle=str(input_angle)

print("sin(" + input_angle + ")=>", end="")

input_angle=float(input_angle)

print(math.sin(math.radians(input_angle)))