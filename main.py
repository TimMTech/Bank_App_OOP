import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from CM import OpenFile
import os

LARGE_FONT = ("Calibri", 14)
MEDIUM_FONT = ("Calibri", 12)


class BankingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Banking Application")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        self.frames = {}

        for F in (StartPage, RegisterPage, LoginPage, AccountDash, PersonalDetails):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        self.center_window()

    def show_frame(self, con):
        frame = self.frames[con]
        frame.tkraise()

    def center_window(self):
        app_width = 300
        app_height = 300
        self.geometry(f'{app_width}x{app_height}+{600}+{350}')


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.show_pic()
        label = tk.Label(self, text="Custom Banking Beta", font=LARGE_FONT)
        label.grid(row=1, sticky=N, pady=10, padx=78)

        register_button = tk.Button(self, text="Register", font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(RegisterPage))
        register_button.grid(row=3, sticky=N)

        login_button = tk.Button(self, text="Login", font=MEDIUM_FONT, width=20,
                                 command=lambda: controller.show_frame(LoginPage))
        login_button.grid(row=4, sticky=N, pady=5)

    def show_pic(self):
        pic = Image.open("bankingoop.png")
        pic = pic.resize((150, 150))
        self.tkpic = ImageTk.PhotoImage(pic)
        label = Label(self, image=self.tkpic)
        label.grid(row=2, sticky=N, pady=15)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.all_accounts = os.listdir()
        self.username = StringVar()
        self.age = StringVar()
        self.username_password = StringVar()
        self.recovery_answer = StringVar()
        label = tk.Label(self, text="Please Enter Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        label_username = tk.Label(self, text="Username", font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W)
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=1, padx=70)
        label_age = tk.Label(self, text="Age", font=MEDIUM_FONT)
        label_age.grid(row=2, sticky=W)
        self.age_entry = tk.Entry(self, textvariable=self.age)
        self.age_entry.grid(row=2)
        label_password = tk.Label(self, text="Password", font=MEDIUM_FONT)
        label_password.grid(row=3, sticky=W)
        self.password_entry = tk.Entry(self, textvariable=self.username_password, show="*")
        self.password_entry.grid(row=3)
        label_answer = tk.Label(self, text="Answer", font=MEDIUM_FONT)
        label_answer.grid(row=4, sticky=W)
        self.answer_entry = tk.Entry(self, textvariable=self.recovery_answer, show="*")
        self.answer_entry.grid(row=4)

        self.register_button = tk.Button(self, text="Register", font=MEDIUM_FONT, width=20,
                                         command=self.finish_reg)
        self.register_button.grid(row=5, pady=10)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=self.start_page)

        previous_button.grid(row=6)

        self.username_notify = tk.Label(self, font=MEDIUM_FONT)

    def finish_reg(self):
        name = self.username.get()
        age = self.age.get()
        password = self.username_password.get()
        answer = self.recovery_answer.get()
        if name in self.all_accounts:
            self.username_notify = tk.Label(self, font=MEDIUM_FONT)
            self.username_notify.grid(row=7)
            self.username_notify.config(fg='red', text='Account Exists')
            return
        with OpenFile(name, 'w') as f:
            f.write(name + '\n')
            f.write(age + '\n')
            f.write('0' + '\n')
            f.write(password + '\n')
            f.write(answer)
            self.all_accounts.append(name)
            self.username_notify.grid_remove()
            self.register_button['text'] = 'Account Registered'
            self.register_button['state'] = 'disabled'

    def start_page(self):
        self.refresh()
        self.controller.show_frame(StartPage)

    def refresh(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.answer_entry.delete(0, END)
        self.username_notify.grid_remove()
        self.register_button['text'] = 'Register'
        self.register_button['state'] = 'normal'


class LoginPage(RegisterPage, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = StringVar()
        self.username_password = StringVar()
        label = tk.Label(self, text="Please Enter Login Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        label_username = tk.Label(self, text="Username", font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W)
        username_entry = tk.Entry(self, textvariable=self.username)
        username_entry.grid(row=1, padx=70)
        label_password = tk.Label(self, text="Password", font=MEDIUM_FONT)
        label_password.grid(row=4, sticky=W)
        password_entry = tk.Entry(self, textvariable=self.username_password, show="*")
        password_entry.grid(row=4, padx=70)

        login_button = tk.Button(self, text="Login", font=MEDIUM_FONT, width=20,
                                 command=self.login_session)
        login_button.grid(row=5, pady=10)

        forgot_pass_button = tk.Button(self, text="Forgot Password", font=MEDIUM_FONT, width=20,
                                       command=lambda: controller.show_frame(StartPage))
        forgot_pass_button.grid(row=6, pady=10)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(StartPage))
        previous_button.grid(row=7, pady=10)

        self.login_notify = tk.Label(self, font=MEDIUM_FONT)

    def login_session(self):
        self.username = self.username.get()
        self.username_password = self.username_password.get()
        self.all_accounts = os.listdir()
        for name in self.all_accounts:
            if self.username in name:
                with OpenFile(self.username, 'r') as f:
                    file_data = f.read()
                    file_data = file_data.split('\n')
                    password = file_data[3]

                    if self.username_password == password:
                        self.login_notify.grid_remove()
                        self.controller.show_frame(AccountDash)
                    self.login_notify.config(fg='red', text='Incorrect Password')
                    return
            self.login_notify.grid(row=8)
            self.login_notify.config(fg='red', text='No Account Found')


class AccountDash(LoginPage, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.all_accounts = os.listdir()

        label = tk.Label(self, text="Account Dashboard", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78, pady=20)
        details_button = tk.Button(self, text="Personal Details", font=MEDIUM_FONT, width=20,
                                   command=lambda: controller.show_frame(PersonalDetails))
        details_button.grid(row=1, sticky=N, pady=10)
        deposit_button = tk.Button(self, text="Deposit", font=MEDIUM_FONT, width=20,
                                   command=lambda: controller.show_frame(StartPage))
        deposit_button.grid(row=2, sticky=N, pady=10)

        withdraw_button = tk.Button(self, text="Withdraw", font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(StartPage))
        withdraw_button.grid(row=3, sticky=N, pady=10)

        change_password_button = tk.Button(self, text="Change Password", font=MEDIUM_FONT, width=20,
                                           command=lambda: controller.show_frame(StartPage))
        change_password_button.grid(row=4, sticky=N, pady=10)

        logout_button = tk.Button(self, text="Logout", font=MEDIUM_FONT, width=20,
                                  command=lambda: controller.show_frame(StartPage))
        logout_button.grid(row=5, sticky=N, pady=10)


class PersonalDetails(AccountDash, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Account Information", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78)
        label_username = tk.Label(self, text="Username: ", font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W, pady=10, padx=50)
        label_age = tk.Label(self, text="Age: ", font=MEDIUM_FONT)
        label_age.grid(row=2, sticky=W, pady=10, padx=50)
        label_balance = tk.Label(self, text="Balance :$", font=MEDIUM_FONT)
        label_balance.grid(row=3, sticky=W, pady=10, padx=50)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(AccountDash))
        previous_button.grid(row=5, sticky=N, pady=40)


app = BankingApp()
app.mainloop()
