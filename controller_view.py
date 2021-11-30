import os
import tkinter as tk
from tkinter import StringVar, N, W, END, Label
import sys

from PIL import ImageTk, Image
from decimal import Decimal

from observable import MEDIUM_FONT, LARGE_FONT


def successLogOut():
    print("Successfully Logged out")
    python = sys.executable
    os.execl(python, python, *sys.argv)


class BankingApp(tk.Tk):

    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Banking Application")
        self.controller = controller

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        self.frames = {}

        self.path = '/Users/tim/PycharmProjects/Bank_App_OOP'
        self.app_data = os.listdir(self.path)
        self.app_dict = {"name": StringVar(),
                         "password": StringVar(),
                         "balance": '0',
                         "deposit": StringVar(),
                         "withdraw": StringVar()
                         }

        for F in (StartPage, RegisterPage, LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        self.center_window()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def clear_frame(self, cont):
        frame = self.frames[cont]
        for widget in frame.winfo_children():
            widget.grid_remove()

    def restore_frame(self, cont):
        frame = self.frames[cont]
        for widget in frame.winfo_children():
            widget.grid()

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
                                    command=lambda: self.controller.show_frame(RegisterPage))
        register_button.grid(row=3, sticky=N)

        login_button = tk.Button(self, text="Login", font=MEDIUM_FONT, width=20,
                                 command=lambda: self.controller.show_frame(LoginPage))
        login_button.grid(row=4, sticky=N, pady=5)

    def show_pic(self):
        pic = Image.open("bankingoop.png")
        pic = pic.resize((150, 150))
        # noinspection PyAttributeOutsideInit
        self.tkpic = ImageTk.PhotoImage(pic)
        label = Label(self, image=self.tkpic)
        label.grid(row=2, sticky=N, pady=15)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please Enter Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        label_username = tk.Label(self, text="Username", font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W)
        self.username_entry = tk.Entry(self, textvariable=self.controller.app_dict["name"])
        self.username_entry.grid(row=1, padx=70)
        label_password = tk.Label(self, text="Password", font=MEDIUM_FONT)
        label_password.grid(row=3, sticky=W)
        self.password_entry = tk.Entry(self, textvariable=self.controller.app_dict["password"], show="*")
        self.password_entry.grid(row=3)

        self.register_button = tk.Button(self, text="Register", font=MEDIUM_FONT, width=20,
                                         command=lambda: self.storeIt())
        self.register_button.grid(row=5, pady=10)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=self.restore_StartPage)

        previous_button.grid(row=6)

        self.username_notify = tk.Label(self, font=MEDIUM_FONT)

    def storeIt(self):
        """
        Function to store in DB
        :return:
        """
        username_value = self.controller.app_dict["name"].get()
        password_value = self.controller.app_dict["password"].get()
        balance = self.controller.app_dict["balance"]

        if username_value in self.controller.app_data:
            self.username_notify = tk.Label(self, font=MEDIUM_FONT)
            self.username_notify.grid(row=7)
            self.username_notify.config(fg='red', text="Account Exists")
            return
        with open(username_value, "w") as f:
            f.write(username_value + '\n')
            f.write(password_value + '\n')
            f.write(balance)
            self.controller.app_data.append(username_value)
            self.username_notify.grid_remove()
            self.register_button['text'] = 'Account Registered'
            self.register_button['state'] = 'disabled'

    def restore_StartPage(self):
        self.refresh()
        self.controller.show_frame(StartPage)

    def refresh(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.username_notify.grid_remove()
        self.register_button['text'] = 'Register'
        self.register_button['state'] = 'normal'


class LoginPage(tk.Frame):
    """
    Frame for Distinct Users
    All operation performed in class LoginPage
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please Enter Login Details Below", font=LARGE_FONT)
        label.grid(row=0, sticky=N, pady=10)
        label_username = tk.Label(self, text="Username", font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W)
        username_entry = tk.Entry(self, textvariable=self.controller.app_dict["name"])
        username_entry.grid(row=1, padx=70)
        label_password = tk.Label(self, text="Password", font=MEDIUM_FONT)
        label_password.grid(row=4, sticky=W)
        password_entry = tk.Entry(self, textvariable=self.controller.app_dict["password"], show="*")
        password_entry.grid(row=4, padx=70)

        login_button = tk.Button(self, text="Login", font=MEDIUM_FONT, width=20,
                                 command=self.loginSession)
        login_button.grid(row=5, pady=10)

        forgot_pass_button = tk.Button(self, text="Forgot Password", font=MEDIUM_FONT, width=20,
                                       command=lambda: controller.show_frame(StartPage))
        forgot_pass_button.grid(row=6, pady=10)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=lambda: controller.show_frame(StartPage))
        previous_button.grid(row=7, pady=10)

        self.login_notify = tk.Label(self, font=MEDIUM_FONT)
        self.deposit_notify = tk.Label(self, font=MEDIUM_FONT)
        self.withdraw_notify = tk.Label(self, font=MEDIUM_FONT)
        self.balance_label = tk.Label(self, font=MEDIUM_FONT)

    def loginSession(self):
        """
        Function that allocates distinct User DB
        :return:
        """
        global username
        username = self.controller.app_dict["name"].get()
        user_password = self.controller.app_dict["password"].get()
        for name in self.controller.app_data:
            if username in name:
                with open(username, 'r') as f:
                    file_data = f.read()
                    file_data = file_data.split('\n')
                    password = file_data[1]

                    if user_password == password:
                        self.login_notify.grid_remove()
                        self.controller.clear_frame(LoginPage)
                        self.accountDashboard()
                        return
                    self.login_notify.grid(row=8)
                    self.login_notify.config(fg='red', text="Invalid Password")
                    return
            self.login_notify.grid(row=8)
            self.login_notify.config(fg='red', text="No Account Found")

    def accountDashboard(self):
        label = tk.Label(self, text="Account Dashboard", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78, pady=20)
        details_button = tk.Button(self, text="Personal Details", font=MEDIUM_FONT, width=20,
                                   command=self.personalDetails)
        details_button.grid(row=1, sticky=N, pady=10)
        deposit_button = tk.Button(self, text="Deposit", font=MEDIUM_FONT, width=20,
                                   command=self.depositScreen)
        deposit_button.grid(row=2, sticky=N, pady=10)

        withdraw_button = tk.Button(self, text="Withdraw", font=MEDIUM_FONT, width=20,
                                    command=self.withdrawScreen)
        withdraw_button.grid(row=3, sticky=N, pady=10)

        logout_button = tk.Button(self, text="Logout", font=MEDIUM_FONT, width=20,
                                  command=successLogOut)
        logout_button.grid(row=5, sticky=N, pady=10)

    def personalDetails(self):
        self.controller.clear_frame(LoginPage)
        with open(username, 'r') as f:
            account_data = f.read()
            account_details = account_data.split('\n')
            details_name = account_details[0]
            details_balance = account_details[2]

        label = tk.Label(self, text="Account Information", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78)
        label_username = tk.Label(self, text="Username: " + details_name, font=MEDIUM_FONT)
        label_username.grid(row=1, sticky=W, pady=10, padx=50)
        label_balance = tk.Label(self, text="Balance : $" + details_balance, font=MEDIUM_FONT)
        label_balance.grid(row=3, sticky=W, pady=10, padx=50)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=self.restore_accountDashboard)
        previous_button.grid(row=5, sticky=N, pady=40)

    def depositScreen(self):
        self.controller.clear_frame(LoginPage)
        with open(username, 'r') as f:
            account_data = f.read()
            account_details = account_data.split('\n')
            details_balance = account_details[2]

        label = tk.Label(self, text="Deposit Information", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78)
        self.balance_label = tk.Label(self, text="Current Balance: $" + details_balance, font=MEDIUM_FONT)
        self.balance_label.grid(row=1, sticky=W, pady=10, padx=20)
        deposit_amount_label = tk.Label(self, text="Amount in $", font=MEDIUM_FONT)
        deposit_amount_label.grid(row=2, sticky=N)
        deposit_amount_entry = tk.Entry(self, textvariable=self.controller.app_dict["deposit"],
                                        width=10)
        deposit_amount_entry.grid(row=3, sticky=N)

        deposit_button = tk.Button(self, text="Deposit", font=MEDIUM_FONT, width=20,
                                   command=lambda: self.depositFinish())
        deposit_button.grid(row=4, sticky=N, pady=20)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=self.restore_accountDashboard)
        previous_button.grid(row=5, sticky=N)

    def depositFinish(self):
        if self.controller.app_dict["deposit"].get() == "":
            self.deposit_notify.grid(row=6)
            self.deposit_notify.config(fg='red', text="Amount Needed")
            return
        if Decimal(self.controller.app_dict["deposit"].get()) <= 0:
            self.deposit_notify.grid(row=6)
            self.deposit_notify.config(fg='red', text="Negative Currency Not Allowed")
            return
        with open(username, "r+") as file:
            file_data = file.read()
            details = file_data.split('\n')
            current_name = details[0]
            current_password = details[1]
            current_balance = details[2]
            updated_balance = current_balance
            updated_balance = Decimal(updated_balance) + Decimal(self.controller.app_dict["deposit"].get())
        with open(username, "w") as new_file:
            new_file.write(current_name + '\n')
            new_file.write(current_password + '\n')
            new_file.write(str(updated_balance))
            self.deposit_notify.grid(row=6)
            self.deposit_notify.config(fg='green', text="Balance Updated")
            self.balance_label.config(text="Current Balance $" + str(updated_balance))

    def withdrawScreen(self):
        self.controller.clear_frame(LoginPage)
        with open(username, 'r') as f:
            account_data = f.read()
            account_details = account_data.split('\n')
            details_balance = account_details[2]

        label = tk.Label(self, text="Withdrawal Information", font=LARGE_FONT)
        label.grid(row=0, sticky=N, padx=78)
        self.balance_label = tk.Label(self, text="Current Balance: $" + details_balance, font=MEDIUM_FONT)
        self.balance_label.grid(row=1, sticky=W, pady=10, padx=20)
        withdraw_amount_label = tk.Label(self, text="Amount in $", font=MEDIUM_FONT)
        withdraw_amount_label.grid(row=2, sticky=N)
        withdraw_amount_entry = tk.Entry(self, textvariable=self.controller.app_dict["withdraw"])
        withdraw_amount_entry.grid(row=3, sticky=N)

        withdraw_button = tk.Button(self, text="Withdraw", font=MEDIUM_FONT, width=20,
                                    command=lambda: self.withdrawFinish())
        withdraw_button.grid(row=4, sticky=N, pady=20)

        previous_button = tk.Button(self, text="Previous", font=MEDIUM_FONT, width=20,
                                    command=self.restore_accountDashboard)
        previous_button.grid(row=5, sticky=N)

    def withdrawFinish(self):
        if self.controller.app_dict["withdraw"].get() == "":
            self.withdraw_notify.grid(row=6)
            self.withdraw_notify.config(fg='red', text="Amount Needed")
            return
        if Decimal(self.controller.app_dict["withdraw"].get()) <= 0:
            self.withdraw_notify.grid(row=6)
            self.withdraw_notify.config(fg='red', text="Negative Currency Not Allowed")
            return
        with open(username, "r+") as file:
            file_data = file.read()
            details = file_data.split('\n')
            current_name = details[0]
            current_password = details[1]
            current_balance = details[2]

            if Decimal(self.controller.app_dict["withdraw"].get()) > Decimal(current_balance):
                self.withdraw_notify.config(fg='red', text="Insufficient Funds")
                return
            updated_balance = current_balance
            updated_balance = Decimal(updated_balance) - Decimal(self.controller.app_dict["withdraw"].get())
        with open(username, "w") as new_file:
            new_file.write(current_name + '\n')
            new_file.write(current_password + '\n')
            new_file.write(str(updated_balance))
            self.withdraw_notify.grid(row=6)
            self.withdraw_notify.config(fg='green', text="Balance Updated")
            self.balance_label.config(text="Current Balance $" + str(updated_balance))

    def restore_accountDashboard(self):
        self.controller.clear_frame(LoginPage)
        self.accountDashboard()


app = BankingApp(tk.Frame)
app.mainloop()
