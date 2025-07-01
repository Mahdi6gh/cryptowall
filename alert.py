import tkinter as tk
def do():
    def disable_event():
        pass  # این باعث میشه Alt+F4 یا بستن با ضربدر غیرفعال بشه

    root = tk.Tk()
    root.attributes("-fullscreen", True)  # حالت تمام‌صفحه
    root.protocol("WM_DELETE_WINDOW", disable_event)  # غیرفعال کردن بستن با ضربدر
    root.bind("<Escape>", lambda e: None)  # غیرفعال کردن Esc

    # ساخت یک نوشته وسط صفحه
    label = tk.Label(root, text="Your pc is locked")
    label.pack(expand=True)

    root.mainloop()
