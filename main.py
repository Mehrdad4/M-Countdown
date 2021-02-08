from tkinter import Label, Button, Entry, StringVar, END, Tk
t = 0
def set_timer():
    global t
    t = t + int(en1.get())
    en1.delete(0, END)
    return t
def countdown():
    global t
    if t > 0:
        lb1.configure(text = t)
        t = t - 1
        lb1.after(1000, countdown)
    elif t == 0:
        lb1.configure(text = 'finish')

root = Tk()
root.geometry('228x228')
lb1 = Label(root, font = 'times 20')
lb1.grid(row = 1, column = 2)
times = StringVar()
en1 = Entry(root, textvariable = times)
en1.grid(row = 3, column = 2)
bu1 = Button(root, text = 'Set', width = 20, command = set_timer)
bu1.grid(row = 4, column = 2, padx = 20)
bu2 = Button(root, text = 'Start', width = 20, command = countdown)
bu2.grid(row = 6, column = 2, padx = 20)
root.mainloop()
