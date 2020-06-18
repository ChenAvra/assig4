import preProcessing
# import model
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename, Label, Button, Entry, IntVar, END, W, E


class OurGUI:

    def __init__(self, master):
        self.master = master
        master.title("countries")
        master.minsize(800,400)

        self.filename="C:\\Users\\Chen\\Desktop\\Dataset.xlsx"
        self.df=None

        self.e1 = Entry(self.master, width=40)
        self.e1.grid(row=1, column=1)

        master.lableFrame=LabelFrame(master,text="Open a file")
        master.lableFrame.grid(column = 0 , row = 1 , padx = 20 , pady = 20 )
        master.button=Button(master.lableFrame, text = "Browse A File",command=self.fileDialog)
        master.button.grid(column=1, row=1)


        Label(master, text='Number of clusters k').grid(row=2)
        e2 = Entry(master,width=40)
        e2.grid(row=2, column=1)

        Label(master, text='Number of runs').grid(row=3)
        e3 = Entry(master, width=40)
        e3.grid(row=3, column=1)
        # lambda: bot_analysis_frame(eventConditionL, eventBreakL)
        master.button = Button(master, text='Pre-process', width=25, command=lambda: self.preProc(self.filename))
        master.button.grid(column=1, row=4)

        master.button = Button(master, text='Cluster', width=25)
        master.button.grid(column=3, row=4)


    def fileDialog(self):

        self.filename=filedialog.askopenfilename(initialdir="/",title="Browse a file",filetype=(("xlsx","*jpg"),(" ALL FILES","*.*")))
        self.e1.insert(0, self.filename)

    def preProc(self,filename):
        self.df=preProcessing.preProcess(self.filename)
        messagebox.showinfo("message","Preprocessing completed successfully!")
        print(self.df)






