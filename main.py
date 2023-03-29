import customtkinter
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

        self.create_sign_in(current_path) #create ii and place it in the grid(show it)
        self.create_sign_up(current_path) #create it but doesnt place it
        self.create_main(current_path)
 


    def create_sign_in(self, path):
          # ---------- Login Frame ----------
        #Frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        #Logo
        self.logo_image = customtkinter.CTkImage(Image.open(path + "/logo.png"), size=(128, 128))
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


    def create_sign_up(self, path):
        
        # ---------- Sign-Up Frame ----------

        #Frame
        self.sign_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sign_frame.grid_columnconfigure(0, weight=1)

        #Logo
        self.logo_image = customtkinter.CTkImage(Image.open(path + "/logo.png"), size=(128, 128))
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
    
    
    def create_main(self, path):
        # ---------- Main Frame ----------

        #Frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=11)

        self.create_nav_1(path)
        self.create_nav_2()
        self.create_chat(path)


    def create_nav_1(self, path):
    
        # ---------- Nav 1 Frame ----------
        self.nav_1_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.nav_1_frame.grid(row=0, column=0, sticky="nsew") 

        self.nav_1_frame.grid_columnconfigure(0, weight=1)
        self.nav_1_frame.grid_rowconfigure(0, weight=1)
        self.nav_1_frame.grid_rowconfigure(1, weight=12)

        # 0 0 Home button that have to switch to friend mode 

        self.home_btn_image = customtkinter.CTkImage(Image.open(path + "/logo.png"), size=(64, 64))
        self.home_btn_button = customtkinter.CTkButton(self.nav_1_frame, height = 70, text="",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.home_btn_image, command = self.test).grid(row=0, column=0, sticky="nsew")
       
        # 1 0 Server list 

        #-------------------------------------------------------------------------------

        servers = ["Server1", "Server2","Server3", "Server4"]

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableButtons(self.nav_1_frame, width = 100, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        
        for i in range(len(servers)):  # add items with images
            self.scrollable_label_button_frame.add_item(f"{servers[i]}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "assets/", "globe.png"))))
     
        #-------------------------------------------------------------------------------

    def create_nav_2(self):

        # ---------- Nav 2 Frame ----------
        self.nav_2_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.nav_2_frame.grid(row=0, column=1, sticky="nsew") 

        self.nav_2_frame.grid_columnconfigure(1, weight=1)
        self.nav_2_frame.grid_rowconfigure(0, weight=1)
        self.nav_2_frame.grid_rowconfigure(1, weight=12)
        self.nav_2_frame.grid_rowconfigure(2, weight=1)
        
        # 0 1 Server name in server mode or add friend button in friend mode

        # by default add friend 
        self.test = customtkinter.CTkLabel(self.nav_2_frame, text="Server Name", font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=0, column=1)

        # en 1 1 friend list or channels list

        #-------------------------------------------------------------------------------

        friends = ["Obsydh", "sebni","NaturallyGifted", "GOULOUGOULOU"]

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableButtons(self.nav_2_frame, width = 150, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
        
        for i in range(len(friends)):  # add items with images
            self.scrollable_label_button_frame.add_item(f"{friends[i]}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "assets/", "user.png"))))
     
        #-------------------------------------------------------------------------------



        # 2 1 audio paraeter(mute) 
        
        customtkinter.CTkLabel(self.nav_2_frame, text="parameter", font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=2, column=1)

    def create_chat(self, path):
        
        # ---------- Chat Frame ----------
        self.chat_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.chat_frame.grid(row=0, column=2, sticky="nsew") 

        self.chat_frame.grid_columnconfigure(0, weight=5)
        self.chat_frame.grid_columnconfigure(1, weight=1)
        
        self.chat_frame.grid_rowconfigure(0, weight=1)
        self.chat_frame.grid_rowconfigure(1, weight=12)
        self.chat_frame.grid_rowconfigure(2, weight=1)
        # 0 2 Channel using or friend talking to

        self.main_label = customtkinter.CTkLabel(self.chat_frame, text="CustoTkinter\nMain Page",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, columnspan = 2, padx=30, pady= 10)

        # 1 2 Scrollable list of btn and chat with time posted
        messages = ["Server1", "Server2","Server3", "Server4"]

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableButtons(self.chat_frame, width = 700, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
        
        for i in range(len(messages)):  # add items with images
            self.scrollable_label_button_frame.add_item(f"{messages[i]}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "assets/", "globe.png"))))
     
        # 2 2 Input zone 
        self.text_entry = customtkinter.CTkEntry(self.chat_frame, width= 400, placeholder_text="CTkEntry").grid(row=2, column = 0, sticky = "e")


        self.send_btn_image = customtkinter.CTkImage(Image.open(path + "/play.png"), size=(32, 32))
        self.send_btn_button = customtkinter.CTkButton(self.chat_frame,  text="",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.send_btn_image, command = self.test).grid(row=2, column=1, sticky = "e")
       

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
    
    def test(self):
        print(1)

    def label_button_frame_event(self, item):
        self.nav_2_frame.grid_forget(self)
        self.test = customtkinter.CTkLabel(self.nav_2_frame, text=item, font=customtkinter.CTkFont(size=20, weight="bold")).grid(row=0, column=1)
        print(f"label button frame clicked: {item}")


class ScrollableButtons(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.button_list = []

    def add_item(self, item, image=None):

        button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text=item,
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=image, anchor="w")
        
        if self.command is not None:
            button.configure(command=lambda: self.command(item))

        button.grid(row=len(self.button_list), column=0, padx=5, sticky="ew")
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.button_list):
            if item == label.cget("text"):
                button.destroy()
                self.button_list.remove(button)
                return
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
