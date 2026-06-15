import tkinter as tk
from tkinter import messagebox

# Create a window
window = tk.Tk()

window.title("Job Application Tracker")
window.minsize(width=800, height=600)

label = tk.Label(window, text="Job Application Tracker")
label.grid(row=0)


company_label = tk.Label(window, text="Company: ")
company_label.grid(row=2)

role_label = tk.Label(window, text= "Role: ")
role_label.grid(row=4)

status_label = tk.Label(window, text="Job Status: ")
status_label.grid(row=5)

next_row = 10

# Button clickers
def save_job():
    global next_row

    company = company_entry.get().strip()
    role = role_entry.get().strip()
    status = status_entry.get().strip()

    required_fields = [company, role, status]

    if not all(required_fields):
        messagebox.showerror(title="ERROR EMPTY FIELD", 
                             message="Please enter valid company or role")
        return 

    company_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)
    status_entry.delete(0,tk.END)

    job_label = tk.Label(window, text=f"{company} | {role} | {status}")
    job_label.grid(row=next_row, column=0, columnspan=2)
    next_row +=1

# Entries

company_entry = tk.Entry(window, width=30)
company_entry.grid(row=2, column=1)

role_entry = tk.Entry(window, width=30)
role_entry.grid(row=4, column=1)

status_entry = tk.Entry(window, width=30)
status_entry.grid(row=5, column=1)

# Buttons

# Save job

save_job_button = tk.Button(window, text= "Save job", command=save_job)
save_job_button.grid(row=7)





window.mainloop()