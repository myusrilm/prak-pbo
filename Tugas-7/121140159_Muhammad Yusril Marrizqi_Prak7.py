import tkinter as tk
from tkinter import messagebox

def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

def encrypt_text():
    try:
        shift = shift_entry.get()
        if not shift:
            raise ValueError("Please enter a shift value")
        try:
            shift = int(shift)
        except ValueError:
            raise ValueError("Shift value must be an integer")
        plaintext = plaintext_entry.get("1.0", tk.END).strip()
        if not plaintext:
            raise ValueError("Please enter some text to encrypt")
        ciphertext = encrypt(plaintext, shift)
        ciphertext_entry.delete("1.0", tk.END)
        ciphertext_entry.insert("1.0", ciphertext)
        global result
        result=1
        messagebox.showinfo("Encrypt", "Text Encrypted!")
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def decrypt_text():
    try:
        shift = shift_entry.get()
        if not shift:
            raise ValueError("Please enter a shift value")
        try:
            shift = int(shift)
        except ValueError:
            raise ValueError("Shift value must be an integer")
        ciphertext = ciphertext_entry.get("1.0", tk.END).strip()
        if not ciphertext:
            raise ValueError("Please enter some text to decrypt")
        plaintext = decrypt(ciphertext, -shift)
        plaintext_entry.delete("1.0", tk.END)
        plaintext_entry.insert("1.0", plaintext)
        global result
        result=2
        messagebox.showinfo("Decrypt", "Text Decrypted!")
    except ValueError as error:
        messagebox.showerror("Error", str(error))

def copy_to_clipboard():
    try:
        global result
        if result == 1 :
            ciphertext = ciphertext_entry.get("1.0", tk.END).strip()
            if not ciphertext:
                raise ValueError("Nothing to copy")
            else:
                root.clipboard_clear()
                root.clipboard_append(ciphertext)
                messagebox.showinfo("Copy", "Copied to clipboard!")
        elif result == 2 :
            plaintext = plaintext_entry.get("1.0", tk.END).strip()
            if not plaintext:
                raise ValueError("Nothing to copy")
            else:
                root.clipboard_clear()
                root.clipboard_append(plaintext)
                messagebox.showinfo("Copy", "Copied to clipboard!")
        else :
            raise ValueError("Nothing to copy")
    except ValueError as error:
        messagebox.showerror("Error", str(error))

root = tk.Tk()
root.title("Caesar Cipher")

result=0

plaintext_label = tk.Label(root, text="Plain Text :")
plaintext_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

plaintext_entry = tk.Text(root, height=5)
plaintext_entry.grid(row=1, column=0, padx=5, pady=5)

shift_label = tk.Label(root, text="Shift Key :")
shift_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="nswe")

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=1, padx=5, pady=5, sticky="ns")

ciphertext_label = tk.Label(root, text="Cipher Text :")
ciphertext_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ciphertext_entry = tk.Text(root, height=5)
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
