# Bank_App_OOP
REFACTORED IN OOP.
BankingApp
Banking GUI -This is a Tkinter Library-based Banking Application.

-Modules used:

Tkinter sys PIL OS decimal(Currency) When you run the application, it opens a centered GUI window that asks for the user to either register or log in.

Register: Once you click on the register button, it opens a new screen that asks you to input you Name, Age, Gender, 
your password(* hidden), select a recovery question and provide the answer(* hidden) 
Once you press register, it will save the user information into its own separate txt file. Note: If the account already exists, 
a message below the register button will prompt "Account Exists"

Login: Once you click on the login button, it opens a new screen that asks you to input your login credentials. 
Note: If password or user is incorrect, invalid message will prompt below the Login button.

Once logged in successfully, you will be brought to your respective account's dashboard.

Three options:

Personal Details - Shows the users' personal details, such as Name, Age, Gender and Balance. (NEVER THE PASSWORD OR RECOVERY QUESTION/ANSWER)

Deposit - Opens a new window that allows User to deposit a specific amount in decimal form. 
Will also show the User's current balance. If deposited amount is either a negative or the integer 0, 
an error message will prompt below the finish button. If deposit is successful, a message will prompt that Account has been updated!

Withdraw - Opens a new window that allows User to withdraw a specific amount in decimal form. 
Will also show the User's current balance. If withdrawal amount is either a negative or the integer 0, 
an error message will prompt below the finish button. An error wil ALSO show if the amount withdrawn exceeds the current balance amount. 
If withdrawal is successful, a message will prompt that Account has been updated!

All successful updates will be saved into the respective User's text file.

Will continue to work on new updates... Will also implement an SQL database for specific Users...
