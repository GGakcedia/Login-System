from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk 


def register_user():

  username_info = username.get()
  password_info = password.get()

  file=open(username_info+".txt", "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("Nunito Light", 11)).pack()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username  ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password  ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  print("Login session started")


def main_screen():



  global screen
  screen = Tk()
  screen.geometry("640x480")
  screen.title("Notes 1.0")
  Frame(screen, bg="#3F51B5").place(x=160, y=100, width=300, height=250)
 
  #Username
  Label(screen, text="Username", font=("Nunito Bold", 15), fg="#C5CAE9", bg="#3F51B5").place(x=200,y=130)
  password =  Entry(screen,bd=0, font=("Nunito Bold", 15), bg="#C5CAE9").place(x=200,y=160, width=220)

  #Password
  Label(screen, text="Password", font=("Nunito Bold", 15), fg="#C5CAE9", bg="#3F51B5").place(x=200,y=190)
  password =  Entry(screen,bd=0, font=("Nunito Bold", 15), bg="#C5CAE9").place(x=200,y=220, width=220)
  
  Label(screen,text = "Notes 1.0", bg = "grey",  font = ("Nunito Bold", 13)).place(x=200,y=270,height = 50, width = 100)
  
  Button(text = "Log in", bd=0,bg="#0288d1",fg="#000000",font = ("Nunito Bold", 12), command = login).place(x=200,y=270,height = 50, width = 100)
  Label(text = "").pack()
  Button(text = "Register",bd=0,bg="#0288d1",fg="#000000",font = ("Nunito Bold", 12), command = register,).place(x=320,y=270,height = 50, width = 100)

  screen.mainloop()

main_screen()