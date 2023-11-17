import cv2
import os
import tkinter as tk
from tkinter import filedialog

def encrypt_message():
    global img, msg, password, d, c

    img = cv2.imread("lion.jpg")  # filepath
    msg = entry_message.get()
    password = entry_password.get()

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)
    os.system("start Encryptedmsg.jpg")


def decrypt_message():
    global img, msg, password, d, c

    message = ""
    n = 0
    m = 0
    z = 0

    pas = entry_decrypt_password.get()

    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        result_label.config(text="Decrypted msg: " + message, fg="green")
    else:
        result_label.config(text="Password not valid", fg="red")


# Create the main window
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Define colors
bg_color = "#2c3e50"  # dark blue
text_color = "#ecf0f1"  # light gray
button_bg = "#3498db"  # blue
button_fg = "white"

# Configure window background color
root.configure(bg=bg_color)

# Create GUI elements with colors
label_message = tk.Label(root, text="Enter Your Secret Message:", bg=bg_color, fg=text_color)
entry_message = tk.Entry(root)
label_password = tk.Label(root, text="Enter Your Password:", bg=bg_color, fg=text_color)
entry_password = tk.Entry(root, show="*")
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, bg=button_bg, fg=button_fg)

label_decrypt_password = tk.Label(root, text="Enter Your Password for decryption:", bg=bg_color, fg=text_color)
entry_decrypt_password = tk.Entry(root, show="*")
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, bg=button_bg, fg=button_fg)
result_label = tk.Label(root, text="Decrypted msg: ", bg=bg_color, fg=text_color)

# Place GUI elements on the window
label_message.pack(pady=5)
entry_message.pack(pady=5)
label_password.pack(pady=5)
entry_password.pack(pady=5)
encrypt_button.pack(pady=10)

label_decrypt_password.pack(pady=5)
entry_decrypt_password.pack(pady=5)
decrypt_button.pack(pady=10)
result_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
