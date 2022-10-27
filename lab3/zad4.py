def reverse(text: str) -> str:
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]


text = "test"
print(reverse(text))
