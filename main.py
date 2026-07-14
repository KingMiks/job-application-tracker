import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

# Headers
headers = [
    "Company",
    "Role",
    "Job link",
    "Status",
    "Date applied",
    "Follow-up Date",
    "Notes",
]

# Helper Functions
def save_to_json():
    columns = tree["columns"]

    rows = []

    for row in tree.get_children():
        row_values = tree.item(row, "values")
        rows.append(dict(zip(columns, row_values)))
        
    
    try:
        with open("jobs.json", "w", encoding="utf-8") as file:
            json.dump(rows, file, indent=4)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")
        return False

def load_from_json():
    try:
        with open("jobs.json", "r", encoding="utf-8") as file:
            rows = json.load(file)

        # Wipe out UI clean before populating
        for item in tree.get_children():
            tree.delete(item)

        columns = tree["columns"]

        # Re-populate from JSON
        for row_dict in rows:
            row_values = [row_dict.get(col, "") for col in columns]
            tree.insert("", index="end", values=row_values)
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Load failed: {e}")

def clear_entries():
    company_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)
    job_link_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)
    date_applied_entry.delete(0, tk.END)
    follow_up_date_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)


# Create a window
window = tk.Tk()

tree = ttk.Treeview(window, columns=headers, show="headings")
tree.grid(row=10, column=0, sticky='w')

window.title("Job Application Tracker")
window.minsize(width=800, height=600)

for column in headers:
    tree.column(column, width=140)
    tree.heading(column, text=column)

# Loads current json file
load_from_json()

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

    job_data = [company, role, job_link, status, date_applied, follow_up_date, notes]

    if not all(job_data):
        messagebox.showerror(title="ERROR: EMPTY FIELD", 
                             message="Please complete every field.")
        return 
    tree.insert(parent= "", index="end", values=job_data)
    
    if save_to_json():
        clear_entries()

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
def delete_job():
    selected_rows = tree.selection()

    if not selected_rows:
        messagebox.showerror(title="ERROR: NO DATA SELECTED", 
                             message="Please select a data entry.")
        return 

    tree.delete(*selected_rows)
    save_to_json()

def update_job():
    selected_rows = tree.selection()

    if len(selected_rows) != 1:
        messagebox.showerror(
            title="ERROR: INVALID SELECTION",
            message="Please select exactly one job to update."
        )
        return
    update_row = selected_rows[0]

    # Extract fresh text
    new_company = company_entry.get().strip()
    new_role = role_entry.get().strip()
    new_job_link = job_link_entry.get().strip()
    new_status = status_entry.get().strip()
    new_date_applied = date_applied_entry.get().strip()
    new_follow_up_date = follow_up_date_entry.get().strip()
    new_notes = notes_entry.get().strip()

    updated_data = [
        new_company,
        new_role,
        new_job_link,
        new_status,
        new_date_applied,
        new_follow_up_date,
        new_notes,
]

    if not all(updated_data):
        messagebox.showerror(
            title="ERROR: EMPTY FIELD",
            message="Please complete every field."
        )
        return
    tree.item(update_row, values=updated_data)
    if save_to_json():
        clear_entries()

# Save job

save_button = tk.Button(form_frame, text="Save Job", command=save_job)
save_button.grid(row=9)
update_button = tk.Button(form_frame, text="Update Job", command=update_job)
update_button.grid(row=9, column=1)
delete_button = tk.Button(form_frame, text="Delete Job", command=delete_job)
delete_button.grid(row=9, column=2)





window.mainloop()