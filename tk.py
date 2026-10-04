import tkinter as tk

#bikin jendela utama
window = tk.Tk()
window.title("Login")
window.geometry("250x180")

window.configure(bg="#469CBE")

#buat label dan entry untuk username/]
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5 )

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

#buat label dan entry untuk password
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

#buat tombol login
button_login = tk.Button(window, text="Login")
button_login.pack(pady=10)

window.mainloop()
