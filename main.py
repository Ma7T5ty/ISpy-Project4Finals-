import tkinter as tk
import pyscreenshot
# Capture the full screen
image = pyscreenshot.grab()

image.show()

root = tk.Tk()
root.title("ISPY")
# Widgets are added here

instructions = tk.Label(root, text="Insert Wanted Words")
instructions.pack()

def insert_word():
    user_input = entry1.get()
    if find_entry(user_input) == -1:
        lb.insert(1, user_input)
    else:
        print(user_input+" is already recorded")

def delete_word():
    user_input = entry1.get()
    index = find_entry(user_input)
    if index == -1:
        print(user_input+" does not exist")
    else:
        lb.delete(index)
        

entry1 = tk.Entry(root)
entry1.pack()

button = tk.Button(root, text="Insert", width=25, command = insert_word)
button.pack()
button = tk.Button(root, text="Delete", width=25, command = delete_word)
button.pack()


def on_select(event):
    # event.widget refers to the listbox that triggered the event
    w = event.widget
    if w.curselection():
        index = w.curselection()[0]
        value = w.get(index)
        entry1.delete(0, tk.END)
        entry1.insert(0, value)


lb = tk.Listbox(root)
lb.insert(1, "Test")
lb.pack()
lb.bind('<<ListboxSelect>>', on_select)

def find_entry(search_text):
    entry_list = lb.get(0, tk.END)
    try:
        return entry_list.index(search_text)
    except ValueError:
        return -1

root.mainloop()