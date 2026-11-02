import tkinter as tk
import wordSearching
import time
import os
from pathlib import Path 
output_folder = Path("detected_words")
output_folder.mkdir(parents=True, exist_ok=True)

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

def run_word_search():
    entry_list = lb.get(0, tk.END)
    results = wordSearching.word_search(entry_list)
    results.show(results)

button = tk.Button(root, text="Test Run", width=25, command = run_word_search)
button.pack()
#Most important part


time_left = 0
images_saved = 0   
is_running = False
def start_program():
    global is_running
    global time_left
    global images_saved
    
    start_button.configure(text = "Stop", command = stop_program)
    if is_running == False:
        is_running = True
        time_left = 0
        photos_taken = 0
        program_run()

def program_run():
    
    global is_running
    global time_left
    global images_saved
    entry_list = lb.get(0, tk.END)
    if is_running == True:
        status.configure(text="Time till next scan: "+str(time_left)+"    Images detected: "+str(images_saved))
        print(time_left)
        if time_left <= 0:
            results = wordSearching.word_search(entry_list)
            if results:
                print("A word was found")
                images_saved += 1
                file_name = "word_detected("+str(images_saved)+").png"
                output_path = output_folder / file_name
                results.save(output_path)
                time_left = 60
        elif time_left > 0:
                time_left -= 1
        root.after(1000, program_run)
    

def stop_program():
    global is_running
    start_button.configure(text = "Start", command = start_program)

    if is_running:
        is_running = False
        print("Stopped")


start_button = tk.Button(root, text="Start", width=25, command = start_program)
start_button.pack()

status = tk.Label(root, text="Time till next scan: n/a    Images detected: n/a")
status.pack()

def open_folder():
    os.startfile(output_folder)

show_results_button = tk.Button(root, text="Open Output Folder", width=25, command = open_folder)
show_results_button.pack()

root.mainloop()