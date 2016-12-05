from tkinter import *

root = Tk()
root.configure(background = "#fff")
root.geometry("500x500")

title = Label(root, text = "Line Sticker Downloader", bg = "#fff",
                font = (None, 20))
inputText = Label(root, text = "Enter the sticker pack ID: ", font = (None, 12))
inputUser = Entry(root, bd = 2)


title.pack(anchor = CENTER)
inputText.pack(side = LEFT, anchor = 'n')
inputUser.pack(side = RIGHT, anchor = 'n')
root.mainloop()
