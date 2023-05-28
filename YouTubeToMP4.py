### This is my first project with Python.

from pytube import YouTube
import customtkinter as ck
from tkinter import *
from PIL import ImageTk, Image
import requests
from tkinter import filedialog
from tkinter import messagebox

root = ck.CTk()
root.title("Youtube Downloader")
root.geometry("720x480")

ck.set_appearance_mode("System")
ck.set_default_color_theme("blue")


welcomelabel = ck.CTkLabel(root, text="YouTube Downloader v1.0 by LorenzoProjex")
welcomelabel.pack()

video_link = ck.StringVar(root)
video_quality = ck.StringVar(root)
save_directory = ck.StringVar(root)


def select_save_directory():
    directory = filedialog.askdirectory()
    save_directory.set(directory)

def download_video():
    link = video_link.get()
    directory = save_directory.get()
    if not directory:
        messagebox.showerror("Error", "Please select a save directory.")
        return

    yt = YouTube(link)
    download = yt.streams.get_highest_resolution()
    download_path = download.download(output_path=directory)
    messagebox.showinfo("Download Complete", "Download has completed successfully!")


def see_video_details():
    link = video_link.get()
    yt = YouTube(link)
    details = ("Title: " + yt.title)
    video_details_label.configure(text=details)

    img = Image.open(requests.get(yt.thumbnail_url, stream=True).raw)
    img = img.resize((320, 180))  # Resize the image as desired
    thumbnail = ImageTk.PhotoImage(img)
    thumbnail_label.config(image=thumbnail)
    thumbnail_label.image = thumbnail  # Store a reference to avoid garbage collection


type_URL = ck.CTkLabel(root, text="Enter URL below: ")
type_URL.pack()

urlentry = ck.CTkEntry(root, placeholder_text="Type your URL:", textvariable= video_link)
urlentry.pack(ipadx = 100)

save_directory_label = ck.CTkLabel(root, text="Save To:")
save_directory_label.pack()

select_directory_button = ck.CTkButton(root, text="Browse...", command=select_save_directory)
select_directory_button.pack()

save_directory_entry = ck.CTkEntry(root, textvariable=save_directory)
save_directory_entry.pack()

button_frame = ck.CTkFrame(root)
button_frame.pack(pady=10)

see_details = ck.CTkButton(button_frame, text="See Video Details", command=see_video_details)
see_details.pack(side = LEFT)

download_button = ck.CTkButton(button_frame, text="Download Video", command=download_video)
download_button.pack(side = RIGHT)

video_details_label = ck.CTkLabel(root, text="")
video_details_label.pack()

# Create a label for displaying the thumbnail image
thumbnail_label = Label(root)
thumbnail_label.pack()

root.mainloop()