import tkinter as interface
tp = interface.Tk()

put = interface.Entry(tp)
put.pack()

def who_is_Joe():
    name = put.get()
    name = name.lower()
    if name == 'joe':
        msg1 = interface.Label( tp, text ='Who is Joe?')
        msg1.pack()
    else:
        phrase = "Hello " + name
        msg2 = interface.Label( tp, text=phrase )
        msg2.pack()

Joebtn = interface.Button(tp, text="What's your name?", command=who_is_Joe)
Joebtn.pack()

tp.mainloop()
