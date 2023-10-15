from tkinter import *
from tkinter import messagebox


def save_button():
    note = note_text.get("1.0", END)
    title = title_entry.get()

    if len(note) == 0 or len(title) == 0:
        messagebox.showinfo(title="ERROR!", message="please enter title and note!")
    else:
        try:
            with open("note.txt","a") as data_file:
                data_file.write(f"\n{title}\n{note}")
        except FileNotFoundError:
            with open("note.txt","a") as data_file:
                data_file.write(f"\n{title}\n{note}")
        finally:
            title_entry.delete(0,END)
            note_text.delete("1.0",END)




#GUİ
window = Tk()
window.title("NotePad")
window.geometry("218x361")
FONT = ("Verdena",15,"normal")

title_label = Label(text="Title=", font=FONT)
title_label.place(x=0,y=2)
#title_label.pack()

title_entry = Entry(width=10)
title_entry.place(x=45,y=2)
#title_entry.pack()

note_text = Text(width=30)
note_text.place(x=0,y=40)
#note_text.pack()

save_button = Button(text="Save", command=save_button)
save_button.place(x=150,y=0)
#save_button.pack()




window.mainloop()