import tkinter as tk

FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result

def encrypt_message():
    user_message = message_entry.get()
    user_shift_key = int(shift_entry.get())
    cipher_text = caesar_shift(user_message, user_shift_key)
    result_label.config(text="Cipher Text: " + cipher_text)

root = tk.Tk()
root.title("Caesar Cipher Encryption")


root.geometry("400x200")

message_label = tk.Label(root, text="Message to Encrypt:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

shift_label = tk.Label(root, text="Shift Key (integer):")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
