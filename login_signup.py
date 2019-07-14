from tkinter import*
import os


def main():

    global root
    root = Tk()

    root.title("login/signup")
    root.geometry("300x200")

    Label(text = "Login/Signup", bg="grey", width="300", font="Arial, 30").pack()
    Label(text = "").pack()
    Button(text = "Login", width="30", font="15", command=login).pack()
    Label(text = "").pack()
    Button(text = "Signup", width="30", font="15", command=signup).pack()
    root.mainloop()


def login():
    root1=Toplevel(root)
    root1.title("Login")
    root1.geometry("300x200")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify=StringVar()
    password_verify=StringVar()
    
    Label(root1, text="Welcome to login page", font="30").pack()
    Label(root1, text = "").pack()
    Label(root1, text="Username *").pack()
    username_entry1=Entry(root1, textvariable=username_verify)
    username_entry1.pack()
    Label(root1, text="").pack()
    Label(root1, text="Password *").pack()
    password_entry1=Entry(root1, show="*", textvariable=password_verify)
    password_entry1.pack()
    Button(root1, text="Login", command=login_verify).pack()

def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1, "r")
        verify=file1.read().splitlines()
        if password1 in verify:
            print("login success")
        else:
            print("password not verified")
    else:
        print("user not found")

def signup():
    
    root2=Toplevel(root)
    root2.title("Signup")
    root2.geometry("400x400")

    global name
    global username
    global password
    global name_entry_reg
    global username_entry_reg
    global password_entry_reg

    name=StringVar()
    username=StringVar()
    password=StringVar()
    
    Label(root2, text="Welcome to Signup page", font="30").pack()
    Label(root2, text = "").pack()
    Label(root2, text = "Name").pack()
    name_entry_reg=Entry(root2, textvariable=name)
    name_entry_reg.pack()
    Label(root2, text = "").pack()
    Label(root2, text = "Username").pack()
    username_entry_reg=Entry(root2, textvariable=username)
    username_entry_reg.pack()
    Label(root2, text="").pack()
    Label(root2, text = "Password").pack()
    password_entry_reg=Entry(root2, show="*", textvariable=password)
    password_entry_reg.pack()
    Label(root2, text="").pack()
    Button(root2, text="Signup", font="14", command=signup_user).pack()

def signup_user():
    username_info=username.get()
    password_info=password.get()
    name_info=name.get()

    file=open(username_info+".txt", "w")
    file.write(name_info+"\n")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()

    name_entry_reg.delete(0, END)
    username_entry_reg.delete(0, END)
    password_entry_reg.delete(0, END)

    Label(text="Signup Successful").pack()


main()
