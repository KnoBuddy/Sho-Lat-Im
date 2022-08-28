from tkinter import *
from tkinter import ttk
import json5 as json
import os
import sys
import glob
from PIL import Image

# Definte your directory
# My default is ./samples/
dir = './samples/'

window = Tk()

window.title("Latest Sample")
master_frame = ttk.Frame(window)
master_frame.pack(expand=True, fill=BOTH)

def show_image():
    global list_of_folders
    global latest_folder
    global list_of_files
    global latest_file
    global sample

    list_of_folders = glob.glob(dir+'*') # * means all if need specific format then *.csv
    latest_folder = max(list_of_folders, key=os.path.getctime)
    list_of_files = glob.glob('./'+latest_folder+'/*.png') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    sample = latest_file
    try:
        im = Image.open(sample)
    except:
        print("No Sample")
        image = Image.new('RGB', (512, 512), (255, 255, 255))
        image.save(sample)
        im = Image.open(sample)
    global h
    global w
    h = im.size[1]
    w = im.size[0]
    global image_window
    image_window = ttk.Frame(master_frame, width=w, height=h)
    image_window.pack()
    global canvas
    canvas = Canvas(image_window, width=w, height=h)
    global img
    global image_container
    try:
        img = PhotoImage(file=sample)
    except:
        image = Image.new('RGB', (512, 512), (255, 255, 255))
        image.save(sample)
    image_container = canvas.create_image(0,0, anchor="nw",image=img)
    canvas.pack()
    updater()

# Function to refresh the image in the GUI

def refresh_image():
    updater()
    global list_of_folders
    global latest_folder
    global list_of_files
    global latest_file
    global sample

    list_of_folders = glob.glob(dir+'*') # * means all if need specific format then *.csv
    latest_folder = max(list_of_folders, key=os.path.getctime)
    list_of_files = glob.glob('./'+latest_folder+'/*.png') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    sample = latest_file
    try:
        im = Image.open(sample)
        global h
        global w
        if h != im.size[1] or w != im.size[0]:
            h = im.size[1]
            w = im.size[0]
            image_window.config(width=w, height=h)
        global img
        global image_container
        global canvas
        img = PhotoImage(file=sample)
        canvas.config(width=w, height=h)
        canvas.itemconfig(image_container, image = img)
        canvas.pack()
        global has_run
        has_run = True
    except:
        pass


def updater():
    window.after(1000, refresh_image)

show_image()

mainloop()
