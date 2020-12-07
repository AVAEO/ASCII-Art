# ARCHIE HANCOCK CS GCSE #
#    Copyright © 2019-2020 Archie Hancock - All Rights Reserved
#    You may not use, distribute and modify this code
#    By Using this Program, You agree to the EULA associated with this program
 
##############################################################################################################################
# Imports Various UI Modules
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import filedialog
import re
Count = 0
 
 
##############################################################################################################################
# Enter RLE Behind Scenes
def RLE_Enter():
    try:
        RLELines = e1.get()
        if int(RLELines) <= 2:
            MsgBoxRLEEnterFew = tk.messagebox.showinfo ('Error','Too Few Lines Entered',icon = 'warning')
        elif int(RLELines) >= 21:
            MsgBoxRLEEnterMany = tk.messagebox.showinfo ('Error','Too Many Lines Entered',icon = 'warning')
        else:
            int(RLELines)
            e2.config(state = NORMAL)
            RLEButton.config (state = NORMAL)
            e1.config(state = DISABLED)
            RLELine.config(state = DISABLED)
            global RLEComplete
            RLEComplete = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if RLEComplete is None: 
                return
                  
    except:
        MsgBoxRLEInvalid = tk.messagebox.showinfo ('Error','Invalid Entry',icon = 'warning')

    

 
def RLE_Lines():
        alldata = []
        enterdata = e2.get()
        e2.delete(0, END)

        uncompressed = ""
        while len(enterdata) >= 3:
            uncompressed += enterdata[2] * int(enterdata[0:2])
            enterdata = enterdata[3:]
        alldata.append(uncompressed)

        for lineofdata in alldata:
            RLEComplete.write(lineofdata + "\n")

        ComplieRLE(1)

        
def ComplieRLE(arg):
        global RLEComplete
        CompleteFileName = RLEComplete.name

        RLELines = e1.get()
        linesdata = int(RLELines)
        global Count

        if arg == 1:
            Count += 1

        if Count == linesdata:
            RLEButton.config (state = DISABLED)
            Count = 0
            RLEComplete.close()
            fileopen = open(CompleteFileName)
            DATA = fileopen.read()
            fileopen.close()
            DisplayASCI = Tk()
            DisplayASCI.title("Display ASCI Art From RLE")
            DisplayASCI.minsize(width=600, height=600)
            w = Label(DisplayASCI, text=DATA, justify=LEFT, font="Consolas")
            w.pack()
            mainloop()



            
            
##############################################################################################################################
# Display ASCI Behind Scenes
def DisplayASCI():
    AsciDisplayFile =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))   


    try:
        f=open(AsciDisplayFile, "r")
        if f.mode == 'r':
            DisplayASCIContents =f.read()
            DisplayASCI = Tk()
            DisplayASCI.title("Display ASCI Art")
            DisplayASCI.minsize(width=600, height=600)
            w = Label(DisplayASCI, text=DisplayASCIContents, justify=LEFT, font="Consolas")
            w.pack()
            mainloop()
        else:
            MsgBoxASCIDisplay = tk.messagebox.showinfo ('Error','File Opened In Wrong Mode, Please Restart The Application',icon = 'warning')
    except:
        MsgBoxASCIDisplayInvalid = tk.messagebox.showinfo ('Error','Invalid File Entered',icon = 'warning')
    

        
 
        
##############################################################################################################################
# Convert ASCI Behind Scenes
def ConvertASCI():
    try:
        ASCIConvertFile =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))   
        f=open(ASCIConvertFile, "r")
        ConvertASCIContents = f
        if f.mode == 'r':
            LogoRLE = ConvertASCIContents.readlines()
            alldata = []
            for line in LogoRLE:
                uncompressed = ""
                while len(line) >= 3:
                    uncompressed += line[2] * int(line[0:2])
                    line = line[3:]
                alldata.append(uncompressed)
            ASCIConvertedFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            ConvertedFileName = ASCIConvertedFile.name
            if ASCIConvertedFile is None: 
                return
            for lineofdata in alldata:
                ASCIConvertedFile.write(lineofdata + "\n")
            ASCIConvertedFile.close()
            fileopen = open(ConvertedFileName)
            DATA = fileopen.read()
            fileopen.close()
            DisplayASCI = Tk()
            DisplayASCI.title("Display ASCI Art")
            DisplayASCI.minsize(width=600, height=600)
            w = Label(DisplayASCI, text=DATA, justify=LEFT, font="Consolas")
            w.pack()
            mainloop()
    except:
        ErrorBox = tk.messagebox.showinfo ('Error','Invalid File Entered',icon = 'warning')

    

     
 
