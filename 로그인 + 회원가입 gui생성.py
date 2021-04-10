from tkinter import *
from tkinter import messagebox
from 회원가입gui import signupmain
from 로그인gui import loginch
from 회원가입gui import info_warning

def logincheck():
    usid = usid_entry.get()
    uspw = uspw_entry.get()

    loginch(usid,uspw)


root = Tk()
root.title("testing")
id_entry = str(" ")
pw_entry = str(" ")

label_comment = Label(root, text="Welcome")
label_comment.grid(column=0, row=0)

usid_entry = Entry(root, width=30)
usid_entry.grid(ipady=4, padx=3, pady=3)
usid_entry.insert(0, 'ID를 입력하세요')

uspw_entry = Entry(root, width=30)
uspw_entry.grid(ipady=4, padx=3, pady=3)
uspw_entry.insert(0, 'PW를 입력하세요')

btn_login = Button(root, text="login", width=29, height=2, command=logincheck)
btn_login.grid(column=0, row=3, padx=5, pady=3)

btn_signup = Button(root, text="Sign up", command=signupmain, width=13)
btn_signup.grid(column=0, row=4, padx=3, pady=3)
root.resizable(False, False)

root.mainloop()
