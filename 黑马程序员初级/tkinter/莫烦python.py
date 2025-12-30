import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x200")

var = tk.StringVar()
l = tk.Label(window, textvariable=var,background="green",font=("Arial",24),width=15,height=2)
l.pack()
on_hit = False

def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me!',width=15,height=2,command=hit_me)
b.pack()
window.mainloop()
