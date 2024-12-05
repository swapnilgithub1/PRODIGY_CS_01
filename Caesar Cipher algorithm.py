Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def caesar_cipher(text, shift, direction):
...     result = ""
...     # Traverse the text
...     for char in text:
...         if char.isalpha():
...             # Calculate the shift for uppercase and lowercase characters
...             shift_base = 65 if char.isupper() else 97
...             if direction == "encrypt":
...                 result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
...             elif direction == "decrypt":
...                 result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
...         else:
...             result += char
...     return result
... 
... def main():
...     message = input("Enter your message: ")
...     shift = int(input("Enter shift value: "))
...     action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
... 
...     if action == "encrypt":
...         encrypted_message = caesar_cipher(message, shift, "encrypt")
...         print("Encrypted Message:", encrypted_message)
...     elif action == "decrypt":
...         decrypted_message = caesar_cipher(message, shift, "decrypt")
...         print("Decrypted Message:", decrypted_message)
...     else:
...         print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
... 
... if __name__ == "__main__":
...     main()
