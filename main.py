import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk, Image
from decimal import *

LARGE_FONT = ("Calibri",14)
MEDIUM_FONT = ("Calibri",12)


class BankingApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"Banking Application")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand= True)
        container.grid_rowconfigure(10,weight=1)
        container.grid_columnconfigure(10,weight=1)

        self.frames = {}

        for F in (StartPage,RegisterPage,LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)
        self.center_window()


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def center_window(self):
        app_width = 300
        app_height = 300
        self.geometry(f'{app_width}x{app_height}+{600}+{350}')



class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.show_pic()
        label = tk.Label(self,text="Custom Banking Beta", font=LARGE_FONT)
        label.grid(row=1,sticky=N ,pady=10,padx=78)

        register_button = tk.Button(self, text="Register",font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(RegisterPage))
        register_button.grid(row=3, sticky=N)

        login_button = tk.Button(self, text = "Login", font=MEDIUM_FONT, width=20,
                                 command=lambda: controller.show_frame(LoginPage))
        login_button.grid(row=4,sticky=N,pady=5)


    def show_pic(self):
        pic = Image.open("bankingoop.png")
        pic = pic.resize((150, 150))
        self.tkpic = ImageTk.PhotoImage(pic)
        label = Label(self, image=self.tkpic)
        label.grid(row=2, sticky=N,pady=15)



class RegisterPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        temp_username = StringVar()
        temp_age = StringVar()
        temp_username_password = StringVar()
        temp_recovery_answer = StringVar()
        label = tk.Label(self, text="Please Enter Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        label_username = tk.Label(self, text="Username", font=MEDIUM_FONT)
        label_username.grid(row=1,sticky=W)
        username_entry = tk.Entry(self, textvariable=temp_username)
        username_entry.grid(row=1,padx=70)
        label_age = tk.Label(self, text="Age", font=MEDIUM_FONT)
        label_age.grid(row=2, sticky=W)
        age_entry = tk.Entry(self, textvariable=temp_age)
        age_entry.grid(row=2)
        label_password = tk.Label(self, text="Password", font=MEDIUM_FONT)
        label_password.grid(row=3,sticky=W)
        password_entry = tk.Entry(self, textvariable=temp_username_password, show="*")
        password_entry.grid(row=3)
        label_answer = tk.Label(self, text="Answer", font=MEDIUM_FONT)
        label_answer.grid(row=4, sticky=W)
        answer_entry = tk.Entry(self, textvariable=temp_recovery_answer, show="*")
        answer_entry.grid(row=4)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        temp_username = StringVar()
        temp_username_password = StringVar()
        label = tk.Label(self, text="Please Enter Login Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        username_entry = tk.Entry(self, textvariable=temp_username)
        username_entry.grid(row=1, padx=60)
        password_entry = tk.Entry(self, textvariable=temp_username_password, show="*")
        password_entry.grid(row=4, padx=60)


app = BankingApp()
app.mainloop()






