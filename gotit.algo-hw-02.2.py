from collections import deque

def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")
    char_queue = deque(input_str)
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

input_str = input("Введіть рядок для перевірки на паліндром: ")
if is_palindrome(input_str):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
