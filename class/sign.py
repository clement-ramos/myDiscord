import customtkinter  # 3.11 python
from PIL import Image
import os
import string
import bcrypt
import settings
from datetime import datetime
import re

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 1200
    height = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ----- Generals  parameters -----
        self.title("My Discord")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # ERROR
        self.error_message_var = ""

        # load and create background image
        current_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets/")

        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/bg_gradient.jpg"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image).grid(row=0, column=0)

        # ---------- Login Frame ----------
        #Frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        #Logo
        self.logo_image = customtkinter.CTkImage(Image.open(current_path + "/logo.png"), size=(128, 128))
        self.logo_image_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.logo_image).grid(row=0, column=0, columnspan = 2, pady = (30, 10))

        #Labels
        customtkinter.CTkLabel(self.login_frame, text="My Discord", font=customtkinter.CTkFont(size=40, weight="bold")).grid(row=1, column=0, columnspan = 2, pady = (10, 40))
        customtkinter.CTkLabel(self.login_frame, text="Connection", font=customtkinter.CTkFont(size=30, weight="bold")).grid(row=2, column=0, columnspan = 2, padx=10, pady=30)

        #Inputs
        self.username_login_entry = customtkinter.CTkEntry(self.login_frame, width=300, placeholder_text="mail")
        self.username_login_entry.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

        self.password_login_entry = customtkinter.CTkEntry(self.login_frame, width=300, show="*", placeholder_text="password")
        self.password_login_entry.grid(row=4, column=0, columnspan=2, pady=10, padx=20)

        #Buttons
        self.sign_button = customtkinter.CTkButton(self.login_frame, text="Sign Up", command=self.sign_event, width=140)
        self.sign_button.grid(row=6, column=0, padx=10, pady=(15, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=140)
        self.login_button.grid(row=6, column=1, padx=10, pady=(15, 15))

        # ERROR
        self.error_login_label = customtkinter.CTkLabel(self.login_frame, text=self.error_message_var, font=customtkinter.CTkFont(size=14, weight="bold"), text_color="red")
        self.error_login_label.grid(row=5, column=0, columnspan=2, pady=10, padx=20)

        # ---------- Sign-Up Frame ----------

        #Frame
        self.sign_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sign_frame.grid_columnconfigure(0, weight=1)

        #Logo
        self.logo_image = customtkinter.CTkImage(Image.open(current_path + "/logo.png"), size=(128, 128))
        self.logo_image_label = customtkinter.CTkLabel(self.sign_frame, text="", image=self.logo_image).grid(row=0, column=0, columnspan = 2, pady = (30, 10))

        #Labels
        customtkinter.CTkLabel(self.sign_frame, text="Sign-Up", font=customtkinter.CTkFont(size=40, weight="bold")).grid(row=1, column=0, columnspan = 2, pady = (10, 40))

        #Inputs
        self.first_name_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="first name")
        self.first_name_entry.grid(row=2, column=0, columnspan=2, pady=10, padx = 20)

        self.name_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="name")
        self.name_entry.grid(row=3, column=0, columnspan=2, pady=10, padx = 20)

        self.email_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="email")
        self.email_entry.grid(row=4, column=0, columnspan=2, pady=10, padx=20)

        self.username_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="username")
        self.username_entry.grid(row=5, column=0, columnspan=2, pady=10, padx=20)

        self.password_entry = customtkinter.CTkEntry(self.sign_frame, show="*", width=300, placeholder_text="password")
        self.password_entry.grid(row=6, column=0, columnspan=2, pady=10, padx=20)

        self.confirm_password_entry = customtkinter.CTkEntry(self.sign_frame, show="*", width=300, placeholder_text="confirm password")
        self.confirm_password_entry.grid(row=7 , column=0, columnspan=2, pady=10, padx=20)

        #Buttons
        self.register_button = customtkinter.CTkButton(self.sign_frame, text="register", command=self.register_event, width=150)
        self.register_button.grid(row=9, column=0, padx=10, pady=(30, 15))

        self.back_button = customtkinter.CTkButton(self.sign_frame, text="back", command=self.back_event, width=150)
        self.back_button.grid(row=9, column=1, padx=10, pady=(30, 15))

        # ERROR LABEL
        self.error_label = customtkinter.CTkLabel(self.sign_frame, text=self.error_message_var, font=customtkinter.CTkFont(size=14, weight="bold"), text_color="red")
        self.error_label.grid(row=8, column=0, columnspan=2, pady=10, padx=20)



        # ---------- Sign-Up Frame ----------

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)

        self.back_button = customtkinter.CTkButton(self.main_frame, text="back", command=self.back_event, width=200)
        self.back_button.grid(row=0, column=0, padx=10, pady=(30, 15))

    def login_event(self):
        # login user check (password, email, username, etc...)
        if self.login_user(self.username_login_entry.get(), self.password_login_entry.get()):
            self.login_frame.grid_forget()
            self.main_frame.grid(row=0, column=0, sticky="nsew")

    def back_event(self):
        self.sign_frame.grid_forget()  # remove sign frame
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def register_event(self):

        # register user check (password, email, username, etc...)
        if self.register_user(self.first_name_entry.get(), self.name_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get()):
            self.sign_frame.grid_forget()  # remove sign frame
            self.login_frame.grid(row=0, column=0, sticky="ns")  # show main frame

    def sign_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.sign_frame.grid(row=0, column=0, sticky="ns")  # show main frame

    def check_if_password_is_ok(self, password):
        # check if password as at least 8 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

    def crypt_password(self, password):
        # crypt password before saving it in database using bcrypt
        crypt = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        print("password:", password, "crypt:", crypt)
        return crypt

    def check_if_password_is_correct(self, password, crypt):
        # check if password is correct
        if bcrypt.checkpw(password.encode('utf-8'), crypt.encode('utf-8')):
            print("password is correct")
            return True
        else:
            print("password is not correct")
            return False

    def check_if_account_exists(self, email):
        # check if account exists in database using email
        sql = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        settings.cursor.execute(sql, val)
        result = settings.cursor.fetchall()
        if len(result) > 0:
            print(f"account with email {email} already exists")
            return True
        else:
            print(f"account with email {email} does not exist")
            return False

    def check_if_email_is_valid(self, email):
        # check if email is valid
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            self.set_error_message("email is not valid")
            return False

    def register_user(self, first_name, name, email, username, password):
        # check if account already exists
        if self.check_if_account_exists(email):
            self.set_error_message("account already exists")
            return False
        # check if email is valid
        if not self.check_if_email_is_valid(email):
            self.set_error_message("email is not valid")
            return False
        # check if password is ok
        if not self.check_if_password_is_ok(password):
            self.set_error_message("password is not ok")
            return False
        if self.name_entry.get() == "":
            self.set_error_message("name is empty")
            return False
        if self.first_name_entry.get() == "":
            self.set_error_message("first name is empty")
            return False
        if self.username_entry.get() == "":
            self.set_error_message("username is empty")
            return False
        # check if password is same as confirm password
        if password != self.confirm_password_entry.get():
            self.set_error_message("passwords are not the same")
            return False
        sql = "INSERT INTO users (first_name, name, email, username, password_hash, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (first_name, name, email, username, self.crypt_password(password), datetime.now())
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(f"account with email {email} created and saved in database at {datetime.now()}")
        return True

    def login_user(self, email, password):
        # check if account exists
        print(f"email: {email}, password: {password}")
        if not self.check_if_account_exists(email):
            self.set_error_message("account does not exist")
            return False
        # check if password is correct
        else:
            sql = "SELECT password_hash FROM users WHERE email = %s"
            val = (email,)
            settings.cursor.execute(sql, val)
            result = settings.cursor.fetchall()
            print("result:", result[0][0])
            if self.check_if_password_is_correct(password, result[0][0]):
                print("password is correct")
                return True
            else:
                self.set_error_message("password is not correct")
                return False

    def set_error_message(self, message):
        self.error_message_var = message
        self.error_label.configure(text=self.error_message_var)
        self.error_login_label.configure(text=self.error_message_var)
        # after 2 seconds, remove error message
        self.after(2000, self.remove_error_message)

    def remove_error_message(self):
        self.error_message_var = ""
        self.error_label.configure(text=self.error_message_var)
        self.error_login_label.configure(text=self.error_message_var)


if __name__ == "__main__":
    app = App()
    app.mainloop()