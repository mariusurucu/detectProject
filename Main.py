import tkinter as tk

import os
from PIL import Image, ImageTk



def callFaceDetectFromImage():
    from detectProject import FaceDetectFromImage
    FaceDetectFromImage


def callLive():
    from detectProject import live
    live


def callVideoMethod1():
    from detectProject import read_frames_fast
    read_frames_fast

def callVideoMethod2():
    from detectProject import read_frames_slow
    read_frames_slow


root = tk.Tk()
root.title("Test")
image = Image.open("D:/downloads/lionlogo.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root,
         text="Face Detection:",
         padx=20).pack()
tk.Label(root,
         text="~Proiect 2 2017-2018~",
         padx=20).pack()
tk.Label().pack()
tk.Label().pack()

tk.Label(root, text="Image Detection", padx=20).pack()
tk.Button(root, text="Image", width=10, command=callFaceDetectFromImage).pack(anchor=tk.CENTER)
tk.Label().pack()

tk.Label(root, text="Live Detection", padx=20).pack()
tk.Button(root, text="Live", width=10, command=callLive).pack(anchor=tk.CENTER)
tk.Label().pack()

tk.Label(root, text="Video Method 1 Detection", padx=20).pack()
tk.Button(root, text="Video1", width=10, command=callVideoMethod1).pack(anchor=tk.CENTER)
tk.Label().pack()

tk.Label(root, text="Video Method 2 Detection", padx=20).pack()
tk.Button(root, text="Video2", width=10, command=callVideoMethod2).pack(anchor=tk.CENTER)
tk.Label().pack()
tk.Label().pack()
tk.Label().pack()

tk.Label(root, text="By Urucu Marius 433A").pack(anchor=tk.S)
tk.Label(root, text="V1.0").pack(anchor=tk.SE)

root.geometry('{}x{}'.format(435, 435))
root.resizable(width=False, height=False)

root.mainloop()
