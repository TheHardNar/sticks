from tkinter import *
import random as r
window = Tk()
window.geometry('400x300')
window.title('sticks')
window.resizable(False, False)
def player():
    global sticks
    if entry_sticks.get() == '':
        pass
    else:
        delete_sticks = entry_sticks.get()
        a = int(delete_sticks)
        if delete_sticks in '1 2 3' and a < sticks and sticks != 1:
            sticks = sticks - a
            label_sticks.config(text=sticks*'|')
            status.config(text=sticks)
            if sticks != 1:
                label_move.config(text="Computer's turn, please wait...")
                window.after(2000, computer)
                button.config(state = DISABLED)
    if sticks == 1:
        status.config(text='You win!', fg = 'green')
        button.config(state = DISABLED)
    
def computer():
    global sticks

    if sticks == 4:
        sticks = sticks - 3
    elif sticks == 3:
        sticks = sticks - 2
    elif sticks == 2:
        sticks = sticks - 1
    else:
        a = r.randint(1,3)
        sticks = sticks - a
    label_move.config(text='Input number between 1 to 3')
    label_sticks.config(text=sticks*'|')
    status.config(text=sticks)
    button.config(state = NORMAL)
    if sticks == 1:
        status.config(text='Computer won!', fg = 'red')
        button.config(state = DISABLED)
    
    
sticks = 20
label_move = Label(text='Input number between 1 to 3', font=('Arial', 15, 'bold'))
entry_sticks = Entry(font=('Arial', 15, 'bold'), justify = 'center')
label_sticks = Label(text=sticks*'|', font=('Arial', 30, 'bold'))
status = Label(text=str(sticks), font=('Arial', 30, 'bold'))
button = Button(text='Take sticks', font=('Arial', 15, 'bold'), command = player)
label_move.pack(pady=7)
entry_sticks.pack(pady=7)
label_sticks.pack(pady=7)
status.pack(pady=7)
button.pack(pady=7)

window.mainloop()
