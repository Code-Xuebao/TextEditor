from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
import re, base64, os
from icon import img

root = Tk()
root.geometry("500x400")
root.title("Text Editor")
with open('TextEditor.ico', 'wb+') as ico:
    ico.write(base64.b64decode(img))
root.iconbitmap('TextEditor.ico')
os.remove('TextEditor.ico')

text_editor = Text(root, font=("Comfortaa", 14))
text_editor.pack(fill=BOTH, expand=True)
def new_file():
    text_editor.delete("1.0", END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as f:
            text_editor.insert(END, f.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_editor.get("1.0", END))

def find_and_replace():
    
    search_str = simpledialog.askstring("Find and Replace", "Enter text to find:")
    if search_str:
        replace_str = simpledialog.askstring("Find and Replace", "Enter replacement text:")
        if replace_str:
            
            idx = "1.0"
            while True:
                match = re.search(r"\b" + search_str + r"\b", text_editor.get(idx, END))
                if not match:
                    messagebox.showinfo("Result", "No more matches")
                    break
                start_idx = f"{idx}+{match.start()}c"
                end_idx = f"{idx}+{match.end()}c"
                
                text_editor.delete(start_idx, end_idx)
                text_editor.insert(start_idx, replace_str)
                
                idx = start_idx

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Find and Replace", command=find_and_replace)

root.mainloop()