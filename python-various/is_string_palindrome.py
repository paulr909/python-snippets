def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()


print(is_palindrome("Paul"))

print(is_palindrome("Abba"))

print(is_palindrome("LEVEL"))
