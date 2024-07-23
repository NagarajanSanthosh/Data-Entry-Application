import tkinter
from tkinter import ttk, filedialog
from tkinter import messagebox
import sqlite3
import csv

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                registration_status TEXT, num_courses INT, num_semesters INT, email TEXT, phone TEXT, address TEXT)
        '''
        self.cursor.execute(table_create_query)
        self.conn.commit()

    def insert_data(self, data_tuple):
        data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
        age, nationality, registration_status, num_courses, num_semesters, email, phone, address) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(data_insert_query, data_tuple)
        self.conn.commit()

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM Student_Data")
        rows = self.cursor.fetchall()
        return rows

    def search_data(self, column, value):
        query = f"SELECT * FROM Student_Data WHERE {column} LIKE ?"
        self.cursor.execute(query, ('%' + value + '%',))
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()

class DataEntryForm:
    def __init__(self, root):
        self.window = root
        self.window.title("Data Entry Form")
        
        self.db = Database('data.db')

        self.frame = tkinter.Frame(self.window)
        self.frame.pack()

        self.create_user_info_frame()
        self.create_course_info_frame()
        self.create_contact_info_frame()
        self.create_terms_frame()
        self.create_button_frame()
        
    def create_user_info_frame(self):
        self.user_info_frame = tkinter.LabelFrame(self.frame, text="User Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        self.first_name_label = tkinter.Label(self.user_info_frame, text="First Name")
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = tkinter.Label(self.user_info_frame, text="Last Name")
        self.last_name_label.grid(row=0, column=1)

        self.first_name_entry = tkinter.Entry(self.user_info_frame)
        self.last_name_entry = tkinter.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        self.title_label = tkinter.Label(self.user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        self.title_label.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        self.age_label = tkinter.Label(self.user_info_frame, text="Age")
        self.age_spinbox = tkinter.Spinbox(self.user_info_frame, from_=18, to=110)
        self.age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)

        self.nationality_label = tkinter.Label(self.user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        self.nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3, column=1)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_course_info_frame(self):
        self.courses_frame = tkinter.LabelFrame(self.frame, text="Course Information")
        self.courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.registered_label = tkinter.Label(self.courses_frame, text="Registration Status")
        self.reg_status_var = tkinter.StringVar(value="Not Registered")
        self.registered_check = tkinter.Checkbutton(self.courses_frame, text="Currently Registered", variable=self.reg_status_var, onvalue="Registered", offvalue="Not Registered")

        self.registered_label.grid(row=0, column=0)
        self.registered_check.grid(row=1, column=0)

        self.numcourses_label = tkinter.Label(self.courses_frame, text="# Completed Courses")
        self.numcourses_spinbox = tkinter.Spinbox(self.courses_frame, from_=0, to='infinity')
        self.numcourses_label.grid(row=0, column=1)
        self.numcourses_spinbox.grid(row=1, column=1)

        self.numsemesters_label = tkinter.Label(self.courses_frame, text="# Semesters")
        self.numsemesters_spinbox = tkinter.Spinbox(self.courses_frame, from_=0, to='infinity')
        self.numsemesters_label.grid(row=0, column=2)
        self.numsemesters_spinbox.grid(row=1, column=2)

        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_contact_info_frame(self):
        self.contact_info_frame = tkinter.LabelFrame(self.frame, text="Contact Information")
        self.contact_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.email_label = tkinter.Label(self.contact_info_frame, text="Email")
        self.email_entry = tkinter.Entry(self.contact_info_frame)
        self.email_label.grid(row=0, column=0)
        self.email_entry.grid(row=1, column=0)

        self.phone_label = tkinter.Label(self.contact_info_frame, text="Phone")
        self.phone_entry = tkinter.Entry(self.contact_info_frame)
        self.phone_label.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)

        self.address_label = tkinter.Label(self.contact_info_frame, text="Address")
        self.address_entry = tkinter.Entry(self.contact_info_frame)
        self.address_label.grid(row=2, column=0)
        self.address_entry.grid(row=3, column=0, columnspan=2)

        for widget in self.contact_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def create_terms_frame(self):
        self.terms_frame = tkinter.LabelFrame(self.frame, text="Terms & Conditions")
        self.terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = tkinter.Checkbutton(self.terms_frame, text="I accept the terms and conditions.", variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)

    def create_button_frame(self):
        self.button_frame = tkinter.Frame(self.frame)
        self.button_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

        self.enter_button = tkinter.Button(self.button_frame, text="Enter Data", command=self.enter_data)
        self.enter_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_button = tkinter.Button(self.button_frame, text="View Data", command=self.view_data)
        self.view_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tkinter.Button(self.button_frame, text="Search Data", command=self.search_data)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.export_button = tkinter.Button(self.button_frame, text="Export Data", command=self.export_data)
        self.export_button.grid(row=0, column=3, padx=5, pady=5)

    def validate_email(self, email):
        import re
        return re.match(r'[^@]+@[^@]+\.[^@]+', email)

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    def enter_data(self):
        accepted = self.accept_var.get()
        
        if accepted == "Accepted":
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            address = self.address_entry.get()

            if not self.validate_email(email):
                tkinter.messagebox.showwarning(title="Error", message="Invalid email address.")
                return

            if not self.validate_phone(phone):
                tkinter.messagebox.showwarning(title="Error", message="Invalid phone number.")
                return

            if firstname and lastname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                nationality = self.nationality_combobox.get()
                registration_status = self.reg_status_var.get()
                numcourses = self.numcourses_spinbox.get()
                numsemesters = self.numsemesters_spinbox.get()

                data_tuple = (firstname, lastname, title, age, nationality, registration_status, numcourses, numsemesters, email, phone, address)
                self.db.insert_data(data_tuple)
                tkinter.messagebox.showinfo(title="Success", message="Data entered successfully.")
            else:
                tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

    def view_data(self):
        new_window = tkinter.Toplevel(self.window)
        new_window.title("View Data")
        
        rows = self.db.fetch_data()
        
        tree = ttk.Treeview(new_window, columns=("firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters", "email", "phone", "address"), show='headings')
        tree.heading("firstname", text="First Name")
        tree.heading("lastname", text="Last Name")
        tree.heading("title", text="Title")
        tree.heading("age", text="Age")
        tree.heading("nationality", text="Nationality")
        tree.heading("registration_status", text="Registration Status")
        tree.heading("num_courses", text="Num Courses")
        tree.heading("num_semesters", text="Num Semesters")
        tree.heading("email", text="Email")
        tree.heading("phone", text="Phone")
        tree.heading("address", text="Address")
        
        for row in rows:
            tree.insert("", "end", values=row)
        
        tree.pack(padx=10, pady=10)

    def search_data(self):
        search_window = tkinter.Toplevel(self.window)
        search_window.title("Search Data")
        
        search_frame = tkinter.Frame(search_window)
        search_frame.pack(padx=10, pady=10)

        search_label = tkinter.Label(search_frame, text="Search by")
        search_label.grid(row=0, column=0, padx=5, pady=5)
        
        search_options = ["firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters", "email", "phone", "address"]
        self.search_combobox = ttk.Combobox(search_frame, values=search_options)
        self.search_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        self.search_entry = tkinter.Entry(search_frame)
        self.search_entry.grid(row=0, column=2, padx=5, pady=5)
        
        search_button = tkinter.Button(search_frame, text="Search", command=self.perform_search)
        search_button.grid(row=0, column=3, padx=5, pady=5)

        self.search_results_frame = tkinter.Frame(search_window)
        self.search_results_frame.pack(padx=10, pady=10)

    def perform_search(self):
        search_column = self.search_combobox.get()
        search_value = self.search_entry.get()
        
        if search_column and search_value:
            rows = self.db.search_data(search_column, search_value)
            
            for widget in self.search_results_frame.winfo_children():
                widget.destroy()
            
            tree = ttk.Treeview(self.search_results_frame, columns=("firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters", "email", "phone", "address"), show='headings')
            tree.heading("firstname", text="First Name")
            tree.heading("lastname", text="Last Name")
            tree.heading("title", text="Title")
            tree.heading("age", text="Age")
            tree.heading("nationality", text="Nationality")
            tree.heading("registration_status", text="Registration Status")
            tree.heading("num_courses", text="Num Courses")
            tree.heading("num_semesters", text="Num Semesters")
            tree.heading("email", text="Email")
            tree.heading("phone", text="Phone")
            tree.heading("address", text="Address")
            
            for row in rows:
                tree.insert("", "end", values=row)
            
            tree.pack(padx=10, pady=10)

    def export_data(self):
        rows = self.db.fetch_data()
        if rows:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if file_path:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["First Name", "Last Name", "Title", "Age", "Nationality", "Registration Status", "Num Courses", "Num Semesters", "Email", "Phone", "Address"])
                    writer.writerows(rows)
                tkinter.messagebox.showinfo(title="Success", message="Data exported successfully.")
        else:
            tkinter.messagebox.showwarning(title="Error", message="No data available to export.")

if __name__ == "__main__":
    root = tkinter.Tk()
    app = DataEntryForm(root)
    root.mainloop()
