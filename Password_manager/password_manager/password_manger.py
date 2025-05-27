# JAI SHREE RAM 
# ------------------Importing module -----------------------------------------------------------------
from tkinter import *
from pandas import *
from tkinter import ttk, messagebox
from tkinter import messagebox
import json
from genrate_password import password_gen 


#------------------Search the data -------------------------------------------------
def search():
   
    website=data_to_be_checked()
    try:
        with open('data.json','r') as file:
            data=json.load(file)
    except FileNotFoundError:
            messagebox.showerror(message="File Not Found ")

    else:        

        if website in data:
            email=data[website]["Email"]
            password=data[website]["password"]
            messagebox.showinfo(message=f"Email:{email}\n Password:{password}\n",title=f"Search_Details:-{website} ")
        else:    

            messagebox.showwarning(message=f"No data Found{website} ",title="Error")

    

    


# --------------------------------------data to be checked-------------------------------------------------
def data_to_be_checked():
    data=website_entry.get()
    return data

# check the data is there in file 
def check_details():
    with open( 'data.json',"r") as file:
        content=file.read()
        if len(data_to_be_checked())==0:
            messagebox.showwarning(message="Please enter the details\n",title="Details")
        else:
            if data_to_be_checked() in content:
                messagebox.showinfo(message="website user data is already avaliable please check the file\n",title="Check")
        
# ---------------------------- Password genrate from other file(from password genrater module) ---------------------------------------------------- 
def password_genrate():
    password = password_gen()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# Save Password in txt or xls or Json
# User can choose any file like Text , Excel, Json 
# I recommend to choose Json file for more useful 

# -----------------------------------------Data logging for the Json file ---------------------------------------------------
def data_logging_json():
    website=website_entry.get()
    email=Email_enrty.get()
    password=password_entry.get()
    new_data={
        website: {
        
        "Email":email,
        "password":password,
    }
    }

    if len(website and email and password)==0:
        messagebox.showwarning(title=Warning,message="Invalid Entry")
    else:
        msg_box_ok_cancel=messagebox.askokcancel(title=website,message=f"check for EMAIL:{email}\n Check for Password:{password}")    
        if msg_box_ok_cancel:
            try:
                with open('data.json',"r") as file:

                
                    data=json.load(file)
            except FileNotFoundError:
                     with open("data.json","w") as file:
                    
                        json.dump(new_data,file,indent=4)

            else:
                data.update(new_data)
               
                    
            finally:
                website_entry.delete(0,END)
                Email_enrty.delete(0,END)
                password_entry.delete(0,END)
        return messagebox.showinfo(message="successful")   
                
                    


                
                     
# ----------------------------------------------Data loggong for text file-------------------------------------------
def data_logging():
    
    website=website_entry.get()
    email=Email_enrty.get()
    password=password_entry.get()
    

    if len(website and email and password)==0:
         messagebox.showwarning(title=Warning,message="Invalid Entry ")
    else :
        msg_box_ok_cancle=messagebox.askokcancel(title=website,message=f"check for EMAIL :{email}\n Check for Password:{ password}")

        if msg_box_ok_cancle:
            with open('data.txt','a')as file :
                file.write(f" {website}|{email}|{password}\n")
                website_entry.delete(0,END)
                Email_enrty.delete(0,END)
                password_entry.delete(0,END)
        return messagebox.showinfo(message="successful")    

#  GUI for data entry 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("🔐 PASSWORD MANAGER")
window.geometry("600x450")
window.config(bg="#ecf0f1", padx=30, pady=30)

# ---------------------------- HEADER ------------------------------- #
header_frame = Frame(window, bg="#ff6f61", bd=0)
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 20))
header_label = Label(header_frame, text="|| जय श्री राम ||", font=("Segoe UI", 20, "bold"), bg="#ff6f61", fg="white", pady=15)
header_label.pack(fill="x")

# ---------------------------- LABELS ------------------------------- #
label_font = ("Segoe UI", 12, "bold")
entry_font = ("Segoe UI", 10)

website_lable = Label(window, text="WEBSITE:", font=label_font, bg="#ecf0f1", fg="#2c3e50")
website_lable.grid(row=1, column=0, sticky='e', pady=10)

Email_lable = Label(window, text="Email:", font=label_font, bg="#ecf0f1", fg="#2c3e50")
Email_lable.grid(row=2, column=0, sticky='e', pady=10)

password_label = Label(window, text="Password:", font=label_font, bg="#ecf0f1", fg="#2c3e50")
password_label.grid(row=3, column=0, sticky='e', pady=10)

# ---------------------------- ENTRIES ------------------------------- #
style = ttk.Style()
style.configure("TEntry", padding=6, font=entry_font)

website_entry = ttk.Entry(width=32)
website_entry.grid(row=1, column=1, pady=10, sticky='w')
website_entry.focus()

Email_enrty = ttk.Entry(width=32)
Email_enrty.grid(row=2, column=1, pady=10, sticky='w')

password_entry = ttk.Entry(width=22)
password_entry.grid(row=3, column=1, pady=10, sticky='w')

# ---------------------------- BUTTONS ------------------------------- #
style.configure("TButton",
    font=("Segoe UI", 10, "bold"),
    padding=6,
    relief="flat",
    background="#3498db",
    foreground="white"
)

def create_colored_button(text, command, row, column, padx=5, pady=10):
    btn = Button(window, text=text, command=command, font=("Segoe UI", 10, "bold"),
                 bg="#3498db", fg="white", activebackground="#2980b9",
                 relief="flat", bd=0, padx=10, pady=5)
    btn.grid(row=row, column=column, padx=padx, pady=pady)
    return btn

Genrate_password_button = create_colored_button("Generate", password_genrate, 3, 2)
search_button = create_colored_button("Search", search, 1, 2)
check_button = create_colored_button("Check", check_details, 4, 0)
add_button = create_colored_button("ADD", data_logging_json, 4, 2)

# ---------------------------- MAINLOOP ------------------------------- #
window.mainloop()
