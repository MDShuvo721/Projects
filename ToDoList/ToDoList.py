from tkinter import *
from datetime import date
import calendar

def current_month():
    td = date.today()
    
    cMonth = td.month
    cYear = td.year

    month = calendar.monthcalendar(cYear, cMonth)

    # Build the calendar string
    calendar_str = f"{calendar.month_name[cMonth]} {cYear}\n"

    for week in month:
        for day in week:
            if day == 0:
                calendar_str += "   "  # Empty space for days outside the current month
            else:
                if day == td.day:
                    calendar_str += f"[{day:2}]"  # Mark today's day
                else:
                    calendar_str += f" {day:2} "  # Regular day
        calendar_str += "\n"  # Move to the next line after each week
    
    return calendar_str

window = Tk()

window.title("To Do List")
window.geometry("800x450")

window.config(background="#f3e2cd")

top_label = Label(window, text=current_month(), 
                  font=("Courier", 14), padx=10, pady=10,
                  background="#f3e2cd", foreground="green"
                  )

top_label.pack()


window.mainloop()