from tkinter import *
from 회원가입gui import info_login_comp
from 회원가입gui import info_warning

def loginch(usid,uspw):

    if (usid == uspw or uspw == "" or usid == "" or usid == "ID를 입력하십시오"):
        info_warning()
    else:
        f = open("id.txt", "r")

        id_1 = f.read()

        id_list = id_1.split('/')

        for a in range(len(id_list)):

                idresult = id_list[a].find(usid)

                if (idresult > 0 or idresult == 0):

                    pwresult = id_list[a].find(uspw)

                    if (pwresult > 0 or pwresult == 0):
                        info_login_comp()

                    else:
                        continue
                else:
                    continue

        f.close()
        info_warning()
