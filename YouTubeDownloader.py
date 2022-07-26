from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def download():
    link = link_input.get()
    
    if len(link) == 0:
        messagebox.showwarning(title="Field Empty", message="Put a link in the text box before pressing 'Download'")
    else:
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        ys.download()
        print("Download Completed!")

window = Tk()
window.title("YouTube Video Downloader")
window.config(padx=50,pady=50)

link_input = Entry()
link_input.grid(column=0,row=0)

download_button = Button(text="Download", command = download)
download_button.grid(column=0,row=1)




window.mainloop()