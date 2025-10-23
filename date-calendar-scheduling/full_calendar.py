from tkinter import *
from tkinter import ttk
import calendar

def show_cal():
    new_window = Tk()
    new_window.config(background="white")
    new_window.title("Calendar")
    new_window.geometry("500x600")

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(
        new_window,
        text=cal_content,
        font="Consolas 10 bold"
    )
    cal_year.grid(row=6, column=1, padx=20)
    new_window.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.config(background="white")
    root.title("HOME")
    root.geometry("500x400")
    
    cal = Label(
        root,
        text="Welcome to the calendar application",
        bg="Green",
        font=("times", 20, "bold")
    )

    year = Label(
        root,
        text="Please enter a year",
        bg="Green"
    )
    year_field = Entry(root)

    Show = Button(
        root,
        text="Show Calendar",
        fg="Black",
        bg="Light Green",
        command=show_cal
    )
    Exit = Button(
        root,
        text="Exit",
        fg="Black",
        bg="Light Green",
        command=exit
    )

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    root.mainloop()