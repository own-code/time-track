#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='cyan')
#gui.geometry('300x200')

def get(Nompatient, entree, Birthvalue, Birth_entree):
    """
    Add a patient with
    add button
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:

        mot = "-"
        mot2 = "--"
        mot3 = "---"
        mot4 = "----"
        mot5 = "-----"
        mot6 = "------"
        mot7 = "-------"
        mot8 = "--------"
        mot9 = "---------"
        mot10 = "----------"
        mot11 = "-----------"
        mot12 = "------------"
        mot13 = "-------------"
        mot14 = "--------------"
        mot15 = "---------------"
        mot16 = "----------------"
        mot17 = "-----------------"
        mot18 = "------------------"
        mot19 = "-------------------"
        mot20 = "--------------------"
        mot21 = "---------------------"
        mot22 = "----------------------"
        mot23 = "-----------------------"
        mot24 = "------------------------"

        Nompatient = entree.get()
        Birthvalue = Birth_entree.get()
        print(Nompatient)
        print(Birthvalue)


        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot2 in line:
                        searchLine2(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot3 in line:
                        searchLine3(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        searchLine4(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot8 in line:
                        searchLine8(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot9 in line:
                        searchLine9(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot10 in line:
                        searchLine10(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot11 in line:
                        searchLine11(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot12 in line:
                        searchLine12(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot13 in line:
                        searchLine13(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot14 in line:
                        searchLine14(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot15 in line:
                        searchLine15(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot16 in line:
                        searchLine16(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot17 in line:
                        searchLine17(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot18 in line:
                        searchLine18(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot19 in line:
                        searchLine19(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot20 in line:
                        searchLine20(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile21.txt'):
            with open('./newpatient/entryfile21.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot21 in line:
                        searchLine21(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile22.txt'):
            with open('./newpatient/entryfile22.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot22 in line:
                        searchLine22(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile23.txt'):
            with open('./newpatient/entryfile23.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot23 in line:
                        searchLine23(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile24.txt'):
            with open('./newpatient/entryfile24.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot24 in line:
                        searchLine24(Nompatient, Birthvalue)
        else:
            print("There is no file to edit as entryfile")

        gui.destroy()

def searchLine1(Nompatient, Birthvalue):
        file = open('./newpatient/entryfile.txt', 'w')
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')
        file.close()

def searchLine2(Nompatient, Birthvalue):
        file = open('./newpatient/entryfile2.txt', 'w')
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')
        file.close()

def searchLine3(Nompatient, Birthvalue):
    with open('./newpatient/entryfile3.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine4(Nompatient, Birthvalue):
    with open('./newpatient/entryfile4.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine5(Nompatient, Birthvalue):
    with open('./newpatient/entryfile5.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine6(Nompatient, Birthvalue):
    with open('./newpatient/entryfile6.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine7(Nompatient, Birthvalue):
    with open('./newpatient/entryfile7.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine8(Nompatient, Birthvalue):
    with open('./newpatient/entryfile8.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine9(Nompatient, Birthvalue):
    with open('./newpatient/entryfile9.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine10(Nompatient, Birthvalue):
    with open('./newpatient/entryfile10.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine11(Nompatient, Birthvalue):
    with open('./newpatient/entryfile11.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine12(Nompatient, Birthvalue):
    with open('./newpatient/entryfile12.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine13(Nompatient, Birthvalue):
    with open('./newpatient/entryfile13.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine14(Nompatient, Birthvalue):
    with open('./newpatient/entryfile14.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine15(Nompatient, Birthvalue):
    with open('./newpatient/entryfile15.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine16(Nompatient, Birthvalue):
    with open('./newpatient/entryfile16.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine17(Nompatient, Birthvalue):
    with open('./newpatient/entryfile17.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine10(Nompatient, Birthvalue):
    with open('./newpatient/entryfile10.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine18(Nompatient, Birthvalue):
    with open('./newpatient/entryfile18.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine19(Nompatient, Birthvalue):
    with open('./newpatient/entryfile19.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine20(Nompatient, Birthvalue):
    with open('./newpatient/entryfile20.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine21(Nompatient, Birthvalue):
    with open('./newpatient/entryfile21.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine22(Nompatient, Birthvalue):
    with open('./newpatient/entryfile22.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine23(Nompatient, Birthvalue):
    with open('./newpatient/entryfile23.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine24(Nompatient, Birthvalue):
    with open('./newpatient/entryfile24.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')


labelName = Label(gui)
labelName = Label(text='Enter Name and Surname : ', font="Times 14 bold", 
    fg='RoyalBlue4', bg='cyan')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='light sky blue', bd=4)
entree.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birth_entree = Entry(gui, textvariable=Birthvalue, highlightbackground='light sky blue', bd=4)
Birth_entree.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='white', bg='RoyalBlue4', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command = lambda: get(Nompatient, entree, Birthvalue, Birth_entree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue4', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
