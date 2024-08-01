from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        # Variables
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_div = StringVar()
        self.var_uid = StringVar()
        self.var_gender = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        # Title
        title = Label(self.root, text="Student Management System", font=("times new roman", 40, "bold"), bg="blue", fg="white")
        title.pack(side=TOP, fill=X)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=100, width=1330, height=580)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=560)

        # Student Information
        class_student_frame = Frame(left_frame, bg="white")
        class_student_frame.place(x=5, y=10, width=640, height=500)

        # Student ID
        id_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        name_label = Label(class_student_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        dep_label = Label(class_student_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(class_student_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=18, state="readonly")
        dep_combo['values'] = ("Select", "CSE", "IT", "ECE", "EEE", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Course
        course_label = Label(class_student_frame, text="Course:", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(class_student_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo['values'] = ("Select", "B.Tech", "M.Tech", "MBA", "MCA")
        course_combo.current(0)
        course_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Year
        year_label = Label(class_student_frame, text="Year:", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(class_student_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=18, state="readonly")
        year_combo['values'] = ("Select", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Semester
        semester_label = Label(class_student_frame, text="Semester:", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(class_student_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=20, state="readonly")
        semester_combo['values'] = ("Select", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Division
        division_label = Label(class_student_frame, text="Division:", font=("times new roman", 12, "bold"), bg="white")
        division_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        division_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), width=18, state="readonly")
        division_combo['values'] = ("Select", "A", "B", "C", "D")
        division_combo.current(0)
        division_combo.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # UID
        uid_label = Label(class_student_frame, text="UID:", font=("times new roman", 12, "bold"), bg="white")
        uid_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        uid_entry = ttk.Entry(class_student_frame, textvariable=self.var_uid, width=20, font=("times new roman", 12, "bold"))
        uid_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.var_gender = StringVar()
        male_radio = ttk.Radiobutton(class_student_frame, text="Male", variable=self.var_gender, value="Male")
        male_radio.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        female_radio = ttk.Radiobutton(class_student_frame, text="Female", variable=self.var_gender, value="Female")
        female_radio.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.var_address = StringVar()
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        self.var_phone = StringVar()
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        self.var_email = StringVar()
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
         # Radiobuttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="YES")
        radiobtn1.grid(row=5, column=0)
        
  
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="NO")
        radiobtn2.grid(row=5, column=1)

        # Buttons
        btn_frame = Frame(class_student_frame, bd=2, bg="white")
        btn_frame.place(x=5, y=450, width=620)

        add_btn = ttk.Button(btn_frame, text="Add", command=self.add_student)
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        update_btn = ttk.Button(btn_frame, text="Update", command=self.update_student)
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_student)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        reset_btn = ttk.Button(btn_frame, text="Reset", command=self.reset_fields)
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Records", font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=640, height=560)

        # Search Frame
        search_frame = Frame(right_frame, bd=2, bg="white")
        search_frame.place(x=5, y=10, width=620, height=60)

        search_by_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_by_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_by_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by, font=("times new roman", 12, "bold"), width=20, state="readonly")
        search_by_combo['values'] = ("Select", "Student ID", "Name", "Department", "Course", "Year", "Semester", "Division", "UID", "Gender", "Address", "Phone", "Email")
        search_by_combo.current(0)
        search_by_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_txt_entry = ttk.Entry(search_frame, textvariable=self.var_search_txt, width=20, font=("times new roman", 12, "bold"))
        search_txt_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = ttk.Button(search_frame, text="Search", command=self.search_student)
        search_btn.grid(row=0, column=3, padx=10, pady=5)

        # Student Table
        table_frame = Frame(right_frame, bd=2, bg="white")
        table_frame.place(x=5, y=70, width=620, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("id", "name", "department", "course", "year", "semester", "division", "uid", "gender", "address", "phone", "email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("uid", text="UID")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text="Email")

        self.student_table['show'] = 'headings'
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.show_all_students()

    def add_student(self):
        if self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_dep.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO student (id, name, department, course, year, semester, division, uid, gender, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (self.var_std_id.get(), self.var_std_name.get(), self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_div.get(), self.var_uid.get(), self.var_gender.get(), self.var_address.get(), self.var_phone.get(), self.var_email.get()))
            conn.commit()
            self.reset_fields()
            self.show_all_students()
            messagebox.showinfo("Success", "Student added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def update_student(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to update")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("UPDATE student SET name=%s, department=%s, course=%s, year=%s, semester=%s, division=%s, uid=%s, gender=%s, address=%s, phone=%s, email=%s WHERE id=%s",
                           (self.var_std_name.get(), self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_div.get(), self.var_uid.get(), self.var_gender.get(), self.var_address.get(), self.var_phone.get(), self.var_email.get(), self.var_std_id.get()))
            conn.commit()
            self.reset_fields()
            self.show_all_students()
            messagebox.showinfo("Success", "Student updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def delete_student(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE id=%s", (self.var_std_id.get(),))
            conn.commit()
            self.reset_fields()
            self.show_all_students()
            messagebox.showinfo("Success", "Student deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def reset_fields(self):
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_dep.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_div.set("")
        self.var_uid.set("")
        self.var_gender.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_email.set("")

    def search_student(self):
        search_by = self.var_search_by.get()
        search_txt = self.var_search_txt.get()
        if search_by == "Select":
            messagebox.showerror("Error", "Please select a search criterion")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
            cursor = conn.cursor()
            query = f"SELECT * FROM student WHERE {search_by.lower().replace(' ', '_')} LIKE %s"
            cursor.execute(query, ('%' + search_txt + '%',))
            rows = cursor.fetchall()
            self.populate_table(rows)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def show_all_students(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abhijeet@15", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            self.populate_table(rows)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def populate_table(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            self.student_table.insert('', 'end', values=row)

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        if row:
            self.var_std_id.set(row[0])
            self.var_std_name.set(row[1])
            self.var_dep.set(row[2])
            self.var_course.set(row[3])
            self.var_year.set(row[4])
            self.var_semester.set(row[5])
            self.var_div.set(row[6])
            self.var_uid.set(row[7])
            self.var_gender.set(row[8])
            self.var_address.set(row[9])
            self.var_phone.set(row[10])
            self.var_email.set(row[11])

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
