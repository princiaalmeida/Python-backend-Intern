import customtkinter as ctk
from tkinter import ttk, messagebox

# ======================
# SETTINGS
# ======================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ======================
# WINDOW
# ======================
root = ctk.CTk()
root.title("Student Grade Manager")
root.geometry("950x620")
root.resizable(False, False)

# macOS focus fix
root.lift()
root.attributes("-topmost", True)
root.after_idle(root.attributes, "-topmost", False)

students = []

# ======================
# GRADE FUNCTION
# ======================
def calculate_grade(marks):
    marks = float(marks)
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# ======================
# ADD STUDENT (FAST)
# ======================
def add_student():
    name = name_entry.get().strip()
    marks = marks_entry.get().strip()

    if name == "" or marks == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        grade = calculate_grade(marks)
    except:
        messagebox.showerror("Error", "Marks must be a number")
        return

    students.append([name, marks, grade])

    # Insert directly (NO FULL REFRESH)
    tree.insert("", "end", values=(name, marks, grade))

    name_entry.delete(0, "end")
    marks_entry.delete(0, "end")
    name_entry.focus()

# ======================
# SEARCH STUDENT (FAST)
# ======================
def search_student():
    keyword = search_entry.get().lower()

    tree.delete(*tree.get_children())

    for student in students:
        if keyword in student[0].lower():
            tree.insert("", "end", values=student)

# ======================
# VIEW ALL
# ======================
def view_all():
    tree.delete(*tree.get_children())
    for student in students:
        tree.insert("", "end", values=student)

# ======================
# DELETE STUDENT (FAST)
# ======================
def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student to delete")
        return

    for item in selected:
        values = tree.item(item, "values")

        # Remove from list
        students[:] = [s for s in students
                       if not (s[0] == values[0] and s[1] == values[1])]

        # Remove from table directly
        tree.delete(item)

# ======================
# TITLE
# ======================
title = ctk.CTkLabel(
    root,
    text="🎓 Student Grade Manager Dashboard",
    font=("Arial", 26, "bold")
)
title.pack(pady=20)

# ======================
# MAIN FRAME
# ======================
main_frame = ctk.CTkFrame(root, corner_radius=20)
main_frame.pack(padx=40, pady=10, fill="both", expand=True)

# ======================
# INPUT FRAME
# ======================
input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(pady=20, padx=30, fill="x")

ctk.CTkLabel(input_frame, text="Student Name:", font=("Arial", 14))\
    .grid(row=0, column=0, padx=10, pady=10)

name_entry = ctk.CTkEntry(input_frame, width=250, height=40)
name_entry.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(input_frame, text="Marks:", font=("Arial", 14))\
    .grid(row=0, column=2, padx=10, pady=10)

marks_entry = ctk.CTkEntry(input_frame, width=150, height=40)
marks_entry.grid(row=0, column=3, padx=10, pady=10)

ctk.CTkButton(input_frame,
              text="Add Student",
              command=add_student,
              height=40,
              width=150)\
    .grid(row=0, column=4, padx=15)

# ======================
# SEARCH FRAME
# ======================
search_frame = ctk.CTkFrame(main_frame)
search_frame.pack(pady=10, padx=30, fill="x")

ctk.CTkLabel(search_frame, text="Search:", font=("Arial", 14))\
    .grid(row=0, column=0, padx=10, pady=10)

search_entry = ctk.CTkEntry(search_frame, width=250, height=40)
search_entry.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkButton(search_frame, text="Search",
              command=search_student,
              width=120, height=40)\
    .grid(row=0, column=2, padx=10)

ctk.CTkButton(search_frame, text="View All",
              command=view_all,
              width=120, height=40)\
    .grid(row=0, column=3, padx=10)

ctk.CTkButton(search_frame, text="Delete",
              command=delete_student,
              width=120, height=40)\
    .grid(row=0, column=4, padx=10)

# ======================
# TABLE FRAME
# ======================
table_frame = ctk.CTkFrame(main_frame)
table_frame.pack(pady=20, padx=30, fill="both", expand=True)

columns = ("Name", "Marks", "Grade")

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=250)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                          command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Auto focus
root.after(300, lambda: name_entry.focus())

# RUN
root.mainloop()
