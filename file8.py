from tkinter import *
root = Tk()
n = 0
def click_handler():
    global n, lable
    n += 1
    lable.destroy()
    lable = Label(root, text = f'Hello {n}')
    lable.pack()
btn = Button(root, text = 'Click Me!', command = click_handler)
btn.pack()
lable = Label(root, text = f'Hello {n}')
lable.pack()
root.mainloop()
