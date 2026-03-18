from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Search")
root.geometry('900x600')

# background image
bg_img = Image.open("hoho.jpg") 
bg_img = bg_img.resize((900, 600))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# LEFT-MIDDLE FRAME positioned with padding to avoid overlap
frame = Frame(root, bg="")
frame.place(x=30, y=250)  # 30 pixels from left, 250 from top (adjust as needed)

# search icon
icon_img = Image.open("search.png")
icon_img = icon_img.resize((18, 18))
search_icon = ImageTk.PhotoImage(icon_img)

def search(event=None):
    query = search_entry.get()
    if query != "" and query != "Search...":
        print("Searching for:", query)

# search bar frame
search_frame = Frame(frame, bg="white", bd=1, relief="solid")
search_frame.pack()

# icon
icon_label = Label(search_frame, image=search_icon, bg="white")
icon_label.pack(side=LEFT, padx=8)

# entry
search_entry = Entry(search_frame,
                     font=('Arial', 15),
                     bd=0,
                     width=28,
                     fg="grey")
search_entry.pack(side=LEFT, ipady=6, padx=5)

def on_click(event):
    if search_entry.get() == "Search...":
        search_entry.delete(0, END)
        search_entry.config(fg="black")

def on_leave(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Search...")
        search_entry.config(fg="grey")

search_entry.insert(0, "Search...")
search_entry.bind("<FocusIn>", on_click)
search_entry.bind("<FocusOut>", on_leave)

search_entry.bind("<Return>", search)

root.mainloop()





