from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk 
class Login :
    def __init__(self, root) :
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1366x768")
        self.root.resizable(False, False)

        #Background Image
        self.bg=ImageTk.PhotoImage (file="background.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
 
        #Login Frame
        Frame_login = Frame(self.root, bg="#3F51B5")
        Frame_login.place(x=530, y=250, width=300, height=300)

        #Title & subtitle
        title= Label(Frame_login, text="Login Here", font=("Nunito Bold", 30, ), fg="#C5CAE9", bg="#3F51B5").place(x=45, y=30) 

        #Username 
        lbl_user = Label(Frame_login, text="Username", font=("Nunito Light", 15), fg="#C5CAE9", bg="#3F51B5").place(x=20,y=110)
        self.username = Entry(Frame_login, bd=0, font=("Nunito Light", 15), bg="#C5CAE9")
        self.username.place(x=25, y=140, width=250, height=30)

        #Password
        lbl_user = Label(Frame_login, text="Password", font=("Nunito Light", 15), fg="#C5CAE9", bg="#3F51B5").place(x=20,y=180)
        self.username = Entry(Frame_login,bd=0, font=("Nunito Light", 15), bg="#C5CAE9")
        self.username.place(x=25, y=210, width=250, height=30)

        #Button 
        forget = Button(Frame_login, text="forgot password?", bd=0, font=("Nunito Light",8), bg="#3F51B5",fg="#FFFFFF").place(x=185,y=187)
        submit = Button(Frame_login, text="Log in", bd=1, font=("Nunito Bold",10), bg="#C5CAE9",fg="#3F51B5").place(x=25,y=255, width=250, height=30)



root = Tk()
obj = Login(root)
root.mainloop()