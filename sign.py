import customtkinter # 3.11 python
from PIL import Image
import os

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

        # load and create background image
        current_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/")
        
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
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=300, placeholder_text="username")
        self.username_entry.grid(row=3, column=0, columnspan = 2, pady=10, padx = 20)

        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=300, show="*", placeholder_text="password")
        self.password_entry.grid(row=4, column=0, columnspan = 2, pady=10, padx = 20)

        #Buttons
        self.sign_button = customtkinter.CTkButton(self.login_frame, text="Sign Up", command=self.sign_event, width=140)
        self.sign_button.grid(row=5, column=0, padx=10, pady=(15, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=140)
        self.login_button.grid(row=5, column=1, padx=10, pady=(15, 15))

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
        self.first_name_entry.grid(row=2, column=0, pady=10, padx = 20)

        self.name_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="name")
        self.name_entry.grid(row=3, column=0, pady=10, padx = 20)

        self.email_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="email")
        self.email_entry.grid(row=4, column=0, pady=10, padx = 20)

        self.username_entry = customtkinter.CTkEntry(self.sign_frame, width=300, placeholder_text="username")
        self.username_entry.grid(row=5, column=0, pady=10, padx = 20)

        self.password_entry = customtkinter.CTkEntry(self.sign_frame, show="*", width=300, placeholder_text="password")
        self.password_entry.grid(row=6, column=0, pady=10, padx = 20)

        self.confirm_password_entry = customtkinter.CTkEntry(self.sign_frame, show="*", width=300, placeholder_text="confirm password")
        self.confirm_password_entry.grid(row=7 , column=0, pady=10, padx = 20)

        #Buttons
        self.register_button = customtkinter.CTkButton(self.sign_frame, text="register", command=self.register_event, width=200)
        self.register_button.grid(row=8, column=0, padx=10, pady=(30, 15))


        # ---------- Sign-Up Frame ----------

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)

        self.back_button = customtkinter.CTkButton(self.main_frame, text="back", command=self.back_event, width=200)
        self.back_button.grid(row=0, column=0, padx=10, pady=(30, 15))

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        # Test if password is ok

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame

    def register_event(self):

        # Test if informatins is ok

        self.sign_frame.grid_forget()  # remove sign frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show main frame

    def sign_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.sign_frame.grid(row=0, column=0, sticky="ns")  # show main frame
if __name__ == "__main__":
    app = App()
    app.mainloop()