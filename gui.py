import requests as requests
import json
import tkinter as tk

from english_engish_dictionary import query_word

icon_path = "C:/workspace/github/quickDictionary/dictionary.bmp"
def ask_word():
    master = tk.Tk()
    master.title('')
    master.iconbitmap(icon_path)
    def handler(e):
        master.quit()
    master.bind('<Return>', handler)#lambda x: master.quit)
    tk.Label(master, text="word").grid(row=0)

    e1 = tk.Entry(master)
    e1.icursor(1)
    e1.grid(row=0, column=1)

    tk.Button(master,text='OK',command=master.quit).grid(row=3,column=0,sticky=tk.W,pady=4)

    master.mainloop()
    word = e1.get()
    try:
        master.destroy()
        return word
    except:
        return word

def show_word(word):
    definition_list = query_word(word)

    master = tk.Tk()
    master.title('')
    master.iconbitmap(icon_path)
    def handler(e):
        master.quit()
    master.bind('<Return>', handler)

    definitions= ""
    rowIdx = 0
    for d in definition_list:
        # definitions = definitions + "\n\n"+ d
        tk.Label(master, text=d, wraplength = 500, anchor='w').grid(row=rowIdx, column=0, columnspan=2)
        rowIdx += 1
    e2 = tk.Entry(master)
    e2.grid(row=rowIdx, column=0, columnspan=2)
    rowIdx += 1
    tk.Button(master, text='OK', command=master.quit).grid(row=rowIdx, column=1, sticky=tk.W, pady=4)
    master.mainloop()
    summary=""
    try:
        summary = e2.get()
        master.destroy()
        return summary
    except:
        return summary

def ok_no_msgbox(question):
    master = tk.Tk()
    master.title('')
    master.iconbitmap(icon_path)
    tk.Label(master, text=question).grid(row=0)
    def yes():
        master.quit()
    def no():
        master.quit()
        master.destroy()
    def handler(e):
        master.quit()
    master.bind('<Return>', handler)
    tk.Button(master, text='OK', command=yes).grid(row=1, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='NO', command=no).grid(row=1, column=1, sticky=tk.W, pady=4)
    master.mainloop()
    try:
        master.destroy()
        return True
    except:
        return False