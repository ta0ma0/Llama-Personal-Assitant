import tkinter as tk


def answer_window(text_data):
    window = tk.Tk()
    window.geometry("700x400")
    window.title("Llama answer")
    window1 = tk.Text(window, height=350, width=550)
    window1.insert(tk.END, text_data)
    window1.tag_add("start", "1.0")
    window1.tag_config("start", font="Ubuntu")
    window1.pack()
    window.mainloop()


def auto_close_window(text_data):
    win = tk.Tk()
    win.geometry("420x150")
    win.title("Question")
    tk.Label(win, text=text_data, font=('Helvetica 12')).pack(pady=20)
    win.after(3000,lambda:win.destroy())
    win.mainloop()
