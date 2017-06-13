import tkinter as tk                # python 3
from tkinter import *
import tkinter as Tkinter   # Python 3
import tkinter.ttk as ttk
from tkinter import font  as tkfont # python 3
from tkinter import Label
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto import Random
import pandas
import os

import time

global e1
names1=[]
var1 = []
filepath1=""
box_num1 = 0
boxes1 = []
box_vars1 = []


class CrypDex(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.minsize(width=500, height=500)
        global status
        status = Label(self, text="", bd=1, bg='white', relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, EncryptPage, DecryptPage, PerfEncryp, PerfDecryp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Crypdex!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        encryptButton = tk.Button(self, text="Encrypt File",
                                  command=lambda: controller.show_frame("EncryptPage"))
        decryptButton = tk.Button(self, text="Decrypt file",
                                  command=lambda: controller.show_frame("DecryptPage"))
        encryptButton.pack(fill="none", expand=True)
        decryptButton.pack(fill="none", expand=True)


class EncryptPage(tk.Frame):
    def openFile1(self):
        global encFile1
        global filepath1
        filepath1 = filedialog.askopenfilename()
        self.changeLocation1()
        global v1
        if(v1.get()==1):
            encFile1 = pandas.read_csv(filepath1, dtype={'branch': str, 'account': str, 'daily_balance': str, 'date': str,
                                                       'branch_cluster': str, 'pmjdy': str, 'date1': str, 'date2': str,
                                                       'description': str, 'debit_credit': str, 'amount': str,
                                                       'debit_credit1': str, 'balance': str, 'journal_no': str,
                                                       'updated_acct': str, 'max_date': str, 'max_date_demon': str,
                                                       'cif_s1': str, 'name_s1': str, 'open_date_s1': str,
                                                       'mobile_s1': str, 's1_info': str, 'cif_s2': str,
                                                       'open_date_s2': str, 'dateofbirth_s2': str,
                                                       'mobno_account_s2': str, 'atm_account_s2': str,
                                                       'sms_account_s2': str, 'mobno_cif_s2': str, 'female_cif_s2': str,
                                                       'male_cif_s2': str, 's2_info': str, 'savings_type': str,
                                                       'acct_holder_age': str, 'working_age': str,
                                                       'female_working': str, 'female_non_working': str,
                                                       'male_working': str, 'male_non_working': str,
                                                       'zero_balance': str, 'year': str, 'month': str, 'day': str,
                                                       'first_trans': str, 'first_trans_date': str,
                                                       'last_trans_date': str, 'open_date': str, 'ATM': str,
                                                       'ATM_others': str, 'POS': str, 'CSH': str, 'CSH_WDL': str,
                                                       'CSH_DEP': str, 'CHQ': str, 'thru_CHQ': str, 'OWN_CHQ_DP': str,
                                                       'WDL_TX_CHQ': str, 'CSH_WDL_Chq': str, 'CHQ_DEP': str,
                                                       'CHQ_others': str, 'DEP_TX': str, 'SCHOLARSHIP': str,
                                                       'WDL_TX': str, 'NEFT': str, 'IMPS': str, 'RTGS': str,
                                                       'CREDIT_BULK': str, 'PMJJBY': str, 'PMJJBY_renewal': str,
                                                       'PMJJBY_first': str, 'PMSBY': str, 'PMSBY_renewal': str,
                                                       'TFR_DB': str, 'TFR_CR': str, 'NPCI': str, 'LPG_SUBSIDY': str,
                                                       'LPG_availed': str, 'LPG_amount': str, 'AADHAAR': str,
                                                       'FTRNO': str, 'SUPPLECS': str, 'SGT': str, 'VLR': str,
                                                       'PENSION': str, 'SGT_PEN': str, 'FTRNO_availed': str,
                                                       'SUPPLECS_availed': str, 'SGT_availed': str, 'VLR_availed': str,
                                                       'PENSION_availed': str, 'FTRNO_amount': str,
                                                       'SUPPLECS_amount': str, 'SGT_amount': str, 'VLR_amount': str,
                                                       'PENSION_amount': str, 'POS_amount': str, 'SGT_PEN_amount': str,
                                                       'LIC': str, 'TDS': str, 'SAL': str, 'CR_INT_CR': str,
                                                       'CR_INT_DB': str, 'REPIN8': str, 'AMC_ATM': str, 'CHARGES': str,
                                                       'SMS': str, 'INTR_CTY_CHRG': str, 'COMBINE1': str,
                                                       'COMBINE': str, 'DB_TRF_ALL': str, 'CR_TRF_ALL': str,
                                                       'ACTIVE_WDL': str, 'ACTIVE_DEP': str, 'ALL_CHARGES': str,
                                                       'CRDT_BLK': str, 'total_remain': str, 'CRDT_BLK_Others': str,
                                                       'INTEREST': str, 'unexplained': str, 'govt_init_trans': str,
                                                       'govt_assisted_acc': str, 'SAL_account': str, 'SAL_savings': str,
                                                       'SAL_pmjdy': str, 'trans_identified': str, 'age': str,
                                                       'age_quarter': str, 'age_month': str,
                                                       'quarter_govt_assisted': str, 'month_govt_assisted': str,
                                                       'MOBILE_linked': str, 'SMS_charged_account': str,
                                                       'AADHAAR_linked': str})

        elif(v1.get()==2):
            encFile1=pandas.read_csv(filepath1, dtype={'accno': str, 'account_type': str, 'CIF': str, 'customer_name': str, 'limit': str, 'interest_rate': str, 'theo_balance': str, 'outstanding': str, 'irregularity': str,'emi_due': str, 'emi_paid': str, 'emi_overdue': str, 'new_irac': str,'arrear_cond': str, 'currency': str, 'acct_maintain_branch': str,'emi_installment_amt': str, 'unrealised_int': str, 'accru_int': str,'file_date	': str, 'branch': str, 'sanction_date': str, 'irregularity_date': str,'emi_installment': str})
        self.Ecolumns1.config(state="normal")
        global names1
        names1=list(encFile1.columns.values)

    def create_window(self):
        t1 = tk.Toplevel(self)
        global canvas1
        canvas1 = tk.Canvas(t1)
        canvas1.pack(side=tk.LEFT)
        scrollbar1= tk.Scrollbar(t1, command=canvas1.yview)
        scrollbar1.pack(side=tk.LEFT, fill='y')

        canvas1.configure(yscrollcommand=scrollbar1.set)

        frame1 = tk.Frame(canvas1)
        canvas1.create_window((0, 0), window=frame1, anchor='nw')
        canvas1.bind('<Configure>', self.on_configure1)

        t1.wm_title("Choose the columns...")
        frame1.grid_columnconfigure(0, weight=1)
        butt1=Button(frame1, text="Confirm",command = t1.destroy)
        global names1
        butt1.pack()
        global var1
        global box_num1
        global boxes1
        global box_vars1
        global box_num1
        for name in names1:
            box_vars1.append(tk.IntVar())
            boxes1.append(tk.Checkbutton(frame1, text=name, variable=box_vars1[box_num1]))
            box_vars1[box_num1].set(0)
            boxes1[box_num1].pack()
            box_num1 +=1


    def on_configure1(self,event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas1.configure(scrollregion=canvas1.bbox('all'))

    def changeLocation1(self):
        labelLocation1.config(text=filepath1)
    def changeStatus1(self,Text):
        status.config(text=Text)

    def selected1(self):
        fileButton1.config(state="normal")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ENCRYPTION", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        backButton1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("MainPage"))
        labelFile1=Label(self,text="File")
        global fileButton1
        fileButton1=tk.Button(self,text="Browse",command=self.openFile1,state=DISABLED)
        global labelLocation1
        labelLocation1=Label(self,text="",bd=1,bg='white',width=50, height=2,relief=SUNKEN,anchor=W)
        global names1
        global okButton1
        okButton1=Button(self, text="Continue",command=lambda: controller.show_frame("PerfEncryp"))
        global v1
        v1= IntVar()
        Radiobutton(self, text="Loan Data", variable=v1, value=2,command=self.selected1).pack(anchor=W)
        Radiobutton(self, text="Savings Data", variable=v1, value=1,command=self.selected1).pack(anchor=W)
        self.changeStatus1("Please choose the type of file, and add file location...")
        labelFile1.pack(padx=5, pady=10, side=LEFT)
        labelLocation1.pack(padx=5, pady=10, side=LEFT)
        fileButton1.pack(padx=5, pady=10, side=LEFT)
        backButton1.pack(fill="none", expand=True)
        self.Ecolumns1 = Button(self, state=DISABLED, text="Choose the columns to encrypt",
                               command=self.create_window)
        self.Ecolumns1.pack()
        okButton1.pack()


class PerfEncryp(tk.Frame):

    def start_now(self):
        name=self.e1.get()
        global names1
        global var1
        global box_num1
        global boxes1
        global box_vars1
        global box_num1
      # here you have ints but when calc. %'s usually floats
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        public_key = key.publickey()
        global v1
        global encFile1
        global var1

        if v1.get() == 1:
            for i in range(len(names1)):
                if box_vars1[i].get() == 1:
                    for index, row in encFile1.iterrows():
                        pres=names1[i]
                        encFile1[pres].values[index] = public_key.encrypt((encFile1[pres].values[index]).encode("utf8"),
                                                                      32)

                        filename1=name+".csv"
                        encFile1.to_csv(os.path.join(self.savePath, filename1), encoding='utf-8')
        if v1.get() == 2:
            for i in range(len(names1)):
                if box_vars1[i].get() == 1:
                    for index, row in encFile1.iterrows():
                        pres=names1[i]
                        encFile1[pres].values[index] = public_key.encrypt((encFile1[pres].values[index]).encode("utf8"),
                                                                      32)

                        filename1=name+".csv"
                        encFile1.to_csv(os.path.join(self.savePath, filename1), encoding='utf-8')

        PublicKeyFile=("PublicKey_"+name)
        f = open(os.path.join(self.savePath, PublicKeyFile), "w")
        f.write((key.publickey().exportKey('PEM')).decode("utf8"))
        f.close()
        PrivateKeyFile=("PrivateKey_"+name)
        f = open(os.path.join(self.savePath, PrivateKeyFile), "w")
        f.write((key.exportKey('PEM')).decode("utf8"))
        f.close()

        def loop_function():
            k = 0
            while k <= self.MAX:
               
                self.progress_var.set(k)
                k += 1
                time.sleep(0.02)
                self.update_idletasks()
        loop_function()
        self.finish.config(state="normal")
        #dtypeCount = [encFile.iloc[:, i].apply(type).value_counts() for i in range(encFile.shape[1])]
        #print(dtypeCount)

    def filepathLoc1(self):
        self.savePath = filedialog.askdirectory()
        self.selected1()
        self.changeLocation1()
    def changeLocation1(self):
        self.Location.config(text=filepath1)

    def selected1(self):
        self.start.config(state="normal")

    def __init__(self,parent,controller):
        self.MAX = 100
        self.savePath=""
        self.progress_var = DoubleVar()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Encrypting file now...", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("EncryptPage"))
        self.start=tk.Button(self, text="Start",state=DISABLED,command=self.start_now)
        selectSave=tk.Button(self, text="Select Save location",command=self.filepathLoc1)
        self.Location = Label(self, text="", bd=1, bg='white', width=50, height=2, relief=SUNKEN, anchor=W)
        self.Location.pack(padx=10,pady=10,side="left")
        selectSave.pack(padx=10,pady=10,side="left")
        Label(self, text="Save file as: ").pack(side="left")
        self.e1=Entry(self)
        self.e1.pack(side="left")
        self.finish = tk.Button(self, text="Finish", state=DISABLED, command=self.quit)

        self.start.pack(fill=X,padx=10,pady=10,side="bottom")
        self.progressbar = ttk.Progressbar(self, variable=self.progress_var, maximum=self.MAX)

        self.progressbar.pack(fill=X, padx=10, pady=10, side="bottom")
        self.finish.pack(fill=X, padx=10, pady=10, side="bottom")
        button.pack()
        global var1


global e2
names2=[]
var2 = []
filepath2=""
box_num2 = 0
boxes2 = []
box_vars2 = []
keyFile=""

class DecryptPage(tk.Frame):
    def openFile(self):
        global encFile2
        global keyFile
        keyFile = filedialog.askopenfilename()
        self.labelLocation3.config(text=keyFile)
        self.changeLocation2()
        global v2
        if (v2.get() == 1):
            encFile2 = pandas.read_csv(self.filepath2,
                                      dtype={'branch': str, 'account': str, 'daily_balance': str, 'date': str,
                                             'branch_cluster': str, 'pmjdy': str, 'date1': str, 'date2': str,
                                             'description': str, 'debit_credit': str, 'amount': str,
                                             'debit_credit1': str, 'balance': str, 'journal_no': str,
                                             'updated_acct': str, 'max_date': str, 'max_date_demon': str,
                                             'cif_s1': str, 'name_s1': str, 'open_date_s1': str,
                                             'mobile_s1': str, 's1_info': str, 'cif_s2': str,
                                             'open_date_s2': str, 'dateofbirth_s2': str,
                                             'mobno_account_s2': str, 'atm_account_s2': str,
                                             'sms_account_s2': str, 'mobno_cif_s2': str, 'female_cif_s2': str,
                                             'male_cif_s2': str, 's2_info': str, 'savings_type': str,
                                             'acct_holder_age': str, 'working_age': str,
                                             'female_working': str, 'female_non_working': str,
                                             'male_working': str, 'male_non_working': str,
                                             'zero_balance': str, 'year': str, 'month': str, 'day': str,
                                             'first_trans': str, 'first_trans_date': str,
                                             'last_trans_date': str, 'open_date': str, 'ATM': str,
                                             'ATM_others': str, 'POS': str, 'CSH': str, 'CSH_WDL': str,
                                             'CSH_DEP': str, 'CHQ': str, 'thru_CHQ': str, 'OWN_CHQ_DP': str,
                                             'WDL_TX_CHQ': str, 'CSH_WDL_Chq': str, 'CHQ_DEP': str,
                                             'CHQ_others': str, 'DEP_TX': str, 'SCHOLARSHIP': str,
                                             'WDL_TX': str, 'NEFT': str, 'IMPS': str, 'RTGS': str,
                                             'CREDIT_BULK': str, 'PMJJBY': str, 'PMJJBY_renewal': str,
                                             'PMJJBY_first': str, 'PMSBY': str, 'PMSBY_renewal': str,
                                             'TFR_DB': str, 'TFR_CR': str, 'NPCI': str, 'LPG_SUBSIDY': str,
                                             'LPG_availed': str, 'LPG_amount': str, 'AADHAAR': str,
                                             'FTRNO': str, 'SUPPLECS': str, 'SGT': str, 'VLR': str,
                                             'PENSION': str, 'SGT_PEN': str, 'FTRNO_availed': str,
                                             'SUPPLECS_availed': str, 'SGT_availed': str, 'VLR_availed': str,
                                             'PENSION_availed': str, 'FTRNO_amount': str,
                                             'SUPPLECS_amount': str, 'SGT_amount': str, 'VLR_amount': str,
                                             'PENSION_amount': str, 'POS_amount': str, 'SGT_PEN_amount': str,
                                             'LIC': str, 'TDS': str, 'SAL': str, 'CR_INT_CR': str,
                                             'CR_INT_DB': str, 'REPIN8': str, 'AMC_ATM': str, 'CHARGES': str,
                                             'SMS': str, 'INTR_CTY_CHRG': str, 'COMBINE1': str,
                                             'COMBINE': str, 'DB_TRF_ALL': str, 'CR_TRF_ALL': str,
                                             'ACTIVE_WDL': str, 'ACTIVE_DEP': str, 'ALL_CHARGES': str,
                                             'CRDT_BLK': str, 'total_remain': str, 'CRDT_BLK_Others': str,
                                             'INTEREST': str, 'unexplained': str, 'govt_init_trans': str,
                                             'govt_assisted_acc': str, 'SAL_account': str, 'SAL_savings': str,
                                             'SAL_pmjdy': str, 'trans_identified': str, 'age': str,
                                             'age_quarter': str, 'age_month': str,
                                             'quarter_govt_assisted': str, 'month_govt_assisted': str,
                                             'MOBILE_linked': str, 'SMS_charged_account': str,
                                             'AADHAAR_linked': str})

        elif (v2.get() == 2):
            encFile2 = pandas.read_csv(self.filepath2,
                                      dtype={'accno': str, 'account_type': str, 'CIF': str, 'customer_name': str,
                                             'limit': str, 'interest_rate': str, 'theo_balance': str,
                                             'outstanding': str, 'irregularity': str, 'emi_due': str,
                                             'emi_paid': str, 'emi_overdue': str, 'new_irac': str,
                                             'arrear_cond': str, 'currency': str, 'acct_maintain_branch': str,
                                             'emi_installment_amt': str, 'unrealised_int': str, 'accru_int': str,
                                             'file_date	': str, 'branch': str, 'sanction_date': str,
                                             'irregularity_date': str, 'emi_installment': str})
        self.Ecolumns2.config(state="normal")
        global names2
        names2 = list(encFile2.columns.values)


    def create_window(self):
        t2 = tk.Toplevel(self)
        global canvas2
        canvas2 = tk.Canvas(t2)
        canvas2.pack(side=tk.LEFT)
        scrollbar2 = tk.Scrollbar(t2, command=canvas2.yview)
        scrollbar2.pack(side=tk.LEFT, fill='y')

        canvas2.configure(yscrollcommand=scrollbar2.set)

        frame2 = tk.Frame(canvas2)
        canvas2.create_window((0, 0), window=frame2, anchor='nw')
        canvas2.bind('<Configure>', self.on_configure2)

        t2.wm_title("Choose the columns...")
        frame2.grid_columnconfigure(0, weight=1)
        butt2 = Button(frame2, text="Confirm", command=t2.destroy)
        global names2
        butt2.pack()
        global var2
        global box_num2
        global boxes2
        global box_vars2
        global box_num2
        for name in names2:
            box_vars2.append(tk.IntVar())
            boxes2.append(tk.Checkbutton(frame2, text=name, variable=box_vars2[box_num2]))
            box_vars2[box_num2].set(0)
            boxes2[box_num2].pack()
            box_num2 += 1

    def on_configure2(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas2.configure(scrollregion=canvas2.bbox('all'))

    def changeLocation2(self):
        self.labelLocation2.config(text=self.filepath2)

    def changeStatus2(self, Text):
        status.config(text=Text)

    def selected2(self):
        fileButton2.config(state="normal")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label2 = tk.Label(self, text="DECRYPTION", font=controller.title_font)
        label2.pack(side="top", fill="x", pady=10)
        backButton2= tk.Button(self, text="Back",
                               command=lambda: controller.show_frame("MainPage"))
        self.filepath2=""
        labelFile2 = Label(self, text="File")
        global fileButton2
        fileButton2 = tk.Button(self, text="Browse", command=self.openFile3, state=DISABLED)
        self.labelLocation2 = Label(self, text="", bd=1, bg='white', width=50, height=2, relief=SUNKEN, anchor=W)
        global names2
        global okButton2
        okButton2 = Button(self, text="Continue", command=lambda: controller.show_frame("PerfDecryp"))
        global v2
        v2 = IntVar()
        Radiobutton(self, text="Loan Data", variable=v2, value=2, command=self.selected2).pack(anchor=W)
        Radiobutton(self, text="Savings Data", variable=v2, value=1, command=self.selected2).pack(anchor=W)
        self.changeStatus2("Please choose the type of file, and add file location...")
        labelFile2.pack(padx=5, pady=10, side=LEFT)
        self.labelLocation2.pack(padx=5, pady=10, side=LEFT)
        fileButton2.pack(padx=5, pady=10, side=LEFT)
        self.labelLocation3 = Label(self, text="Choose key file", bd=1, bg='white', width=50, height=2, relief=SUNKEN,
                               anchor=W)
        self.labelLocation3.pack(padx=5, pady=10, side=LEFT)
        self.fileButton3 = tk.Button(self, text="Browse", command=self.openFile, state=DISABLED)
        self.fileButton3.pack(padx=5, pady=10, side=LEFT)

        backButton2.pack(fill="none", expand=True)

        self.Ecolumns2 = Button(self, state=DISABLED, text="Choose the columns to decrypt",
                               command=self.create_window)
        self.Ecolumns2.pack()
        okButton2.pack()

    def openFile3(self):
        self.filepath2 = filedialog.askopenfilename()
        self.labelLocation2.config(text=self.filepath2)
        self.fileButton3.config(state="normal")

from base64 import b64decode


class PerfDecryp(tk.Frame):
    def start_now2(self):
        name = self.e2.get()

        global names2
        global var2
        global box_num2
        global boxes2
        global box_vars2
        global box_num2
        global v2
        global encFile2
        global var2
        global keyFile

        key=open(keyFile,"r")
        private=key.read()
        privateKey=RSA.importKey(private)
        if v2.get() == 1:
            for i in range(len(names2)):

                if box_vars2[i].get() == 1:
                    for index, row in encFile2.iterrows():
                        pres = names2[i]
                        encFile2[pres].values[index] = privateKey.decrypt((encFile2[pres].values[index]))
        if v2.get() == 2:
            for i in range(len(names2)):

                if box_vars2[i].get() == 1:
                    for index, row in encFile2.iterrows():
                        pres = names2[i]
                        encFile2[pres].values[index] = privateKey.decrypt((encFile2[pres].values[index]))

        filename2 = name + ".csv"
        encFile2.to_csv(os.path.join(self.savePath, filename2), encoding='utf-8')

        def loop_function():
            k = 0
            while k <= self.MAX:
                self.progress_var.set(k)
                k += 1
                time.sleep(0.02)
                self.update_idletasks()

        loop_function()
        self.finish2.config(state="normal")
        # dtypeCount = [encFile.iloc[:, i].apply(type).value_counts() for i in range(encFile.shape[1])]
        # print(dtypeCount)

    def filepathLoc2(self):
        self.savePath = filedialog.askdirectory()
        self.selected2()
        self.Location2.config(text=self.savePath)

    def selected2(self):
        self.start2.config(state="normal")

    def __init__(self, parent, controller):
        self.MAX = 100
        self.savePath = ""
        self.progress_var = DoubleVar()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label2 = tk.Label(self, text="Decrypting file now...", font=controller.title_font)
        label2.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("DecryptPage"))
        self.start2 = tk.Button(self, text="Start", state=DISABLED, command=self.start_now2)
        selectSave2 = tk.Button(self, text="Select Save location", command=self.filepathLoc2)
        self.Location2 = Label(self, text="", bd=1, bg='white', width=50, height=2, relief=SUNKEN, anchor=W)
        self.Location2.pack(padx=10, pady=10, side="left")
        selectSave2.pack(padx=10, pady=10, side="left")
        Label(self, text="Save file as: ").pack(side="left")
        self.e2 = Entry(self)
        self.e2.pack(side="left")
        self.finish2 = tk.Button(self, text="Finish", state=DISABLED, command=self.quit)

        self.start2.pack(fill=X, padx=10, pady=10, side="bottom")
        self.progressbar2 = ttk.Progressbar(self, variable=self.progress_var, maximum=self.MAX)

        self.progressbar2.pack(fill=X, padx=10, pady=10, side="bottom")
        self.finish2.pack(fill=X, padx=10, pady=10, side="bottom")
        button2.pack()
        global var2

class VerticalScrolledFrame(Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y", expand="false")
        self.canvas = tk.Canvas(self,
                                bd=0,
                                height=350,
                                highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand="true")
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.interior, anchor="nw")

        self.bind('<Configure>', self.set_scrollregion)

    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
if __name__ == "__main__":
    app = CrypDex()
    app.mainloop()