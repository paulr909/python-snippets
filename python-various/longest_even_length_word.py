import re

text1 = "Start a private video call with your friends or colleagues!"
text2 = (
    "This is a simple test sentence with some words? Plus some random numbers 3, 4, 6."
)


def get_longest_even_length_word(sentence: str) -> str:
    strip_string = re.sub(r"[^a-zA-Z0-9]", " ", sentence).split()
    # print("Stripped:", " ".join(strip_string))

    even_length_words = [word for word in strip_string if len(word) % 2 == 0]

    if even_length_words:
        return max(even_length_words, key=len)
    else:
        return "00"


result = get_longest_even_length_word(text1)

print("Result:", result)
