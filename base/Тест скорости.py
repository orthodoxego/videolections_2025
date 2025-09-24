from stme import STme

name = "Виктор"
age = "75"

st1 = STme("Просто print")
for i in range(1000):
    print("Привет, " + name + "! Тебе " + age + " лет!")
st1.stop()

# 0.0078
# 0.0030

# 0069
# 0024

st2 = STme("Просто f-строка")
for i in range(1000):
    print(f"Привет, {name}! Тебе {age} лет!")
st2.stop()