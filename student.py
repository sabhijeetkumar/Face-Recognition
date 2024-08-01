from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import _mysql_connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x790+0+0")
        self.root.title("Student Management System")
        self.root.configure(bg='white')
        
        self.images = []

        # First image
        img_path = "/Users/abhijeetkumar/Downloads/facial-recognition_0-2.jpg"
        img = Image.open(img_path)
        img = img.resize((450, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        self.images.append(self.photoimg)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)

        # Second image
        img_path1 = "/Users/abhijeetkumar/Downloads/facial-recognition_0-2.jpg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((450, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.images.append(self.photoimg1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=450, y=0, width=450, height=130)

        # Third image
        img_path2 = "/Users/abhijeetkumar/Downloads/facial-recognition_0-2.jpg"
        img2 = Image.open(img_path2)
        img2 = img2.resize((450, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.images.append(self.photoimg2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=900, y=0, width=450, height=130)

        # Background image
        img_path3 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/Image.png"
        img3 = Image.open(img_path3)
        img3 = img3.resize((1350, 675), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.images.append(self.photoimg3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1350, height=675)
        
        
        # Title label
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1350, height=50)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1320, height=600)
        
        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=580)
        
        img_left_path = "/Users/abhijeetkumar/Downloads/WhatsApp Image 2024-06-16 at 6.28.24 PM.jpeg"
        img_left = Image.open(img_left_path)
        img_left = img_left.resize((620, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        self.images.append(self.photoimg_left)

        f_lbl_left = Label(left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=610, height=130)
        
        # Current course frame
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=610, height=100) 
        
        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new Roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 12, "bold"), width=17, state="readonly")
        dep_combo['values'] = ("Select Department", "Computer Science", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)
        
        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new Roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 13, "bold"), width=20, state="readonly")
        course_combo['values'] = ("Select Course", "FE", "SE", "TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new Roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 13, "bold"), width=20, state="readonly")
        year_combo['values'] = ("Select Year", "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=8, sticky=W)
        
        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new Roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 13, "bold"), width=20, state="readonly")
        semester_combo['values'] = ("Semester", "1st", "2nd", "3rd")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        # Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=240, width=610, height=300)  
        
        # Student ID
        student_id_label = Label(class_student_frame, text="Student ID:", font=("times new Roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, sticky=W)
        
        student_id_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, sticky=W)
        
        # Student Name
        student_name_label = Label(class_student_frame, text="Student Name:", font=("times new Roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        student_name_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Class Division
        class_division_label = Label(class_student_frame, text="Class Division:", font=("times new Roman", 12, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        class_division_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        class_division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # UID
        uid_label = Label(class_student_frame, text="UID:", font=("times new Roman", 12, "bold"), bg="white")
        uid_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        uid_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        uid_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new Roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new Roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # Email ID
        email_id_label = Label(class_student_frame, text="Email ID:", font=("times new Roman", 12, "bold"), bg="white")
        email_id_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_id_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        email_id_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Phone No
        phone_no_label = Label(class_student_frame, text="Phone No:", font=("times new Roman", 12, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_no_entry = ttk.Entry(class_student_frame, width=20, font=("times new Roman", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Radiobuttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="YES")
        radiobtn1.grid(row=5, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="NO")
        radiobtn2.grid(row=5, column=1)
        
        # Button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=700, height=30)
        
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=20, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update", width=20, font=("times new Roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, text="Delete", width=20, font=("times new Roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset", width=20, font=("times new Roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=205, width=700, height=35)
        
        take_photo_sample_btn = Button(btn_frame1, text="Take Photo Sample", width=30, font=("times new Roman", 12, "bold"), bg="blue", fg="white")
        take_photo_sample_btn.grid(row=0, column=0)
        
        update_photo_sample_btn = Button(btn_frame1, text="Update Photo Sample", width=30, font=("times new Roman", 12, "bold"), bg="blue", fg="white")
        update_photo_sample_btn.grid(row=0, column=1)
        
         # Right label frame
        
        Right_Frame = LabelFrame(main_frame,bd=2, bg= "white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=660,y=10,width=595,height=580)
        
         
         # Right label frame
        
        Right_Frame = LabelFrame(main_frame,bd=2, bg= "white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=660,y=10,width=595,height=580)
        
        img_right_path = (r"/Users/abhijeetkumar/Downloads/WhatsApp Image 2024-06-16 at 6.28.24 PM.jpeg")
        img_right = Image.open(img_right_path)
        img_rigth = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl1 = Label(Right_Frame, image=self.photoimg_right)
        f_lbl1.place(x=5, y=0, width=710, height=130)
        
        
        
        # Search System
        
        
        search_frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=580, height=70)

    # Add search label
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    # Add search combo box
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo['values'] = ("Select", "UID", "Phone no")
        search_combo.current(0)  # Set the initial value to "Select"
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        search_entry = ttk.Entry(search_frame,width=15,font=("times new Roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

    # Add search button
        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

    # Add show all button
        show_all_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=0, column=4, padx=4)
        
        
        #  table frame
        
        table_frame = Frame(Right_Frame, bd=2, bg="White", relief=RIDGE)
        table_frame.place(x=5, y=210, width=580, height=300)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "ID", "Name", "Div", "UID", "Gender", "DOB", "email", "Phone no", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Div", text="Class Division")
        self.student_table.heading("UID", text="UID")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("email", text="Email ID")
        self.student_table.heading("Phone no", text="Phone No")
        self.student_table.heading("photo", text="Photo Sample Status")
        
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("UID", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("Phone no", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        

    def add_data(self):
        pass  # Placeholder for the add_data method implementation

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
