import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image
import os
import mysql.connector
from objects import LoggedIn

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="canteenmanagement"
)
mycursor = mydb.cursor()


mycursor.execute('INSERT INTO loggedin(username,password) values(%s,%s)', ("doller","123123"))
mycursor.execute('SELECT username,password FROM loggedin')
logged_in = mycursor.fetchone()
global current_user
global current_pass
print(logged_in)
current_user = logged_in[0]
current_pass = logged_in[1]
#mydb.commit()


    
customtkinter.set_appearance_mode("Dark")

DIRPATH = os.path.dirname(os.path.abspath(__file__))

themepath = os.path.join(DIRPATH, "red.json")

if os.path.exists(themepath):       
    customtkinter.set_default_color_theme(themepath)
else:
    customtkinter.set_default_color_theme("blue")

class CIMOS_Admin(customtkinter.CTk):
    def __init__(self):
        super().__init__() 
        
        def delete_loggedin():
            logout = LoggedIn(current_user, current_pass)
            logout.log_out()
            self.destroy()

        def delete_loggedin2():
            logout = LoggedIn(current_user, current_pass)
            logout.log_out()

        def goto_employee():
            self.destroy()
            import EmployeePage

        def goto_menu():
            self.destroy()
            import menu

        def goto_sales():
            print('placeholder command')
            return

        def logout():
            response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if response == 1:
                delete_loggedin2()
                self.destroy()
                os.system('python Login.py')
            else:
                return


        # configure window class CIMOS_Admin
        self.title("CIMOS Admin")
        self.geometry(f"1000x580+350+130")
        #self.bind("<1>", lambda event: event.widget.focus_set())
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.backg = customtkinter.CTkImage(Image.open(os.path.join("he.png")), size=(780,700))
        self.Image_label = customtkinter.CTkLabel(self, text="", image=self.backg, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(220,0))

        #Admin Profile
        self.my_frame = customtkinter.CTkFrame(self, width=220, corner_radius=0)
        self.my_frame.grid(row=0, column=0, rowspan=4, columnspan=1 , sticky="nsw")
        self.profile = customtkinter.CTkImage(Image.open(os.path.join("user.ico")), size=(140,140))
        self.Image_label = customtkinter.CTkLabel(self.my_frame, text="", image=self.profile, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(40,40), pady=(30,70))
        self.linedesprof1 = tk.Frame(self.my_frame, width=45, height=2, bg="#9F0000")
        self.linedesprof1.grid(row=0,column=0, padx=(0,230), pady=(200,0))
        self.linedesprof2 = tk.Frame(self.my_frame, width=45, height=2, bg="#9F0000")
        self.linedesprof2.grid(row=0,column=0, padx=(230,0), pady=(200,0))
        self.logo_label = customtkinter.CTkLabel(self.my_frame, text="Admin Profile", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=(0,0), pady=(160, 0))
        self.outbutton = customtkinter.CTkButton(self.my_frame, text="Log out", bg_color="transparent", font=customtkinter.CTkFont(size=14, weight="bold"), command=logout)
        self.outbutton.grid(row=1, column=0, padx=(10,10), pady=(300,0), sticky="ew")
        label=tk.Label(self.my_frame, text="Change Password?", fg='black', bg="white", font=('Microsoft YaHei UI Light', 10))
        label.place(x=42, y=640)
        
        def pop():

            def fetch_loggedpass():
                mycursor.execute('SELECT password FROM loggedin')
                current_passw = mycursor.fetchone()
                mydb.commit()
                loggedpass = current_passw[0]
                return loggedpass

            def fetch_loggeduser():
                mycursor.execute('SELECT username FROM loggedin')
                current_userw = mycursor.fetchone()
                mydb.commit()
                loggeduser = current_userw[0]
                return loggeduser

            def update_password():
                if self.cupass_entry.get() == "" or self.nupass_entry.get() == "" or self.confirm_entry.get() == "":
                    messagebox.showerror("Error", "Please fill out all the fields!")
                else:
                    if self.cupass_entry.get() != fetch_loggedpass():
                        messagebox.showerror("Error", "Current password is incorrect!")
                    else:
                        if self.nupass_entry.get() != self.confirm_entry.get():
                            messagebox.showerror("Error", "New password and confirm password does not match!")
                        else:
                            if self.nupass_entry.get() == fetch_loggedpass():
                                messagebox.showerror("Error", "New password cannot be the same as the current password!")
                            else:
                                update = LoggedIn(fetch_loggeduser(), self.nupass_entry.get())
                                update.change_pass()
                                

                                collapse_()
                                

            def collapse_():
                self.cpass.configure(state='normal')
                self.passframe.destroy()
            self.cpass.configure(state='disabled')
            
            
            self.passframe = customtkinter.CTkFrame(self.my_frame, width=180, height=260, corner_radius=6, bg_color="transparent")
            self.passframe.grid(row=1, column=0, padx=(0, 0), pady=(0,80))
            cpass= tk.Button(self.passframe, width=3, height=1, text='x', border=0, bg="#333333", cursor='hand2', fg="white", font=('Microsoft YaHei UI', 12), command=collapse_)
            cpass.place(x=185, y=0)
        
            self.current = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="Current Password: ", text_color="white", bg_color="transparent")
            self.current.place(x=20, y=10)
            self.cupass_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
            self.cupass_entry.place(x=20, y=40)
        
            self.newp = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="New Password: ", text_color="white", bg_color="transparent")
            self.newp.place(x=20, y=70)
            self.nupass_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
            self.nupass_entry.place(x=20, y=100)
        
            self.conp = customtkinter.CTkLabel(self.passframe, font=('Microsoft YaHei UI Light', 10), text="Confirm Password: ", text_color="white", bg_color="transparent")
            self.conp.place(x=20, y=130)
            self.confirm_entry = customtkinter.CTkEntry(self.passframe, font=('Microsoft YaHei UI Light', 10), text_color="#000", fg_color="White", border_color='#9F0000', border_width=0, width=140, height=20)
            self.confirm_entry.place(x=20, y=160)
        
            changebutton = customtkinter.CTkButton(self.passframe, text="Change Password", bg_color="transparent", font=customtkinter.CTkFont('Microsoft YaHei UI', size=10, weight="bold"), command = update_password)
            changebutton.place(x=20, y=215)
            
        self.cpass= tk.Button(self.my_frame, width=9, text='Click here', border=0, bg="white", cursor='hand2', fg="#2B65EC", font=('Microsoft YaHei UI Light', 10), command=pop)
        self.cpass.place(x=160, y=638)
        
        
        
        
        #Interface Title
        self.labelframe=customtkinter.CTkFrame(master=self, width=220, height=10, corner_radius=9)
        self.labelframe.grid(row=0, column=0, padx=(240,20), pady=(60,230), sticky="new")
        self.logo_label = customtkinter.CTkLabel(self.labelframe, text="Canteen Management and Ordering System", font=customtkinter.CTkFont("NEXA", size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=115, pady=(10, 10))
        
        
        # choice
        self.choose_des1 = customtkinter.CTkFrame(self, height=200, fg_color="white")
        self.choose_des1.grid(row=0, column=0, columnspan=2, padx=(240,20) , pady=(140, 420), sticky="nsew")
        
        #------------------------------------------------------------------------------------------------------
        self.choose_frame = customtkinter.CTkFrame(self, height=200)
        self.choose_frame.grid(row=0, column=0, padx=(360,150) , pady=(170, 120), columnspan=3, sticky="nsew")
        self.buttonchoose = customtkinter.CTkFrame(self.choose_frame, width=450, height=35, fg_color="#666666")
        self.buttonchoose.place(x=20, y=237)
        self.empbutton = customtkinter.CTkButton(self.choose_frame, text="Employee", bg_color="#666666", font=customtkinter.CTkFont(size=14, weight="bold"), command=goto_employee)
        self.empbutton.grid(row=0, column=0, padx=(55,500), pady=(240,40))
        self.prodbutton = customtkinter.CTkButton(self.choose_frame, text="Menu", bg_color="#666666", font=customtkinter.CTkFont(size=14, weight="bold"), command=goto_menu)
        self.prodbutton.grid(row=0, column=0, padx=(30,0), pady=(240,40))
        #------------------------------------------------------------------------------------------------------
        self.linedes = tk.Frame(self.choose_frame, width=2, height=220, bg='#555555')
        self.linedes.grid(row=0,column=0, padx=(0,260), pady=(0,100))
        self.choose_des2 = customtkinter.CTkFrame(self, height=200, fg_color="white")
        self.choose_des2.grid(row=0, column=0, columnspan=2, padx=(240,20) , pady=(470, 90), sticky="nsew")
        
        #Image Icons
        self.image1 = customtkinter.CTkImage(light_image=Image.open(os.path.join("management2.png")), dark_image=Image.open(os.path.join("management1.png")),size=(160,160))
        self.Image_label = customtkinter.CTkLabel(self.choose_frame, text="", image=self.image1, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(0,450), pady=(0,70))
        self.image2 = customtkinter.CTkImage(Image.open(os.path.join("dish1.png")), dark_image=Image.open(os.path.join("dish (1).png")), size=(160,160))
        self.Image_label = customtkinter.CTkLabel(self.choose_frame, text="", image=self.image2, bg_color="transparent")
        self.Image_label.grid(row=0, column=0, padx=(35,0), pady=(0,70))


        self.protocol("WM_DELETE_WINDOW", delete_loggedin)

if __name__ == "__main__":
    app = CIMOS_Admin()
    app.mainloop()
        
        