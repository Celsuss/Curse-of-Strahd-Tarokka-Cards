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

def getImagesPaths(common_path='images/common/', high_path='images/high/', extensions=['png', 'jpg']):
    common_file_mask = os.path.join(common_path, ('*.' + str([e for e in extensions]) + '*'))
    high_file_mask = os.path.join(common_path, ('*.' + str([e for e in extensions]) + '*'))

    # file_paths = glob.glob(file_mask)
    file_paths = {'common': glob.glob(common_file_mask), 'high': glob.glob(high_file_mask)}
    return file_paths

def main():
    images_paths = getImagesPaths()

    window = setupWindow()
    window.mainloop()


    return 0

if __name__ == '__main__':
    main()