##############################################################################################################################
# Convert RLE Behind Scenes

def ConvertRLE():
   
        RLEConvertFile =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))   
        RLELineFile = open(RLEConvertFile, "r")
        asciidata = RLELineFile.readlines()
        compresseddata = ""
        for asciiline in asciidata:
            currentcharacter = ""
            count = 0
            compressedline = ""
            for asciicharacter in asciiline:
                if asciicharacter == currentcharacter:
                    count += 1
                else:
                    if count < 10:
                        count = "0" + str(count)
                    else:
                        count = str(count)
                    if count != "00":
                        compressedline += count + currentcharacter
                    currentcharacter = asciicharacter
                    count = 1
            compresseddata += compressedline + "\n"
        datafile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        datafile.write(compresseddata)
        datafile.close()
        lengthofcompresseddata = len(compresseddata)
        lengthofuncompresseddata = 0
        for asciiline in asciidata:
            lengthofuncompresseddata += len(asciiline)
        differencefromcompressed = lengthofcompresseddata - lengthofuncompresseddata
        DisplayRLE = Tk()
        DisplayRLE.title("Display ASCI Art")
        DisplayRLE.minsize(width=300, height=200)
        x = Label(DisplayRLE, text="You Saved:", justify=LEFT, font="Consolas")
        w = Label(DisplayRLE, text=-differencefromcompressed, justify=LEFT, font="Consolas")
        z = Label(DisplayRLE, text="Characters", justify=LEFT, font="Consolas")
        x.pack()
        w.pack()
        z.pack()
        mainloop()

    
 

 
    
##############################################################################################################################
# Quit Application
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application',icon = 'warning')
 
 
##############################################################################################################################
# TK UI Ellements
# Base UI
window = Tk()
window.title("ASCI ART")
window.geometry('700x400')
tab_control = ttk.Notebook(window)
# Window Tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
# Window 1
tab_control.add(tab1, text='Enter RLE')
tab_control.add(tab2, text='Display ASCII art')
tab_control.add(tab3, text='Convert to ASCII art')
tab_control.add(tab4, text='Convert to RLE')
# Tab 1
lbl1 = Label(tab1, text= 'How many lines of RLE would you like to enter?')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab1, text= 'RLE Line Enter')
lbl2.grid(column=0, row=1)
e1 = tk.Entry(tab1)
e1.grid(row=0, column=1)
e2 = tk.Entry(tab1)
e2.grid(row=1, column=1)
RLELine = tk.Button(tab1, text='ENTER', command=RLE_Enter)
RLELine.grid(row=0, column=2)
RLEButton = tk.Button(tab1, text='ENTER', command=RLE_Lines)
RLEButton.grid(row=1, column=2)
# Tab 2
ASCIDButton = tk.Button(tab2, text= 'Select File', command=DisplayASCI)
ASCIDButton.grid(column=0, row=0)
# Tab 3
ASCIRLEButton = tk.Button(tab3, text= 'Select File', command=ConvertASCI)
ASCIRLEButton.grid(column=0, row=0)
# Tab 4
RLEConvertButton = tk.Button(tab4, text= 'Select File', command=ConvertRLE)
RLEConvertButton.grid(column=0, row=0)
# Dissable UI Entry
e2.config(state = DISABLED)
RLEButton.config (state = DISABLED)
# Quit Button
Button(window, text='QUIT', fg = "Red", command=ExitApplication).pack(side=BOTTOM)
# Restart Entry Point
def Reset():
    e2.delete(0, END)
    e2.config(state = DISABLED)
    RLEButton.config (state = DISABLED)
    e1.config(state = NORMAL)
    RLELine.config (state = NORMAL)
    e1.delete(0, END)
ResetButton = tk.Button(tab1, text='RESET', command=Reset)
ResetButton.grid(row=0, column=5)
# Window Complete
tab_control.pack(expand=1, fill='both')
window.mainloop()
 
