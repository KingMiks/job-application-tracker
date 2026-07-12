import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Create a window
window = tk.Tk()

headers = [
    "Company",
    "Role",
    "Job link",
    "Status",
    "Date applied",
    "Follow-up Date",
    "Notes",
]

tree = ttk.Treeview(window, columns=headers, show="headings")
tree.grid(row=10, column=0, sticky='w')

window.title("Job Application Tracker")
window.minsize(width=800, height=600)

for column in headers:
    seperator = ttk.Separator()
    tree.column(column, width=140)
    tree.heading(column, text=column)

form_frame = tk.Frame(window)
form_frame.grid(row=0, column=0, sticky="w")

label = tk.Label(form_frame, text="Job Application Tracker")
label.grid(row=1)

company_label = tk.Label(form_frame, text="Company: ")
company_label.grid(row=2, column=0, sticky='w')

role_label = tk.Label(form_frame, text= "Role: ")
role_label.grid(row=3, column=0, sticky='w')

job_link_label = tk.Label(form_frame, text="Job Link: ")
job_link_label.grid(row=4,column=0, sticky='w')

status_label = tk.Label(form_frame, text="Job Status: ")
status_label.grid(row=5, column=0, sticky='w')

date_applied_label = tk.Label(form_frame, text="Date Applied: ")
date_applied_label.grid(row=6, column=0, sticky='w')

follow_up_date_label = tk.Label(form_frame, text="Follow up Date: ")
follow_up_date_label.grid(row=7, column=0, sticky='w')

notes_label = tk.Label(form_frame, text="Notes: ")
notes_label.grid(row=8, column=0, sticky='w')

# Button clickers
def save_job():

    company = company_entry.get().strip()
    role = role_entry.get().strip()
    job_link = job_link_entry.get().strip()
    status = status_entry.get().strip()
    date_applied = date_applied_entry.get().strip()
    follow_up_date = follow_up_date_entry.get().strip()
    notes = notes_entry.get().strip()

    required_fields = [company, role, job_link, status, date_applied, follow_up_date, notes]

    if not all(required_fields):
        messagebox.showerror(title="ERROR EMPTY FIELD", 
                             message="Please enter valid company or role")
        return 

    company_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)
    job_link_entry.delete(0, tk.END)
    status_entry.delete(0,tk.END)
    date_applied_entry.delete(0, tk.END)
    follow_up_date_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)

    tree.insert(company, role, job_link, status, date_applied, follow_up_date, notes)

# Entries

company_entry = tk.Entry(form_frame, width=70)
company_entry.grid(row=2, column=1)

role_entry = tk.Entry(form_frame, width=70)
role_entry.grid(row=3, column=1)

job_link_entry = tk.Entry(form_frame, width=70)
job_link_entry.grid(row=4, column=1)

status_entry = tk.Entry(form_frame, width=70)
status_entry.grid(row=5, column=1)

date_applied_entry = tk.Entry(form_frame, width=70)
date_applied_entry.grid(row=6, column=1)

follow_up_date_entry = tk.Entry(form_frame, width=70)
follow_up_date_entry.grid(row=7, column=1)

notes_entry = tk.Entry(form_frame, width=70)
notes_entry.grid(row=8, column=1)

# Buttons

# Save job

save_job_button = tk.Button(form_frame, text= "Save job", command=save_job)
save_job_button.grid(row=9)





window.mainloop()