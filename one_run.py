from tkinter import *
import time



window = Tk(className='Matty Project')
window.geometry("400x400")
window['bg'] = 'red'
count = 0


def update():
    global count
    if count == 10:
        window.destroy()
        return
    if window['bg'] == 'red':
        window['bg'] = 'green'
        count += 1
        window.after(5000, update)
    else:
        window['bg'] = 'red'

        window.after(3000, update)
update()
window.mainloop()
