# 13

# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
#
# for ch in message:
#     if ch == " ":
#         new_char = " "
#         encoded_message += new_char
#     elif ch == "!":
#         new_char = "!"
#         encoded_message += new_char
#     elif ch.upper() == ch:
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#         encoded_message += new_char
#     else:
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message += new_char
#
# print(f"Encoded message: {encoded_message}")

# 14

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
#     print(chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# 15

result = ()
operand = float()
operator = ("+", "-", "*", "/")
wait_for_number = True

while True:
    user_input = input(">>>")
    if user_input == "=":
        print(result)
        break

    if wait_for_number == True:
        operand = float(wait_for_number)
        wait_for_number = False
        if result == None:
            result = operand
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
    else:
        if wait_for_number == ("+", "-", "*", "/"):
            wait_for_number = operator
            wait_for_number = True