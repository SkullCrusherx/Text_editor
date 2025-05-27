from tkinter import Tk,Text,Button,Entry
from threading import Thread



def text_func():
    saveing_url = str(saving_place.get())
    with open(saveing_url+".txt", "w") as file:
        # Write the text to the file
        file.write(entry.get("1.0", "end-1c"))



root = Tk()
root.title('Text Writer')
root.geometry('800x500')
root.config(background='black')
entry = Text(root,fg = '#1af053',bg='black',insertbackground="#1af053",height=20,width=100)
entry.pack(pady=10,padx=5)
saving_place = Entry(root,fg = '#f70707',bg='black',insertbackground="#1af053")
saving_place.pack(pady=15)

Btn = Button(root, text = 'Save !', command = text_func,padx=20, pady=10)
Btn.pack(pady=20)

root.mainloop()