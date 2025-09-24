
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(str(a) + " + " + str(b) + " = " + str(a + b))
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

print(f"{(a / b):0.1f}")

s = f"Привет, {a}! Как дела, {b}"
print(s)

s = "*"
d = "***"
f = "*****"
print(f"{s:<10}")
print(f"{d:>10}")
print(f"{f:^10}")

a = 13215
b = 897

print(len(str(a) + str(b)))
print(len(f"{a}{b}"))