print("Hello, README!")

text = (
    "Lorem Ipsum - это текст-«рыба», часто используемый в печати и вэб-дизайне."
    "Lorem Ipsum"
)
print(text)


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Привет, {name}"


numbers = [1, 2, 3, 4, 5]

print(greet("мир"))
print(add(2, 2))