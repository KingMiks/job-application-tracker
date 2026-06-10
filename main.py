from tkinter import *

# Create a window
window = Tk()

window.title("Job Application Tracker")
window.minsize(width=800, height=600)

label = Label(window, text="Job Application Tracker")
label.grid(row=0)


company_label = Label(window, text="Company:")
company_label.grid(row=2)

role_label = Label(window, text= "Role:")
role_label.grid(row=4)

next_row = 6

# Button clickers
def save_job():
    global next_row

    company = company_entry.get()
    role = role_entry.get()

    job_label = Label(window, text=f"{company} | {role}")
    job_label.grid(row=next_row, column=0, columnspan=2)

    next_row +=1

# Entries

company_entry = Entry(window, width=30)
company_entry.grid(row=2, column=1)

role_entry = Entry(window, width=30)
role_entry.grid(row=4, column=1)

# Buttons

# Save job

save_job_button = Button(window, text= "Save job", command=save_job)
save_job_button.grid(row=5)





window.mainloop()