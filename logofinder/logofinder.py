from tkinter import *
from google_images_download import google_images_download
#logo finder
def find():
    downloader = google_images_download.googleimagesdownload()
    args = {"keywords": textentry.get() + " logo", "limit": "1", "size": "icon", "print_urls": True, "format": "png"}
    paths = list(downloader.download(args))
    path = list(paths[0].values())[0][0].replace("\\", "/")
    newlogo = PhotoImage(file = path)
    logolabel.configure(image = newlogo)
    logolabel.photo = newlogo
#window config
window = Tk()
window.title("Logo finder")
window.iconbitmap("images\logologo.ico")
window.configure(bg = "#FFFFFF", padx = "5", pady = "5")
#window.resizable(0, 0)
#label
Label(window, text = "Enter a company name to find its logo.", bg = "#FFFFFF", fg = "#000000", font = "none 11").grid(row = 0, column = 0, sticky = W)
#text entry
textentry = Entry(window, width = 42, bg = "#FFFFFF", fg = "#0A0908")
textentry.grid(row = 2, column = 0, sticky = W)
#enter button
Label(window, text = "\n", bg = "#ffffff", font = "none 1").grid(row = 3, column = 0, sticky = W)
Button(window, text = "Find logo", width = 8, command = find, relief = "flat", bg = "#0080ff", fg = "#F2F4F3", borderwidth = "0", activebackground = "#0080ff", activeforeground = "#F2F4F3").grid(row = 4, column = 0, sticky = W)
#logo
logo = PhotoImage(file = "images\prelogo.png")
Label(window, text = "\n", bg = "#ffffff", font = "none 1").grid(row = 5, column = 0, sticky = W)
logolabel = Label(window, image = logo, bg = "#FFFFFF")
logolabel.grid(row = 6, column = 0, sticky = W)
#initialize window
window.mainloop()