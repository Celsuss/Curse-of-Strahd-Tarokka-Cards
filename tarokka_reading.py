import tkinter as tk
# pip install pillow
from PIL import Image, ImageTk
import glob
import os

def setupWindow():
    window = tk.Tk(className="curse of strahd tarokka cards reading")

    greeting = tk.Label(text="Curse of Strahd Tarokka Cards Reading")
    greeting.pack()

    button = tk.Button(text="Do Reading")
    button.pack()

    return window

def getImages(path='images/', extensions=['png', 'jpg']):
    mask = os.path.join(path, ('*.' + str([e for e in extensions]) + '*'))
    file_paths = glob.glob(mask)
    return 0

def main():
    getImages()

    window = setupWindow()
    window.mainloop()


    return 0

if __name__ == '__main__':
    main()