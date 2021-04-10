
from tkinter import *

def info_signup_comp():
    messagebox.showinfo ("알림", "회원가입이 완료되었습니다.")

def info_warning():
    messagebox.showinfo ("경고", "아이디와 비밀번호를 확인해주십시오.")

def info_login_comp():
    messagebox.showinfo("알림", "로그인 완료되었습니다.")

def signupmain():
    signup = Tk()
    signup.title("Sign up")
    signup.grid()
    signup.resizable(False, False)

    def signUp():
        usid = usid_entry.get()
        uspw = uspw_entry.get()

        # print("sign_up:" + usid + ":" + uspw)
        if usid != '':
            try:

                f = open("id.txt", "a")
                f.write(usid)
                f.write("|")
                f.write(uspw)
                f.write("/")

                f.close()
                info_signup_comp()

            except:
                info_warning()

    signup_label = Label(signup, text="Sign up")
    signup_label.grid(column=0, row=0, padx=3, pady=3)

    usid_label = Label(signup, text="ID")
    usid_label.grid(column=0, row=1, sticky = W)

    usid_entry = Entry(signup, width=30)
    usid_entry.grid(column=0, row=2, padx=3, pady=3, ipady=4)

    uspw_label = Label(signup, text="PW")
    uspw_label.grid(column=0, row=3, sticky = W)

    uspw_entry = Entry(signup, width=30)
    uspw_entry.grid(column=0, row=4, padx=3, pady=3, ipady=4)

    signup_btn = Button(signup, text="확인", command = signUp, width = 15)
    signup_btn.grid(padx=3, pady=3)

    signup.mainloop()
