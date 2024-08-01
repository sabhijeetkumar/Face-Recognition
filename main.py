from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Frame
from student import Student

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='white')
        
    #     # First image
        img_path = "/Users/abhijeetkumar/Desktop/Face _Recoginition/e6cdef00-99ef-11e9-90d0-c64097fc903d.jpeg"
        img = Image.open(img_path)
        img = img.resize((450, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)
        
    #     # Second image
        img_path1 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/e6cdef00-99ef-11e9-90d0-c64097fc903d.jpeg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((450, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=450, y=0, width=450, height=130)
        
    #     # Third image
        img_path2 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/e6cdef00-99ef-11e9-90d0-c64097fc903d.jpeg"
        img2 = Image.open(img_path2)
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=900, y=0, width=450, height=130)
        
    #     # Background image
        img_path3 = "/Users/abhijeetkumar/Desktop/Screenshot 2024-07-06 at 11.09.26 PM.png"
        img3 = Image.open(img_path3)
        img3 = img3.resize((1350, 675), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1350, height=675)
        
    #     # Title label
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", 
                          font=("times new roman", 35, "bold"), bg="white", fg="#F4C430")
        title_lbl.place(x=0, y=0, width=1350, height=50)
        
    #     # Create the first button with text
        img_path4 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img4 = Image.open(img_path4)
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

    #     # Display image in a label
        lbl_img4 = Label(self.root, image=self.photoimg4)
        lbl_img4.place(x=150, y=200, width=220, height=220)  # Adjusted y-coordinate to 200

    #     # Create and place button
        b1_1 = Button(self.root, text="Student Details", cursor="hand2",
              font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b1_1.place(x=150, y=420, width=220, height=40)

        
    #     # Detect face
        img_path5 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img5 = Image.open(img_path5)
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

    #     # Display image in a label
        lbl_img5 = Label(self.root, image=self.photoimg5)
        lbl_img5.place(x=450, y=200, width=220, height=220)  # Adjusted y-coordinate to 200
        
    #     # Create and place button
        b2_1 = Button(self.root, text="Face Detector", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b2_1.place(x=450, y=420, width=220, height=40)
        
    #     # Attendance faces
        img_path6 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img6 = Image.open(img_path6)
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # Display image in a label
        lbl_img6 = Label(self.root, image=self.photoimg6)
        lbl_img6.place(x=750, y=200, width=220, height=220)

        # Create and place button directly below the image
        b3_1 = Button(self.root, text="Attendance Face", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b3_1.place(x=750, y=420, width=220, height=40)
        
    #     # Help face Button
        img_path7 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img7 = Image.open(img_path7)
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        # Display image in a label
        lbl_img7 = Label(self.root, image=self.photoimg7)
        lbl_img7.place(x=1050, y=200, width=220, height=220)

        # Create and place button with the same size as the image
        b4_1 = Button(self.root, text="HelpFace", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="blue")
        b4_1.place(x=1050, y=420, width=220, height=40)

        # Train face
        img_path8 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img8 = Image.open(img_path8)
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        # Display second image in a label below the first image
        lbl_img8 = Label(self.root, image=self.photoimg8)
        lbl_img8.place(x=150, y=480, width=220, height=220)

        # Create and place button below the second image
        b5_1 = Button(self.root, text="Train Face", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="black")
        b5_1.place(x=150, y=700, width=220, height=40)
        
    #     # Photos Face
        img_path9 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img9 = Image.open(img_path9)
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        # Display image in a label
        lbl_img9 = Label(self.root, image=self.photoimg9)
        lbl_img9.place(x=450, y=480, width=220, height=220)

        # Create and place button below the image
        b6_1 = Button(self.root, text="Photos", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="black")
        b6_1.place(x=450, y=700, width=220, height=40)
        
        # Developer
        img_path10 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img10 = Image.open(img_path10)
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        # Display image in a label
        lbl_img10 = Label(self.root, image=self.photoimg10)
        lbl_img10.place(x=750, y=480, width=220, height=220)

        # Create and place button below the image
        b7_1 = Button(self.root, text="Developer", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="black")
        b7_1.place(x=750, y=700, width=220, height=40)
        
        # Exit face
        img_path11 = "/Users/abhijeetkumar/Desktop/Face _Recoginition/student_details.png"
        img11 = Image.open(img_path11)
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        # Display image in a label
        lbl_img11 = Label(self.root, image=self.photoimg11)
        lbl_img11.place(x=1050, y=480, width=220, height=220)

    #     # Create and place button below the image
        b8_1 = Button(self.root, text="Exit", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="white", fg="black")
        b8_1.place(x=1050, y=700, width=220, height=40)
        
    # Function to handle Student Details button click
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
