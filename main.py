import tkinter as tk
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as msb


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Notatnik")

        # tworzenie menu

        self.menu = tk.Menu(self.window)

        FileSubmenu = tk.Menu(self.menu, tearoff=0)
        EditSubmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Plik", menu=FileSubmenu)
        self.menu.add_cascade(label="Edytuj", menu=EditSubmenu)

        FileSubmenu.add_command(label="Nowy", command=self.newFile)
        FileSubmenu.add_command(label="Otwórz", command=self.open_file)
        FileSubmenu.add_command(label="Zapisz", command=self.save_file)
        FileSubmenu.add_separator()
        FileSubmenu.add_command(label="Exit", underline=0, command=self.onExit)

        EditSubmenu.add_command(label="Kopiuj", command=self.Copy)
        EditSubmenu.add_command(label="Wytnij", command=self.Cut)
        EditSubmenu.add_separator()
        EditSubmenu.add_command(label="Wklej", command=self.Paste)

        self.window.config(menu=self.menu, width=50, height=30)

        # dodawanie kontrolki typu Text i paska przewijania

        self.text = tk.Text(self.window)

        self.sb_text = tk.Scrollbar(self.window)
        self.sb_text.place(in_=self.text, relx=1., rely=0, relheight=1.)
        self.sb_text.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.sb_text.set)

        self.text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)

        self.window.mainloop()

    def open_file(self):
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # wywołanie okna dialogowego open file

        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")], defaultextension="*.txt")  # wywołanie okna dialogowego save file

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))

    def onExit(self):
        if msb.askokcancel("Czy jestes pewien", message="Czy napewno chcesz wyjść?\n niezapisany tekst zostanie utracony"):
            sys.exit()
        else:
            print("ok")

    def newFile(self):
        if msb.askokcancel("Czy jestes pewien", message="Czy napewno chcesz utworzyć nowy plik?\n niezapisany tekst zostanie utracony"):
            self.text.delete(1.0, tk.END)
        else:
            print("ok")

    def Copy(self):
        self.text.event_generate(("<<Copy>>"))

    def Cut(self):
        self.text.event_generate(("<<Cut>>"))

    def Paste(self):
        self.text.event_generate(("<<Paste>>"))


apl = Application()
