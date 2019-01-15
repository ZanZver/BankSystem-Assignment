#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:07:27 2018

@author: ZanZver
"""

#add comments (description)
#add photos of treewiew
#exceptions if users add num insted of str
#add TEST users to database
#add when you sucessfully do transaction, do pop up!

import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime, calendar
import operator
import uuid
import hashlib

LARGE_FONT = ('Verdana', 12)

accounts_list = []
admins_list = []

GlIdUser = ''

conn = sqlite3.connect('BankData.db')
c = conn.cursor()

rbStat = 'nill'

class BankingSystem(tk.Tk):
    def __init__ (self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,'My program')   
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        
        #adding 'frames to the switch
        for F in (LoginPage, BookAppointment, AdminPage, BankPage, ErrorPage, UserPageAccSelect, Acc1Page, Acc2Page, Acc3Page, WelcomePage, BankBasePage,BankPageSearch, AdminPageBase, AdminPageSearch, InvestmentsPage, InterestRatePage, UpdateSucessAdmin, UpdateSucessUser, ErrorPageAdmin, ErrorPageUser, ManadgeLoadns, ErrorUpdatingLoans, UpdateSucessLoan, BankBalance, UpdateSucessUserFromAdmin, ErrorPageUserFromAdmin, AdminManadgeAppointments,UpdateSucessWithdraw,ErrorUpdateWithdraw,UpdateSucessDeposit,ErrorUpdateDeposit,TransferSucessInternal,MoveToUser,ManagmentReport):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
            
        self.show_frame(WelcomePage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        #size switch
        sframe = str(frame)
        if(sframe == '.!frame.!loginpage'):
            self.geometry('200x150')
            self.minsize(200,150)
        elif(sframe == '.!frame.!userpageaccselect'):
            self.state('zoomed')
        elif(sframe == '.!frame.!bookappointment'):
            self.state('zoomed')
        elif(sframe == '.!frame.!acc1page'):
            self.state('zoomed')
        elif(sframe == '.!frame.!acc2page'):
            self.state('zoomed')
        elif(sframe == '.!frame.!acc3page'):
            self.state('zoomed')
        elif(sframe == '.!frame.!adminpage'):
            self.state('zoomed')
        elif(sframe == '.!frame.!bankpage'):
            self.state('zoomed')
        elif(sframe == '.!frame.!bankbasepage'):
            self.state('zoomed')
        elif(sframe == '.!frame.!errorpage'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucessuser'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucessudmin'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucessudminfromadmin'):
            self.state('normal') 
        elif(sframe == '.!frame.!errorpageadminfromadmin'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucessloan'):
            self.state('normal')
        elif(sframe == '.!frame.!transfersucessinternal'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucesswithdraw'):
            self.state('normal')
        elif(sframe == '.!frame.!errorupdatewithdraw'):
            self.state('normal')
        elif(sframe == '.!frame.!updatesucessdeposit'):
            self.state('normal')
        elif(sframe == '.!frame.!errorupdatedeposit'):
            self.state('normal')
        elif(sframe == '.!frame.!errorpageuser'):
            self.state('normal')
        elif(sframe == '.!frame.!errorpageadmin'):
            self.state('normal')
        elif(sframe == '.!frame.!errorupdatingloans'):
            self.state('normal')
        elif(sframe == '.!frame.!welcomepage'):
            self.geometry('150x100')
            self.minsize(150,100) 
        elif(sframe == '.!frame.!bankpagesearch'):
            self.state('zoomed')
        elif(sframe == '.!frame.!adminpagesearch'):
            self.state('zoomed')
        elif(sframe == '.!frame.!adminpagebase'):
            self.state('zoomed') 
        elif(sframe == '.!frame.!adminmanadgeappointments'):
            self.state('zoomed') 
        elif(sframe == '.!frame.!investmentspage'):
            self.state('zoomed')
        elif(sframe == '.!frame.!interestratepage'):
            self.state('zoomed')   
        elif(sframe == '.!frame.!managmentreport'):
            self.state('zoomed')   
        elif(sframe == '.!frame.!manadgeloadns'):
            self.state('zoomed') 
        elif(sframe == '.!frame.!bankbalance'):
            self.state('zoomed')  
        elif(sframe == '.!frame.!movetouser'):
            self.state('zoomed')          
        else:
            self.state('normal')            
           
#frame pages        
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
            
        self.labelUsername = tk.Label(self, text = 'Enter your username: ')
        self.labelPassword = tk.Label(self, text = 'Enter your password: ')
        
        self.entryUsername = tk.Entry(self)
        self.entryPassword = tk.Entry(self, show = '*')
        
        self.controller.bind('<Return>', self.moveToLogin)
        
        self.buttonLogin = tk.Button(self, text = 'Login', command = self.login)
        
        self.buttonAppointment = tk.Button(self, text = 'Book an appintment', command = lambda: controller.show_frame(BookAppointment))
        
        self.labelUsername.pack()
        self.entryUsername.pack()
        self.labelPassword.pack()
        self.entryPassword.pack()
        self.buttonLogin.pack()
        self.buttonAppointment.pack()
        
    def moveToLogin(self, event):
         b = tk.Button(self, text = '',command = self.login)
         b.invoke()

    def login(self):
        username = str(self.entryUsername.get())
        password = str(self.entryPassword.get())
        
        self.entryUsername.delete(0, 'end')
        self.entryPassword.delete(0, 'end')
        global GlIdUser
         
        Valid, status, idUser = data.read_from_db(username, password)
        if(Valid == True and status == 'admin'):
            GlIdUser = idUser
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(AdminPageBase))
            b.invoke()
        elif(Valid == True and status == 'bank'):
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(BankBasePage))
            b.invoke()
        elif(Valid == True and status == 'user'):
            GlIdUser = idUser
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UserPageAccSelect))
            b.invoke()
        else:
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorPage))
            b.invoke()
            
class BookAppointment(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.OPTIONS = [
        "Loc1",
        "Loc2",
        "Loc3"
        ] 
        
        self.OPTIONSyear = [
        "2018",
        "2019",
        "2020"
        ] 
        
        self.OPTIONSmonth = [    
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'
        ] 
         
        self.OPTIONSday = [
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            '24',
            '25',
            '26',
            '27',
            '28',
            '29',
            '30',
            '31'
        ] 
        
        self.variable = tk.StringVar(self)
        self.variable.set(self.OPTIONS[0])
        
        self.variableyear = tk.StringVar(self)
        self.variableyear.set(self.OPTIONSyear[0])
        
        self.variablemonth = tk.StringVar(self)
        self.variablemonth.set(self.OPTIONSmonth[0])
        
        self.variableday = tk.StringVar(self)
        self.variableday.set(self.OPTIONSday[0])
        
        self.label = tk.Label(self, text = 'book an appointment')
        
        self.labelUserID = tk.Label(self, text = 'Enter your ID (if you have it):')
        self.labelUserName = tk.Label(self, text = 'Enter user name:')
        self.labelUserSurname = tk.Label(self, text = 'Enter user surname:')
        self.labelAppointmentAddress = tk.Label(self, text = 'Enter address of appointment:')
        self.w = tk.OptionMenu(self, self.variable, *self.OPTIONS)
        
        self.labelAppointmentDate = tk.Label(self, text = 'Enter date of appointment:')
        self.wyear = tk.OptionMenu(self, self.variableyear, *self.OPTIONSyear)
        self.wmonth = tk.OptionMenu(self, self.variablemonth, *self.OPTIONSmonth)
        self.wday = tk.OptionMenu(self, self.variableday, *self.OPTIONSday)
        self.labelAppointmentComment= tk.Label(self, text = 'Add coment if you want:')
        
        self.enterUserID = tk.Entry(self)
        self.entryUserName = tk.Entry(self)
        self.entryUserSurname = tk.Entry(self)
        self.entryAppointmentComment = tk.Entry(self)
        
        self.entryUserName.delete(0, 'end')
        
        self.buttonBook = ttk.Button(self, text = 'Book a appointment', command = self.saveToDb)
        self.buttonBack = ttk.Button(self, text = 'Go back', command = self.clearAndMove)
         
        self.label.pack()
        self.labelUserID.pack()
        self.enterUserID.pack()
        self.labelUserName.pack()
        self.entryUserName.pack()
        self.labelUserSurname.pack()
        self.entryUserSurname.pack()
        self.labelAppointmentAddress.pack()
        self.w.pack()
        self.labelAppointmentDate.pack()
        self.wyear.pack()
        self.wmonth.pack()
        self.wday.pack()
        
        self.labelAppointmentComment.pack()
        self.entryAppointmentComment.pack()
        
        self.buttonBook.pack()
        self.buttonBack.pack()
       
    def clearAndMove(self):
        self.variable.set(self.OPTIONS[0])
        self.variableyear.set(self.OPTIONSyear[0])
        self.variablemonth.set(self.OPTIONSmonth[0])
        self.variableday.set(self.OPTIONSday[0])
        self.enterUserID.delete(0, 'end')        
        self.entryUserName.delete(0, 'end')
        self.entryUserSurname.delete(0, 'end')      
        self.entryAppointmentComment.delete(0, 'end')
        b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(LoginPage))
        b.invoke()
        
    def saveToDb(self):
        a = (calendar.monthrange(int(str(self.variableyear.get())),int(str(self.variablemonth.get())))[1])

        if(a < int(self.variableday.get())):
            print('error')
            self.variableday.set(a)
            
        Sep = '.'
        AllDates = (str(self.variableday.get())), (str(self.variablemonth.get())),((str(self.variableyear.get()))) 

        GotUserID = str(self.enterUserID.get())
        GotUserName = str(self.entryUserName.get())
        GotUserSurname = str(self.entryUserSurname.get())
        GotPlace = self.variable.get()
        GotDate = Sep.join(AllDates)
        GotAppointmentComment = str(self.entryAppointmentComment.get())
        
        data.insertIntoAppointments(GotUserID, GotUserName, GotUserSurname,GotPlace, GotDate, GotAppointmentComment)
        
        self.variable.set(self.OPTIONS[0])
        self.variableyear.set(self.OPTIONSyear[0])
        self.variablemonth.set(self.OPTIONSmonth[0])
        self.variableday.set(self.OPTIONSday[0])
        self.enterUserID.delete(0, 'end')        
        self.entryUserName.delete(0, 'end')
        self.entryUserSurname.delete(0, 'end')      
        self.entryAppointmentComment.delete(0, 'end')
            
            
class UserPageAccSelect(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = 'nil'
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Data:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        
        self.frm2 = tk.Frame(self)
        self.frm2.grid(row=1, column=1, sticky='nw')
        
        
        self.rowconfigure(1, weight=1)
        
        self.btnShowAllAccounts = tk.Button(self.frm2,text ='Show all accounts', command = self.ShowAll)
        self.btnCA = tk.Button(self.frm2,text ='Checking account', command = self.ShowCA)
        self.btnSA = tk.Button(self.frm2,text ='Savings account', command = self.ShowSA)
        self.btnCD = tk.Button(self.frm2,text ='Certificate of Deposit (CD)', command = self.ShowCD)
        self.btnMMA = tk.Button(self.frm2,text ='Money market account', command = self.ShowMMA)
        self.btnIRA = tk.Button(self.frm2,text ='Individual Retirement Accounts (IRAs)', command = self.ShowIRA)
        
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        
        self.OPTIONSDeposit = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ]  
        self.variableDeposit = tk.StringVar(self)
        self.variableDeposit.set(self.OPTIONSDeposit[0]) 
        self.lblAccTypeDeposit = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountDeposit = tk.Label(self, text = 'Enter amount to deposit:') 
        self.wDeposit = tk.OptionMenu(self, self.variableDeposit, *self.OPTIONSDeposit)
        self.EntryEnteredAmountDeposit = tk.Entry(self) 
        self.btnConfirmDeposit = tk.Button(self,text ='Confirm')
        
        self.OPTIONSWithdraw = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableWithdraw = tk.StringVar(self)
        self.variableWithdraw.set(self.OPTIONSWithdraw[0])
        self.lblAccTypeWithdraw = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountWithdraw = tk.Label(self, text = 'Enter amount to withdraw:')
        self.wWithdraw = tk.OptionMenu(self, self.variableWithdraw, *self.OPTIONSWithdraw)
        self.EntryEnteredAmountWithdraw = tk.Entry(self)
        self.btnConfirmWithdraw = tk.Button(self,text ='Confirm')
        
        self.btnYourAcc = tk.Button(self.frm2,text ='Transfer between your accounts', command = self.TransferToYourAcc)
        self.btnOtherAcc = tk.Button(self.frm2,text ='Transfer to other acc', command = self.TransferToOtherAcc)
        self.btnHowItWorks = tk.Button(self.frm2,text ='How does transfer works', command = self.TransferInstructions)
        
        self.OPTIONSInterest = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
                
        self.variableInterest = tk.StringVar(self)
        self.variableInterest.set(self.OPTIONSInterest[0])     
        self.lblAccTypeInterest = tk.Label(self, text = 'Chose acc type:')
        self.lblAmmountInterest = tk.Label(self, text = 'Interest on the acc:')     
        self.wInterest = tk.OptionMenu(self, self.variableInterest, *self.OPTIONSInterest)
        self.lblShownInterest = tk.Label(self, text = 'Interest is going to be shown here')     
        self.btnGetInterest = tk.Button(self,text ='Get interest')
        self.btnHowItWorksInterest = tk.Button(self,text ='How does interest work')
        
        self.btnAllInvestments = tk.Button(self.frm2,text ='All investments', command = self.AllInvestments)
        self.btnYourInvestments = tk.Button(self.frm2,text ='Your investments', command = self.CustomerInvestments)
        self.btnBuyInvestments = tk.Button(self.frm2,text ='Buy investments', command = self.BuyInvestments)
        self.btnSellInvestments = tk.Button(self.frm2,text ='Sell investments', command = self.SellInvestmetns)
        self.btnInvestmetnNews = tk.Button(self.frm2,text ='Investment news', command = self.InvestmentNews)

        self.btnYourLoans = tk.Button(self.frm2,text ='Your loans', command = self.CustomerLoans)
        self.btnRequestLoans = tk.Button(self.frm2,text ='Request loans', command = self.RequestLoans)
        self.btnAboutLoans = tk.Button(self.frm2,text ='About loans', command = self.AboutLoans)
        
        self.btnEditUserProfile = tk.Button(self.frm2,text ='Edit user profile', command = self.EditUserProfile)
        self.btnRecentActivity = tk.Button(self.frm2,text ='See recent activity', command = self.RecentActivity)
        self.btnRemoveUser = tk.Button(self.frm2,text ='Remove user', command = self.RemoveUser)
        self.btnRemoveAccountType = tk.Button(self.frm2,text ='Remove account type', command = self.RemoveAccountType)
        
        self.OPTIONSTransfer = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableTransfer = tk.StringVar(self)
        self.variableTransfer.set(self.OPTIONSTransfer[0])      
        self.lblSelectFirstAcc = tk.Label(self, text = 'Transfer from')
        self.lblAccTypeTransferFirst = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountToTransferFirst = tk.Label(self, text = 'Enter amount to withdraw:')
        self.lblSelectAccSecond = tk.Label(self, text = 'Transfer to')
        self.lblSelectSecondAcc = tk.Label(self, text = 'Enter acccount to transfer to:')
        self.lblAccTypeTransferSecond = tk.Label(self, text = 'Chose acc type:')        
        self.wTransferOne = tk.OptionMenu(self, self.variableTransfer, *self.OPTIONSTransfer)
        self.EntryEnteredAmountTransfer = tk.Entry(self)
        self.wTransferTwo = tk.OptionMenu(self, self.variableTransfer, *self.OPTIONSTransfer)        
        self.btnConfirmTransfer = tk.Button(self,text ='Confirm')  
        
        self.OPTIONSTransferToOther = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ]     
        self.variableTransferToOther = tk.StringVar(self)
        self.variableTransferToOther .set(self.OPTIONSTransferToOther[0])    
        self.lblSelectFirstAcc = tk.Label(self, text = 'Transfer from')
        self.lblAccTypeTransferFirst = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountToTransferFirst = tk.Label(self, text = 'Enter amount to withdraw:')
        self.lblSelectSecondAcc = tk.Label(self, text = 'Enter acccount to transfer to')
        self.lblAccTypeTransferName = tk.Label(self, text = 'User name')
        self.lblAccTypeTransferSurname = tk.Label(self, text = 'User surname')
        self.lblAccTypeTransferAccType= tk.Label(self, text = 'Select account type:')    
        self.wTransferOne = tk.OptionMenu(self, self.variableTransferToOther, *self.OPTIONSTransferToOther)
        self.EntryEnteredAmountTransfer = tk.Entry(self)
        self.EntryEnteredAmountTransferName = tk.Entry(self)
        self.EntryEnteredAmountTransferSurname = tk.Entry(self)    
        self.btnConfirmTransfer = tk.Button(self,text ='Confirm')  
        
        self.OPTIONSTransferToOther = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.OPTIONSTransferFromOther = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.variableTransferToOtherFrom = tk.StringVar(self)
        self.variableTransferToOtherFrom.set(self.OPTIONSTransferToOther[0])
        self.variableTransferFromOtherFrom = tk.StringVar(self)
        self.variableTransferFromOtherFrom.set(self.OPTIONSTransferFromOther[0])
        self.lblTransferFromOther = tk.Label(self, text = 'Transfer from')
        self.lblChoseAccToTransferFrom = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountToTransferToOther = tk.Label(self, text = 'Enter amount to transfer:')
        self.lblSelectSecondAccOther = tk.Label(self, text = 'Enter acccount to transfer to')
        self.lblAccTypeTransferNameOther = tk.Label(self, text = 'User name')
        self.lblAccTypeTransferSurnameOther = tk.Label(self, text = 'User surname')
        self.lblAccTypeTransferAccTypeOther = tk.Label(self, text = 'Select account type:')
        self.wTransferFromOther = tk.OptionMenu(self, self.variableTransferToOther, *self.OPTIONSTransferToOther)
        self.wTransferToOther = tk.OptionMenu(self, self.variableTransferFromOtherFrom, *self.OPTIONSTransferFromOther)
        self.EntryEnteredAmountTransferToOther = tk.Entry(self)
        self.EntryEnteredAmountTransferNameOther = tk.Entry(self)
        self.EntryEnteredAmountTransferSurnameOther = tk.Entry(self)
        self.btnConfirmTransferToOther = tk.Button(self,text ='Confirm', command = self.ConfirmTransferOtherAcc)  
        
        
        self.OPTIONSBuyInvestment = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.OPTIONSChoseAcc = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ]   
        self.variableBuyInvestment = tk.StringVar(self)
        self.variableBuyInvestment .set(self.OPTIONSBuyInvestment[0])  
        self.variableChoseAcc = tk.StringVar(self)
        self.variableChoseAcc .set(self.OPTIONSChoseAcc[0])  
        self.lblBuyInvestments = tk.Label(self, text = 'Buy investment')
        self.lblChoseInvestmentType = tk.Label(self, text = 'Chose investment type:')
        self.lblEntertAmountToBuy = tk.Label(self, text = 'Enter amount to buy:')
        self.lblChoseAccountToBuyFrom = tk.Label(self, text = 'Enter acccount to buy from')
        self.lblChoseAccountType= tk.Label(self, text = 'Select account type:')  
        self.wBuyInvestment = tk.OptionMenu(self, self.variableBuyInvestment, *self.OPTIONSBuyInvestment)
        self.wChoseAcc = tk.OptionMenu(self, self.variableChoseAcc, *self.OPTIONSChoseAcc)
        self.EntryEnteredAmountToBuy = tk.Entry(self)  
        self.btnConfirmTransfer = tk.Button(self,text ='Confirm')  
        
        self.OPTIONSSellInvestment = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.OPTIONSChoseAccSell = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.variableSellInvestment = tk.StringVar(self)
        self.variableSellInvestment .set(self.OPTIONSSellInvestment[0])
        self.variableChoseAcc = tk.StringVar(self)
        self.variableChoseAcc .set(self.OPTIONSChoseAccSell[0])
        self.lblSellInvestments = tk.Label(self, text = 'Sell investment')
        self.lblChoseInvestmentTypeSell = tk.Label(self, text = 'Chose investment type:')
        self.lblEntertAmountToSell = tk.Label(self, text = 'Enter amount to sell:')
        self.lblChoseAccountToSellFrom = tk.Label(self, text = 'Enter acccount to sell to')
        self.lblChoseAccountTypeSell = tk.Label(self, text = 'Select account type:')
        self.wSellInvestment = tk.OptionMenu(self, self.variableSellInvestment, *self.OPTIONSSellInvestment)
        self.wChoseAccSell = tk.OptionMenu(self, self.variableChoseAcc, *self.OPTIONSChoseAccSell)
        self.EntryEnteredAmountSell = tk.Entry(self)
        self.btnConfirmSell = tk.Button(self,text ='Confirm')  
        
        self.OPTIONSRequest = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.variableRequest = tk.StringVar(self)
        self.variableRequest .set(self.OPTIONSRequest[0])
        self.lblRequestLoan = tk.Label(self, text = 'Requset loan')
        self.lblChoseInvestmentRequest = tk.Label(self, text = 'Chose account type:')
        self.lblEntertAmountRequest = tk.Label(self, text = 'Enter amount:')
        self.lblEnterCommentRequest = tk.Label(self, text = 'Enter commenet:')
        self.wRequestAcc = tk.OptionMenu(self, self.variableRequest, *self.OPTIONSRequest)
        self.EntryEnteredAmountRequest = tk.Entry(self)
        self.EntryEnteredCommentRequest = tk.Entry(self)
        self.btnConfirmRequestLoan = tk.Button(self,text ='Confirm')  
        
        self.lbACcountSettings = tk.Label(self, text = 'Account settings')
        self.lbChangeUsername = tk.Label(self, text = 'Change username')
        self.lbChangeMiddlename = tk.Label(self, text = 'Change middlename')
        self.lbChangeSurname = tk.Label(self, text = 'Change surname')
        self.lbChangePassword = tk.Label(self, text = 'Change password')
        self.lbChangeHouseNumber = tk.Label(self, text = 'Change house number')
        self.lbChangeStreet = tk.Label(self, text = 'Change street')
        self.lbChangeCity= tk.Label(self, text = 'Change city')
        self.lbChangePostCode = tk.Label(self, text = 'Change post code')
        self.EntryChangeUsername = tk.Entry(self)
        self.EntryChangeMiddlename = tk.Entry(self)
        self.EntryChangeSurname = tk.Entry(self)
        self.EntryChangePassword = tk.Entry(self)
        self.EntryChangeHouseNumber = tk.Entry(self)
        self.EntryChangeStreet = tk.Entry(self)
        self.EntryChangeCity = tk.Entry(self)
        self.EntryChangePostCode = tk.Entry(self)
        self.btnConfirmRequest = tk.Button(self,text ='Confirm')  
        
        self.lbDeliteUser = tk.Label(self, text = 'Delite account')
        self.lbDeliteUserUsername = tk.Label(self, text = 'Enter your username')
        self.lbDeliteUserSurname = tk.Label(self, text = 'Enter your surname')
        self.lbDeliteUserPassword = tk.Label(self, text = 'Enter your password')
        self.EntryDeliteUserUsername = tk.Entry(self)
        self.EntryDeliteUserSurname = tk.Entry(self)
        self.EntryDeliteUserPassword = tk.Entry(self)
        self.btnConfirmDelite = tk.Button(self,text ='Confirm')  

        self.OPTIONSRemove = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        self.variableRemove = tk.StringVar(self)
        self.variableRemove .set(self.OPTIONSRemove[0])
        self.lbDeliteUser = tk.Label(self, text = 'Delite account type')
        self.lbDeliteUserType = tk.Label(self, text = 'Chose account type')
        self.lbDeliteUserUsername = tk.Label(self, text = 'Enter your username')
        self.lbDeliteUserSurname = tk.Label(self, text = 'Enter your surname')
        self.lbDeliteUserPassword = tk.Label(self, text = 'Enter your password')
        self.EntryDeliteUserUsername = tk.Entry(self)
        self.EntryDeliteUserSurname = tk.Entry(self)
        self.EntryDeliteUserPassword = tk.Entry(self)
        self.wRequestAcc = tk.OptionMenu(self, self.variableRemove, *self.OPTIONSRemove)
        self.btnConfirmDelite = tk.Button(self,text ='Confirm')          
        
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
        
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.btnSelectAccType = tk.Button(self.frm,text ='Show accounts', command = self.SelectAccType)
        self.btnSelectAccType.pack(expand=False, fill='x')
        
        self.btnDepositMoney = tk.Button(self.frm,text ='Deposit money', command = self.DepositMoney)
        self.btnDepositMoney.pack(expand=False, fill='x')
        
        self.btnWithdrawMoney = tk.Button(self.frm,text ='Withdraw money', command = self.WithdrawMoney)
        self.btnWithdrawMoney.pack(expand=False, fill='x')
        
        self.btnTransferMoney = tk.Button(self.frm,text ='Transfer money', command = self.TransferMoney)
        self.btnTransferMoney.pack(expand=False, fill='x')
        
        self.btnInterest = tk.Button(self.frm,text ='Interest', command = self.Interest)
        self.btnInterest.pack(expand=False, fill='x')
    
        self.btnInvestments = tk.Button(self.frm,text ='Investments', command = self.Investments)
        self.btnInvestments.pack(expand=False, fill='x')
        
        self.btnLoans = tk.Button(self.frm,text ='Loans', command = self.Loans)
        self.btnLoans.pack(expand=False, fill='x')
        
        self.btnAccSettings = tk.Button(self.frm,text ='Account settings', command = self.AccSettings)
        self.btnAccSettings.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(LoginPage))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nw')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nw')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nw')
        self.tv.grid_forget()          

        
    def SelectAccType(self):  
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
        
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.btnShowAllAccounts = tk.Button(self.frm2,text ='Show all accounts', command = self.ShowAll)
        self.btnShowAllAccounts.pack(expand=False, fill='x') 
        
        self.btnCA = tk.Button(self.frm2,text ='Checking account', command = self.ShowCA)
        self.btnCA.pack(expand=False, fill='x')
        
        self.btnSA = tk.Button(self.frm2,text ='Savings account', command = self.ShowSA)
        self.btnSA.pack(expand=False, fill='x')
        
        self.btnCD = tk.Button(self.frm2,text ='Certificate of Deposit (CD)', command = self.ShowCD)
        self.btnCD.pack(expand=False, fill='x')
        
        self.btnMMA = tk.Button(self.frm2,text ='Money market account', command = self.ShowMMA)
        self.btnMMA.pack(expand=False, fill='x')
        
        self.btnIRA = tk.Button(self.frm2,text ='Individual Retirement Accounts (IRAs)', command = self.ShowIRA)
        self.btnIRA.pack(expand=False, fill='x')
    
    def ShowAll(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')
        
        self.tv.grid(row=1, column=2, sticky='nsw')
        self.tv['columns'] = ( 'balance', 'dateOfChange')
        self.tv.heading("#0", text='Account type')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('balance', text='Balance')
        self.tv.column('balance', anchor='center', width=100)
        self.tv.heading('dateOfChange', text='Date of change')
        self.tv.column('dateOfChange', anchor='center', width=100)
        self.treeview = self.tv
        
        GotId = str(GlIdUser)
        c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}'".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
            self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))        
        
    def ShowCA(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        self.tv.grid_forget()
        for i in self.tv.get_children():
                self.tv.delete(i)
                
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')
        
        GotId = str(GlIdUser)
        ca = ''
        c.execute("SELECT CA FROM AccType Where userId is '{}'".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ca = operator.itemgetter(0)(row)
            
        if(ca.lower() == 'true'):   
            self.tv.grid(row=1, column=2, sticky='nsw')
            self.tv['columns'] = ( 'balance', 'dateOfChange')
            self.tv.heading("#0", text='Account type')
            self.tv.column("#0", anchor='center', width=50)
            self.tv.heading('balance', text='Balance')
            self.tv.column('balance', anchor='center', width=100)
            self.tv.heading('dateOfChange', text='Date of change')
            self.tv.column('dateOfChange', anchor='center', width=100)
            self.treeview = self.tv
            
            GotId = str(GlIdUser)
            c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}' and accType is 'CA'".format(GotId))
            lis = []
            for row in c.fetchall():
                lis.append(row)        
                accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
                self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))
        else:
            print('no acc, want to create one')
        
    def ShowSA(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        self.tv.grid_forget()
        for i in self.tv.get_children():
                self.tv.delete(i)
                
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')
        
        GotId = str(GlIdUser)
        sa = ''
        c.execute("SELECT sa FROM AccType Where userId is '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            sa = operator.itemgetter(0)(row)
            
        if(sa.lower() == 'true'):   
            self.tv.grid(row=1, column=2, sticky='nsw')
            self.tv['columns'] = ( 'balance', 'dateOfChange')
            self.tv.heading("#0", text='Account type')
            self.tv.column("#0", anchor='center', width=50)
            self.tv.heading('balance', text='Balance')
            self.tv.column('balance', anchor='center', width=100)
            self.tv.heading('dateOfChange', text='Date of change')
            self.tv.column('dateOfChange', anchor='center', width=100)
            self.treeview = self.tv
            
            GotId = str(GlIdUser)
            c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}' and accType is 'SA'".format(GotId))
            lis = []
            for row in c.fetchall():
                lis.append(row)        
                accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
                self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))
        else:
            print('no acc, want to create one')
        
    def ShowCD(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        self.tv.grid_forget()
        for i in self.tv.get_children():
                self.tv.delete(i)

        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')

        GotId = str(GlIdUser)
        cd = ''
        c.execute("SELECT sa FROM AccType Where userId is '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            cd = operator.itemgetter(0)(row)
            
        if(cd.lower() == 'true'):   
            self.tv.grid(row=1, column=2, sticky='nsw')
            self.tv['columns'] = ( 'balance', 'dateOfChange')
            self.tv.heading("#0", text='Account type')
            self.tv.column("#0", anchor='center', width=50)
            self.tv.heading('balance', text='Balance')
            self.tv.column('balance', anchor='center', width=100)
            self.tv.heading('dateOfChange', text='Date of change')
            self.tv.column('dateOfChange', anchor='center', width=100)
            self.treeview = self.tv
            
            GotId = str(GlIdUser)
            c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}' and accType is 'COD'".format(GotId))
            lis = []
            for row in c.fetchall():
                lis.append(row)        
                accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
                self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))
        else:
            print('no acc, want to create one')
        
    def ShowMMA(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget()        
        self.tv.grid_forget()
        for i in self.tv.get_children():
                self.tv.delete(i)
                
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')               
                
        GotId = str(GlIdUser)
        mma = ''
        c.execute("SELECT sa FROM AccType Where userId is '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            mma = operator.itemgetter(0)(row)
            
        if(mma.lower() == 'true'):   
            self.tv.grid(row=1, column=2, sticky='nsw')
            self.tv['columns'] = ( 'balance', 'dateOfChange')
            self.tv.heading("#0", text='Account type')
            self.tv.column("#0", anchor='center', width=50)
            self.tv.heading('balance', text='Balance')
            self.tv.column('balance', anchor='center', width=100)
            self.tv.heading('dateOfChange', text='Date of change')
            self.tv.column('dateOfChange', anchor='center', width=100)
            self.treeview = self.tv
            
            GotId = str(GlIdUser)
            c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}' and accType is 'MMA'".format(GotId))
            lis = []
            for row in c.fetchall():
                lis.append(row)        
                accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
                self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))
        else:
            print('no acc, want to create one')
        
    def ShowIRA(self):
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        self.tv.grid_forget()
        for i in self.tv.get_children():
                self.tv.delete(i)
                
        self.btnOpenAcc = tk.Button(self,text ='Open acc')
        self.btnOpenAcc.grid(row=1, column=3, sticky = 'nw')
        self.btnCloseAcc = tk.Button(self,text ='Close acc')
        self.btnCloseAcc.grid(row=1, column=4, sticky = 'nw')
                
        GotId = str(GlIdUser)
        ira = ''
        c.execute("SELECT sa FROM AccType Where userId is '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ira = operator.itemgetter(0)(row)
            
        if(ira.lower() == 'true'):   
            self.tv.grid(row=1, column=2, sticky='nsw')
            self.tv['columns'] = ( 'balance', 'dateOfChange')
            self.tv.heading("#0", text='Account type')
            self.tv.column("#0", anchor='center', width=50)
            self.tv.heading('balance', text='Balance')
            self.tv.column('balance', anchor='center', width=100)
            self.tv.heading('dateOfChange', text='Date of change')
            self.tv.column('dateOfChange', anchor='center', width=100)
            self.treeview = self.tv
            
            GotId = str(GlIdUser)
            c.execute("SELECT accType, balance, dateOfChange FROM Balance Where userId is '{}' and accType is 'IRA'".format(GotId))
            lis = []
            for row in c.fetchall():
                lis.append(row)        
                accType, balance, dateOfChange = operator.itemgetter(0,1,2)(row)
                self.treeview.insert('', 'end',text=accType,  values = (balance, dateOfChange))
        else:
            print('no acc, want to create one')
        
    def DepositMoney(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
                
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
 
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.OPTIONSDeposit = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableDeposit = tk.StringVar(self)
        self.variableDeposit.set(self.OPTIONSDeposit[0])
        
        self.lblAccTypeDeposit = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountDeposit = tk.Label(self, text = 'Enter amount to deposit:')
        
        self.wDeposit = tk.OptionMenu(self, self.variableDeposit, *self.OPTIONSDeposit)
        self.EntryEnteredAmountDeposit = tk.Entry(self)
        
        self.btnConfirmDeposit = tk.Button(self,text ='Confirm', command = self.ConfirmDeposit)
        
        self.lblAccTypeDeposit.place(x = 120, y = 25)
        self.wDeposit.place(x = 300, y = 25)
        self.lblEnterAmmountDeposit.place(x = 120, y = 60)
        self.EntryEnteredAmountDeposit.place(x = 300, y = 60)
        self.btnConfirmDeposit.place(x = 130, y = 95)
    
    def ConfirmDeposit(self):
        GotId = str(GlIdUser)
        GotAmmount = str(self.EntryEnteredAmountDeposit.get())
        GotAccount = str(self.variableDeposit.get())
        
        if (GotAccount == 'Checking account'):
            GotAccount = 'CA'
        elif (GotAccount == 'Savings account'):
            GotAccount = 'SA'
        elif (GotAccount == 'Certificate of Deposit (CD)'):
            GotAccount = 'COD'
        elif (GotAccount == 'Money market account'):
            GotAccount = 'MMA'
        elif (GotAccount == 'Individual Retirement Accounts (IRAs)'):
            GotAccount = 'IRA'
        else:
            GotAccount = 'Error'
        
        ac = ''
        c.execute("SELECT {} FROM AccType Where userId is '{}' ".format(GotAccount,GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ac = operator.itemgetter(0)(row)
            
        if(ac.lower() == 'true'):   
            data.UpdateDepositAmmount(GotId, GotAmmount, GotAccount)

            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessDeposit))
            b.invoke()

        else:
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorUpdateDeposit))
            b.invoke()
        
    def WithdrawMoney(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
 
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   

        self.OPTIONSWithdraw = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableWithdraw = tk.StringVar(self)
        self.variableWithdraw.set(self.OPTIONSWithdraw[0])
        
        self.lblAccTypeWithdraw = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountWithdraw = tk.Label(self, text = 'Enter amount to withdraw:')
        
        self.wWithdraw = tk.OptionMenu(self, self.variableWithdraw, *self.OPTIONSWithdraw)
        self.EntryEnteredAmountWithdraw = tk.Entry(self)
        
        self.btnConfirmWithdraw = tk.Button(self,text ='Confirm', command = self.ConfirmWithdraw)
        
        self.lblAccTypeWithdraw.place(x = 120, y = 25)
        self.wWithdraw.place(x = 300, y = 25)
        self.lblEnterAmmountWithdraw.place(x = 120, y = 60)
        self.EntryEnteredAmountWithdraw.place(x = 300, y = 60)
        self.btnConfirmWithdraw.place(x = 130, y = 95)
        
    def ConfirmWithdraw(self):
        GotId = str(GlIdUser)
        GotAmmount = str(self.EntryEnteredAmountWithdraw.get())
        GotAccount = str(self.variableWithdraw.get())
        
        if (GotAccount == 'Checking account'):
            GotAccount = 'CA'
        elif (GotAccount == 'Savings account'):
            GotAccount = 'SA'
        elif (GotAccount == 'Certificate of Deposit (CD)'):
            GotAccount = 'COD'
        elif (GotAccount == 'Money market account'):
            GotAccount = 'MMA'
        elif (GotAccount == 'Individual Retirement Accounts (IRAs)'):
            GotAccount = 'IRA'
        else:
            GotAccount = 'Error'
        
        ac = ''
        c.execute("SELECT {} FROM AccType Where userId is '{}' ".format(GotAccount,GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ac = operator.itemgetter(0)(row)
            
        if(ac.lower() == 'true'):   
            data.UpdateWithdrawAmmount(GotId, GotAmmount, GotAccount)
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessWithdraw))
            b.invoke()

        else:
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorUpdateWithdraw))
            b.invoke()
        
    def TransferMoney(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
 
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()

        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.btnYourAcc = tk.Button(self.frm2,text ='Transfer between your accounts', command = self.TransferToYourAcc)
        self.btnYourAcc.pack(expand=False, fill='x')
        
        self.btnOtherAcc = tk.Button(self.frm2,text ='Transfer to other acc', command = self.TransferToOtherAcc)
        self.btnOtherAcc.pack(expand=False, fill='x')
        
        self.btnHowItWorks = tk.Button(self.frm2,text ='How does transfer works', command = self.TransferInstructions)
        self.btnHowItWorks.pack(expand=False, fill='x')
        
    def Interest(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
 
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.OPTIONSInterest = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
                
        self.variableInterest = tk.StringVar(self)
        self.variableInterest.set(self.OPTIONSInterest[0])
        
        self.lblAccTypeInterest = tk.Label(self, text = 'Chose acc type:')
        self.lblAmmountInterest = tk.Label(self, text = 'Interest on the acc:')
        
        self.wInterest = tk.OptionMenu(self, self.variableInterest, *self.OPTIONSInterest)
        self.lblShownInterest = tk.Label(self, text = 'Interest is going to be shown here')
        
        self.btnGetInterest = tk.Button(self,text ='Get interest')
        self.btnHowItWorksInterest = tk.Button(self,text ='How does interest work')
        
        self.lblAccTypeInterest.place(x = 120, y = 25)
        self.wInterest.place(x = 300, y = 25)
        self.lblAmmountInterest.place(x = 120, y = 60)
        self.lblShownInterest.place(x = 300, y = 60)
        self.btnGetInterest.place(x = 130, y = 95)
        self.btnHowItWorksInterest.place(x = 215, y = 95)
        
    def Investments(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()

        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()

        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget() 
        
        self.btnAllInvestments = tk.Button(self.frm2,text ='All investments', command = self.AllInvestments)
        self.btnAllInvestments.pack(expand=False, fill='x')
        
        self.btnYourInvestments = tk.Button(self.frm2,text ='Your investments', command = self.CustomerInvestments)
        self.btnYourInvestments.pack(expand=False, fill='x')
        
        self.btnBuyInvestments = tk.Button(self.frm2,text ='Buy investments', command = self.BuyInvestments)
        self.btnBuyInvestments.pack(expand=False, fill='x')
        
        self.btnSellInvestments = tk.Button(self.frm2,text ='Sell investments', command = self.SellInvestmetns)
        self.btnSellInvestments.pack(expand=False, fill='x')
        
        self.btnInvestmetnNews = tk.Button(self.frm2,text ='Investment news', command = self.InvestmentNews)
        self.btnInvestmetnNews.pack(expand=False, fill='x')
        
    def Loans(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
 
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
 
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.btnYourLoans = tk.Button(self.frm2,text ='Your loans', command = self.CustomerLoans)
        self.btnYourLoans.pack(expand=False, fill='x')
        
        self.btnRequestLoans = tk.Button(self.frm2,text ='Request loans', command = self.RequestLoans)
        self.btnRequestLoans.pack(expand=False, fill='x')
        
        self.btnAboutLoans = tk.Button(self.frm2,text ='About loans', command = self.AboutLoans)
        self.btnAboutLoans.pack(expand=False, fill='x')
        
    def AccSettings(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.btnYourAcc.pack_forget()
        self.btnOtherAcc.pack_forget()
        self.btnHowItWorks.pack_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
  
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()
        
        self.btnEditUserProfile = tk.Button(self.frm2,text ='Edit user profile', command = self.EditUserProfile)
        self.btnEditUserProfile.pack(expand=False, fill='x')
        
        self.btnRecentActivity = tk.Button(self.frm2,text ='See recent activity', command = self.RecentActivity)
        self.btnRecentActivity.pack(expand=False, fill='x')
        
        self.btnRemoveUser = tk.Button(self.frm2,text ='Remove user', command = self.RemoveUser)
        self.btnRemoveUser.pack(expand=False, fill='x')
        
        self.btnRemoveAccountType = tk.Button(self.frm2,text ='Remove account type', command = self.RemoveAccountType)
        self.btnRemoveAccountType.pack(expand=False, fill='x')
 
    def TransferToYourAcc(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
   
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget()   
        
        self.OPTIONSTransfer = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableTransferAccFrom = tk.StringVar(self)
        self.variableTransferAccFrom.set(self.OPTIONSTransfer[0])
        
        self.variableTransferAccTo = tk.StringVar(self)
        self.variableTransferAccTo.set(self.OPTIONSTransfer[0])
        
        self.lblSelectFirstAcc = tk.Label(self, text = 'Transfer from')
        self.lblAccTypeTransferFirst = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountToTransferFirst = tk.Label(self, text = 'Enter amount to transfer:')
        self.lblSelectAccSecond = tk.Label(self, text = 'Transfer to')
        self.lblSelectSecondAcc = tk.Label(self, text = 'Enter acccount to transfer to:')
        self.lblAccTypeTransferSecond = tk.Label(self, text = 'Chose acc type:')
        
        self.wTransferOne = tk.OptionMenu(self, self.variableTransferAccFrom, *self.OPTIONSTransfer)
        self.EntryEnteredAmountTransfer = tk.Entry(self)
        self.wTransferTwo = tk.OptionMenu(self, self.variableTransferAccTo, *self.OPTIONSTransfer)
        
        self.btnConfirmTransfer = tk.Button(self,text ='Confirm', command = self.ConfirmTransferYourAcc)  
        
        self.lblSelectFirstAcc.place(x = 340, y = 25)
        self.lblAccTypeTransferFirst.place(x = 340, y = 60)
        self.wTransferOne.place(x = 540, y = 60)
        self.lblSelectAccSecond.place(x = 340, y = 95)
        self.lblEnterAmmountToTransferFirst.place(x = 340, y = 130)
        self.EntryEnteredAmountTransfer.place(x = 540, y = 130)
        self.lblSelectSecondAcc.place(x = 340, y = 165)
        self.wTransferTwo.place(x = 540, y = 165)
        self.btnConfirmTransfer.place(x = 340, y = 200)
        
    def ConfirmTransferYourAcc(self):
        GotId = str(GlIdUser)
        GotAccFrom = str(self.variableTransferAccFrom.get())
        GotAmount = str(self.EntryEnteredAmountTransfer.get())
        GotAccTo = str(self.variableTransferAccTo.get())
        
        print(GotId,GotAccFrom,GotAmount,GotAccTo)
        
        if (GotAccFrom == "Checking account"):
            GotAccFrom = 'CA'
        if (GotAccTo == "Checking account"):
            GotAccTo = 'CA'
        
        if (GotAccFrom == "Savings account"):
            GotAccFrom = 'SA'
        if (GotAccTo == "Savings account"):
            GotAccTo = 'SA'
        
        if (GotAccFrom == 'Certificate of Deposit (CD)'):
            GotAccFrom = 'COD'
        if (GotAccTo == 'Certificate of Deposit (CD)'):
            GotAccTo = 'COD'
        
        if (GotAccFrom == 'Money market account'):
            GotAccFrom = 'MMA'
        if (GotAccTo =='Money market account'):
            GotAccTo = 'MMA'
        
        if (GotAccFrom == 'Individual Retirement Accounts (IRAs)'):
            GotAccFrom = 'IRA'
        if (GotAccTo == 'Individual Retirement Accounts (IRAs)'):
            GotAccTo = 'IRA'
        
        data.UpdateDepositAmmount(GotId, GotAmount, GotAccTo)
        
        data.UpdateWithdrawAmmount(GotId, GotAmount, GotAccFrom)
        
        
        b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(TransferSucessInternal))
        b.invoke()
        
    def TransferToOtherAcc(self):
        self.btnShowAllAccounts.pack_forget() 
        self.btnCA.pack_forget() 
        self.btnSA.pack_forget() 
        self.btnCD.pack_forget() 
        self.btnMMA.pack_forget() 
        self.btnIRA.pack_forget() 
        
        self.btnOpenAcc.grid_forget() 
        self.btnCloseAcc.grid_forget() 
        
        self.lblAccTypeDeposit.place_forget()
        self.wDeposit.place_forget()
        self.lblEnterAmmountDeposit.place_forget()
        self.EntryEnteredAmountDeposit.place_forget()
        self.btnConfirmDeposit.place_forget()
        
        self.lblAccTypeWithdraw.place_forget()
        self.wWithdraw.place_forget()
        self.lblEnterAmmountWithdraw.place_forget()
        self.EntryEnteredAmountWithdraw.place_forget()
        self.btnConfirmWithdraw.place_forget()
        
        self.lblAccTypeInterest.place_forget()
        self.wInterest.place_forget()
        self.lblAmmountInterest.place_forget()
        self.lblShownInterest.place_forget()
        self.btnGetInterest.place_forget()
        self.btnHowItWorksInterest.place_forget()
        
        self.btnAllInvestments.pack_forget() 
        self.btnYourInvestments.pack_forget() 
        self.btnBuyInvestments.pack_forget() 
        self.btnSellInvestments.pack_forget() 
        self.btnInvestmetnNews.pack_forget() 

        self.btnYourLoans.pack_forget() 
        self.btnRequestLoans.pack_forget() 
        self.btnAboutLoans.pack_forget() 

        self.btnEditUserProfile.pack_forget()
        self.btnRecentActivity.pack_forget()
        self.btnRemoveUser.pack_forget()
        self.btnRemoveAccountType.pack_forget()
        
        self.lblSelectFirstAcc.place_forget()
        self.lblAccTypeTransferFirst.place_forget()
        self.wTransferOne.place_forget()
        self.lblSelectAccSecond.place_forget()
        self.lblEnterAmmountToTransferFirst.place_forget()
        self.EntryEnteredAmountTransfer.place_forget()
        self.lblSelectSecondAcc.place_forget()
        self.wTransferTwo.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblTransferFromOther.place_forget()
        self.lblChoseAccToTransferFrom.place_forget()
        self.wTransferFromOther.place_forget()
        self.lblEnterAmmountToTransferToOther.place_forget()
        self.EntryEnteredAmountTransferToOther.place_forget()
        self.lblSelectSecondAccOther.place_forget()
        self.lblAccTypeTransferNameOther.place_forget()
        self.EntryEnteredAmountTransferNameOther.place_forget()
        self.lblAccTypeTransferSurnameOther.place_forget()
        self.EntryEnteredAmountTransferSurnameOther.place_forget()
        self.lblAccTypeTransferAccTypeOther.place_forget()
        self.wTransferToOther.place_forget()
        self.btnConfirmTransferToOther.place_forget()
        
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()

        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.tv.grid_forget() 
        
        self.OPTIONSTransferToOther = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.OPTIONSTransferFromOther = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableTransferToOtherFrom = tk.StringVar(self)
        self.variableTransferToOtherFrom.set(self.OPTIONSTransferToOther[0])
        
        self.variableTransferFromOtherFrom = tk.StringVar(self)
        self.variableTransferFromOtherFrom.set(self.OPTIONSTransferFromOther[0])
        
        self.lblTransferFromOther = tk.Label(self, text = 'Transfer from')
        self.lblChoseAccToTransferFrom = tk.Label(self, text = 'Chose acc type:')
        self.lblEnterAmmountToTransferToOther = tk.Label(self, text = 'Enter amount to transfer:')
        self.lblSelectSecondAccOther = tk.Label(self, text = 'Enter acccount to transfer to')
        self.lblAccTypeTransferNameOther = tk.Label(self, text = 'User name')
        self.lblAccTypeTransferSurnameOther = tk.Label(self, text = 'User surname')
        self.lblAccTypeTransferAccTypeOther = tk.Label(self, text = 'Select account type:')
        
        self.wTransferFromOther = tk.OptionMenu(self, self.variableTransferToOtherFrom, *self.OPTIONSTransferToOther)
        self.wTransferToOther = tk.OptionMenu(self, self.variableTransferFromOtherFrom, *self.OPTIONSTransferFromOther)
        self.EntryEnteredAmountTransferToOther = tk.Entry(self)
        self.EntryEnteredAmountTransferNameOther = tk.Entry(self)
        self.EntryEnteredAmountTransferSurnameOther = tk.Entry(self)
        
        self.btnConfirmTransferToOther = tk.Button(self,text ='Confirm', command = self.ConfirmTransferOtherAcc)  
        
        self.lblTransferFromOther.place(x = 340, y = 25)
        self.lblChoseAccToTransferFrom.place(x = 340, y = 60)
        self.wTransferFromOther.place(x = 540, y = 60)
        self.lblEnterAmmountToTransferToOther.place(x = 340, y = 95)
        self.EntryEnteredAmountTransferToOther.place(x = 540, y = 95)
        self.lblSelectSecondAccOther.place(x = 340, y = 130)
        self.lblAccTypeTransferNameOther.place(x = 340, y = 165)
        self.EntryEnteredAmountTransferNameOther.place(x = 540, y = 165)
        self.lblAccTypeTransferSurnameOther.place(x = 340, y = 200)
        self.EntryEnteredAmountTransferSurnameOther.place(x = 540, y = 200)
        self.lblAccTypeTransferAccTypeOther.place(x = 340, y = 235)
        self.wTransferToOther.place(x = 540, y = 235)
        self.btnConfirmTransferToOther.place(x = 340, y = 270)
        
    def ConfirmTransferOtherAcc(self):
        GotId = str(GlIdUser)
        GotAccFrom = str(self.variableTransferToOtherFrom.get())
        GotAmount = str(self.EntryEnteredAmountTransferToOther.get())
        GotNameTo = str(self.EntryEnteredAmountTransferNameOther.get())
        GotSurnameTo = str(self.EntryEnteredAmountTransferSurnameOther.get())
        GotAccTo = str(self.variableTransferFromOtherFrom.get())
        
        if (GotAccFrom == "Checking account"):
            GotAccFrom = 'CA'
        if (GotAccTo == "Checking account"):
            GotAccTo = 'CA'
        
        if (GotAccFrom == "Savings account"):
            GotAccFrom = 'SA'
        if (GotAccTo == "Savings account"):
            GotAccTo = 'SA'
        
        if (GotAccFrom == 'Certificate of Deposit (CD)'):
            GotAccFrom = 'COD'
        if (GotAccTo == 'Certificate of Deposit (CD)'):
            GotAccTo = 'COD'
        
        if (GotAccFrom == 'Money market account'):
            GotAccFrom = 'MMA'
        if (GotAccTo =='Money market account'):
            GotAccTo = 'MMA'
        
        if (GotAccFrom == 'Individual Retirement Accounts (IRAs)'):
            GotAccFrom = 'IRA'
        if (GotAccTo == 'Individual Retirement Accounts (IRAs)'):
            GotAccTo = 'IRA'
            
        data.UpdateDepositAmmountToOther(GotNameTo,GotSurnameTo, GotAmount, GotAccTo)
        data.UpdateWithdrawAmmount(GotId, GotAmount, GotAccFrom) 

        
    def TransferInstructions(self):
        print('transfer instructions')
        
    def AllInvestments(self):
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.tv.grid_forget() 
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=2, sticky='nsw')
        self.tv['columns'] = ( 'InvestmentName', 'InvestmentValue','InvestmentDateChanged','InvestmentDateCreated','InvestmentDateRemoved')
        self.tv.heading("#0", text='Investment ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('InvestmentName', text='Investment name')
        self.tv.column('InvestmentName', anchor='center', width=100)
        self.tv.heading('InvestmentValue', text='Investment value')
        self.tv.column('InvestmentValue', anchor='center', width=100)
        self.tv.heading('InvestmentDateChanged', text='Investments last change')
        self.tv.column('InvestmentDateChanged', anchor='center', width=100)
        self.tv.heading('InvestmentDateCreated', text='When was investment created')
        self.tv.column('InvestmentDateCreated', anchor='center', width=100)
        self.tv.heading('InvestmentDateRemoved', text='When was investment removed')
        self.tv.column('InvestmentDateRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Investments")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InvestmentId, InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved = operator.itemgetter(0,1,2,3,4,5)(row)
            self.treeview.insert('', 'end',text=InvestmentId,  values=(InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved))


    def CustomerInvestments(self):
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        
        self.tv.grid_forget() 
        GotId = str(GlIdUser)
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=2, sticky='nsw')
        self.tv['columns'] = ( 'Quantity')
        self.tv.heading("#0", text='Investment name')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.column('Quantity', anchor='center', width=100)
        self.tv.heading('Quantity', text='Quantity')
        self.treeview = self.tv
        c.execute("Select Investments.InvestmentName, UserInvestments.Quantity  From Investments,UserInvestments  WHERE Investments.InvestmentsId like UserInvestments.InvestmentID AND UserInvestments.UserID like {} ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InvestmentName, InvestmentQuantity = operator.itemgetter(0,1)(row)
            self.treeview.insert('', 'end',text=InvestmentName,  values=(InvestmentQuantity))
        
    def BuyInvestments(self):
        self.lblSellInvestments.place_forget()
        self.lblChoseInvestmentTypeSell.place_forget()
        self.wSellInvestment.place_forget()
        self.lblEntertAmountToSell.place_forget()
        self.EntryEnteredAmountSell.place_forget()
        self.lblChoseAccountToSellFrom.place_forget()
        self.lblChoseAccountTypeSell.place_forget()
        self.wChoseAccSell.place_forget()
        self.btnConfirmSell.place_forget()
        self.tv.grid_forget() 
        
        self.OPTIONSBuyInvestment = [] 
        
        self.OPTIONSChoseAcc = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        c.execute("Select InvestmentName From Investments")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            self.OPTIONSBuyInvestment.append(row)
        
        self.variableBuyInvestment = tk.StringVar(self)
        self.variableBuyInvestment .set(self.OPTIONSBuyInvestment[0])
        
        self.variableChoseAcc = tk.StringVar(self)
        self.variableChoseAcc .set(self.OPTIONSChoseAcc[0])
        
        self.lblBuyInvestments = tk.Label(self, text = 'Buy investment')
        self.lblChoseInvestmentType = tk.Label(self, text = 'Chose investment type:')
        self.lblEntertAmountToBuy = tk.Label(self, text = 'Enter amount to buy:')
        self.lblChoseAccountToBuyFrom = tk.Label(self, text = 'Enter acccount to buy from')
        self.lblChoseAccountType= tk.Label(self, text = 'Select account type:')
        
        self.wBuyInvestment = tk.OptionMenu(self, self.variableBuyInvestment, *self.OPTIONSBuyInvestment)
        self.wChoseAcc = tk.OptionMenu(self, self.variableChoseAcc, *self.OPTIONSChoseAcc)
        self.EntryEnteredAmountToBuy = tk.Entry(self)
        
        self.btnConfirmTransfer = tk.Button(self,text ='Confirm', command = self.ConfirmBuy)  
        
        self.lblBuyInvestments.place(x = 250, y = 25)
        self.lblChoseInvestmentType.place(x = 250, y = 60)
        self.wBuyInvestment.place(x = 430, y = 60)
        self.lblEntertAmountToBuy.place(x = 250, y = 95)
        self.EntryEnteredAmountToBuy.place(x = 430, y = 95)
        self.lblChoseAccountToBuyFrom.place(x = 250, y = 130)
        self.lblChoseAccountType.place(x = 250, y = 165)
        self.wChoseAcc.place(x = 430, y = 165)
        self.btnConfirmTransfer.place(x = 260, y = 200)
        
    def ConfirmBuy(self):
        GotId = str(GlIdUser)
        GotInvestment = str(self.variableBuyInvestment.get())
        GotAmount = str(self.EntryEnteredAmountToBuy.get())
        GotAccount = str(self.variableChoseAcc.get())
        
        GotInvestment = GotInvestment.replace("(", "")
        GotInvestment = GotInvestment.replace(")", "")
        GotInvestment = GotInvestment.replace(",", "")
        GotInvestment = GotInvestment.replace("'", "")
        
        if (GotAccount == "Checking account"):
            GotAccount = 'CA'
        
        if (GotAccount == "Savings account"):
            GotAccount = 'SA'
        
        if (GotAccount == 'Certificate of Deposit (CD)'):
            GotAccount = 'COD'
        
        if (GotAccount == 'Money market account'):
            GotAccount = 'MMA'
        
        if (GotAccount == 'Individual Retirement Accounts (IRAs)'):
            GotAccount = 'IRA'
        
        data.InsertIntoUserInvestments(GotId,GotInvestment, GotAmount, GotAccount, 'buy') 
        
    def SellInvestmetns(self):
        self.lblBuyInvestments.place_forget()
        self.lblChoseInvestmentType.place_forget()
        self.wBuyInvestment.place_forget()
        self.lblEntertAmountToBuy.place_forget()
        self.EntryEnteredAmountToBuy.place_forget()
        self.lblChoseAccountToBuyFrom.place_forget()
        self.lblChoseAccountType.place_forget()
        self.wChoseAcc.place_forget()
        self.btnConfirmTransfer.place_forget()
        self.tv.grid_forget() 

        self.OPTIONSSellInvestment = [
        ] 
        
        self.OPTIONSChoseAccSell = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        c.execute("SELECT Investments.InvestmentName FROM UserInvestments, Investments WHERE UserInvestments.InvestmentID like Investments.InvestmentsId and UserInvestments.UserID is {}".format(GlIdUser))
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            self.OPTIONSSellInvestment.append(row)
        
        self.variableSellInvestment = tk.StringVar(self)
        self.variableSellInvestment .set(self.OPTIONSSellInvestment[0])
        
        self.variableChoseAcc = tk.StringVar(self)
        self.variableChoseAcc .set(self.OPTIONSChoseAccSell[0])
        
        self.lblSellInvestments = tk.Label(self, text = 'Sell investment')
        self.lblChoseInvestmentTypeSell = tk.Label(self, text = 'Chose investment type:')
        self.lblEntertAmountToSell = tk.Label(self, text = 'Enter amount to sell:')
        self.lblChoseAccountToSellFrom = tk.Label(self, text = 'Enter acccount to sell to')
        self.lblChoseAccountTypeSell = tk.Label(self, text = 'Select account type:')
        
        self.wSellInvestment = tk.OptionMenu(self, self.variableSellInvestment, *self.OPTIONSSellInvestment)
        self.wChoseAccSell = tk.OptionMenu(self, self.variableChoseAcc, *self.OPTIONSChoseAccSell)
        self.EntryEnteredAmountSell = tk.Entry(self)
        
        self.btnConfirmSell = tk.Button(self,text ='Confirm', command = self.ConfirmSell)  
        
        self.lblSellInvestments.place(x = 250, y = 25)
        self.lblChoseInvestmentTypeSell.place(x = 250, y = 60)
        self.wSellInvestment.place(x = 430, y = 60)
        self.lblEntertAmountToSell.place(x = 250, y = 95)
        self.EntryEnteredAmountSell.place(x = 430, y = 95)
        self.lblChoseAccountToSellFrom.place(x = 250, y = 130)
        self.lblChoseAccountTypeSell.place(x = 250, y = 165)
        self.wChoseAccSell.place(x = 430, y = 165)
        self.btnConfirmSell.place(x = 260, y = 200)
        
    def ConfirmSell(self):
        GotId = str(GlIdUser)
        GotInvestment = str(self.variableSellInvestment.get())
        GotAmount = str(self.EntryEnteredAmountSell.get())
        GotAccount = str(self.variableChoseAcc.get())
        
        GotInvestment = GotInvestment.replace("(", "")
        GotInvestment = GotInvestment.replace(")", "")
        GotInvestment = GotInvestment.replace(",", "")
        GotInvestment = GotInvestment.replace("'", "")
        
        if (GotAccount == "Checking account"):
            GotAccount = 'CA'
        
        if (GotAccount == "Savings account"):
            GotAccount = 'SA'
        
        if (GotAccount == 'Certificate of Deposit (CD)'):
            GotAccount = 'COD'
        
        if (GotAccount == 'Money market account'):
            GotAccount = 'MMA'
        
        if (GotAccount == 'Individual Retirement Accounts (IRAs)'):
            GotAccount = 'IRA'
        
        print(GotId,GotInvestment, GotAmount, GotAccount)
        data.InsertIntoUserInvestments(GotId,GotInvestment, GotAmount, GotAccount,'sell') 
        
    def InvestmentNews(self):
        print('sell availible investments')
            
    def CustomerLoans(self):
        self.lblRequestLoan.place_forget()
        self.lblChoseInvestmentRequest.place_forget()
        self.wRequestAcc.place_forget()
        self.lblEntertAmountRequest.place_forget()
        self.EntryEnteredAmountRequest.place_forget()
        self.lblEnterCommentRequest.place_forget()
        self.EntryEnteredCommentRequest.place_forget()
        self.btnConfirmRequestLoan.place_forget()
        
        self.tv.grid_forget() 
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        GotId = str(GlIdUser)
        
        self.tv.grid(row=1, column=2, sticky='nsw')
        self.tv['columns'] = ( 'LoanStatus', 'LoanAmount','LoanMonthlyPlan','LoanComments','LoanChanged','LoanAdded','LoanRemoved')
        self.tv.heading("#0", text='Loan ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('LoanStatus', text='Loan status')
        self.tv.column('LoanStatus', anchor='center', width=100)
        self.tv.heading('LoanAmount', text='Loan amount')
        self.tv.column('LoanAmount', anchor='center', width=100)
        self.tv.heading('LoanMonthlyPlan', text='Loan monthly plan')
        self.tv.column('LoanMonthlyPlan', anchor='center', width=100)
        self.tv.heading('LoanComments', text='Loan comments')
        self.tv.column('LoanComments', anchor='center', width=100)
        self.tv.heading('LoanChanged', text='Last change of loan')
        self.tv.column('LoanChanged', anchor='center', width=100)
        self.tv.heading('LoanAdded', text='When was loan added')
        self.tv.column('LoanAdded', anchor='center', width=100)
        self.tv.heading('LoanRemoved', text='When was loan removed')
        self.tv.column('LoanRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT LoansId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComents, LoanChanged, LoanAdded, LoanRemoved From Loans Where UserLoanId is {}".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            loanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged,LoanAdded,LoanRemoved = operator.itemgetter(0,1,2,3,4,5,6,7)(row)
            self.treeview.insert('', 'end',text=loanId,  values=(LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged,LoanAdded,LoanRemoved))

        
    def RequestLoans(self):
        self.tv.grid_forget() 
        self.OPTIONSRequest = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableRequest = tk.StringVar(self)
        self.variableRequest .set(self.OPTIONSRequest[0])
        
        self.lblRequestLoan = tk.Label(self, text = 'Requset loan')
        self.lblChoseInvestmentRequest = tk.Label(self, text = 'Chose account type:')
        self.lblEntertAmountRequest = tk.Label(self, text = 'Enter amount:')
        self.lblEnterCommentRequest = tk.Label(self, text = 'Enter commenet:')
        
        self.wRequestAcc = tk.OptionMenu(self, self.variableRequest, *self.OPTIONSRequest)
        self.EntryEnteredAmountRequest = tk.Entry(self)
        self.EntryEnteredCommentRequest = tk.Entry(self)
        
        self.btnConfirmRequestLoan = tk.Button(self,text ='Confirm', command = self.ConfirmLoanRequest)  
        
        self.lblRequestLoan.place(x = 250, y = 25)
        self.lblChoseInvestmentRequest.place(x = 250, y = 60)
        self.wRequestAcc.place(x = 430, y = 60)
        self.lblEntertAmountRequest.place(x = 250, y = 95)
        self.EntryEnteredAmountRequest.place(x = 430, y = 95)
        self.lblEnterCommentRequest.place(x = 250, y = 130)
        self.EntryEnteredCommentRequest.place(x = 430, y = 130)
        self.btnConfirmRequestLoan.place(x = 260, y = 165)
        
    def ConfirmLoanRequest(self):
        GotId = str(GlIdUser)
        GotAccType = str(self.variableRequest.get())
        GotAmount = str(self.EntryEnteredAmountRequest.get())
        GotComment = str(self.EntryEnteredCommentRequest.get())
        
        if (GotAccType == "Checking account"):
            GotAccType = 'CA'
        
        if (GotAccType == "Savings account"):
            GotAccType = 'SA'
        
        if (GotAccType == 'Certificate of Deposit (CD)'):
            GotAccType = 'COD'

        if (GotAccType == 'Money market account'):
            GotAccType = 'MMA'

        if (GotAccType == 'Individual Retirement Accounts (IRAs)'):
            GotAccType = 'IRA'

            
        GotAccID = ''
        c.execute("SELECT balanceId FROM Balance WHERE userId is '{}' and accType is '{}'".format(GotId,GotAccType))
        for row in c.fetchall():
            GotAccID = operator.itemgetter(0)(row)        
            
        data.insertIntoLoansRequest(GotId, GotAccID, GotAmount, GotComment)
        
    def AboutLoans(self):
        print('loans')
        
    def EditUserProfile(self): 
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbACcountSettings = tk.Label(self, text = 'Account settings')
        self.lbChangeUsername = tk.Label(self, text = 'Change username')
        self.lbChangeMiddlename = tk.Label(self, text = 'Change middlename')
        self.lbChangeSurname = tk.Label(self, text = 'Change surname')
        self.lbChangePassword = tk.Label(self, text = 'Change password')
        self.lbChangeHouseNumber = tk.Label(self, text = 'Change house number')
        self.lbChangeStreet = tk.Label(self, text = 'Change street')
        self.lbChangeCity= tk.Label(self, text = 'Change city')
        self.lbChangePostCode = tk.Label(self, text = 'Change post code')

        self.EntryChangeUsername = tk.Entry(self)
        self.EntryChangeMiddlename = tk.Entry(self)
        self.EntryChangeSurname = tk.Entry(self)
        self.EntryChangePassword = tk.Entry(self)
        self.EntryChangeHouseNumber = tk.Entry(self)
        self.EntryChangeStreet = tk.Entry(self)
        self.EntryChangeCity = tk.Entry(self)
        self.EntryChangePostCode = tk.Entry(self)
        
        self.btnConfirmRequest = tk.Button(self,text ='Confirm')  
        
        self.lbACcountSettings.place(x = 280, y = 25)
        self.lbChangeUsername.place(x = 280, y = 60)
        self.EntryChangeUsername.place(x = 450, y = 60)
        self.lbChangeMiddlename.place(x = 280, y = 95)
        self.EntryChangeMiddlename.place(x = 450, y = 95)
        self.lbChangeSurname.place(x = 280, y = 130)
        self.EntryChangeSurname.place(x = 450, y = 130)
        self.lbChangePassword.place(x = 280, y = 165)
        self.EntryChangePassword.place(x = 450, y = 165)
        self.lbChangeHouseNumber.place(x = 280, y = 200)
        self.EntryChangeHouseNumber.place(x = 450, y = 200)
        self.lbChangeStreet.place(x = 280, y = 235)
        self.EntryChangeStreet.place(x = 450, y = 235)
        self.lbChangeCity.place(x = 280, y = 270)
        self.EntryChangeCity.place(x = 450, y = 270)
        self.lbChangePostCode.place(x = 280, y = 305)
        self.EntryChangePostCode.place(x = 450, y = 305)
        self.btnConfirmRequest.place(x = 280, y = 340)
        
    def RecentActivity(self):
        print('RecentActivity')
        
    def RemoveUser(self):
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        
        self.lbDeliteUser = tk.Label(self, text = 'Delite account')
        self.lbDeliteUserUsername = tk.Label(self, text = 'Enter your username')
        self.lbDeliteUserSurname = tk.Label(self, text = 'Enter your surname')
        self.lbDeliteUserPassword = tk.Label(self, text = 'Enter your password')

        self.EntryDeliteUserUsername = tk.Entry(self)
        self.EntryDeliteUserSurname = tk.Entry(self)
        self.EntryDeliteUserPassword = tk.Entry(self)
        
        self.btnConfirmDelite = tk.Button(self,text ='Confirm')  
        
        self.lbDeliteUser.place(x = 280, y = 25)
        self.lbDeliteUserUsername.place(x = 280, y = 60)
        self.EntryDeliteUserUsername.place(x = 450, y = 60)
        self.lbDeliteUserSurname.place(x = 280, y = 95)
        self.EntryDeliteUserSurname.place(x = 450, y = 95)
        self.lbDeliteUserPassword.place(x = 280, y = 130)
        self.EntryDeliteUserPassword.place(x = 450, y = 130)
        self.btnConfirmDelite.place(x = 280, y = 165)
        
    def RemoveAccountType(self):
        self.lbACcountSettings.place_forget()
        self.lbChangeUsername.place_forget()
        self.EntryChangeUsername.place_forget()
        self.lbChangeMiddlename.place_forget()
        self.EntryChangeMiddlename.place_forget()
        self.lbChangeSurname.place_forget()
        self.EntryChangeSurname.place_forget()
        self.lbChangePassword.place_forget()
        self.EntryChangePassword.place_forget()
        self.lbChangeHouseNumber.place_forget()
        self.EntryChangeHouseNumber.place_forget()
        self.lbChangeStreet.place_forget()
        self.EntryChangeStreet.place_forget()
        self.lbChangeCity.place_forget()
        self.EntryChangeCity.place_forget()
        self.lbChangePostCode.place_forget()
        self.EntryChangePostCode.place_forget()
        self.btnConfirmRequest.place_forget()
        self.lbDeliteUser.place_forget()
        self.lbDeliteUserType.place_forget()
        self.wRequestAcc.place_forget()
        self.lbDeliteUserUsername.place_forget()
        self.EntryDeliteUserUsername.place_forget()
        self.lbDeliteUserSurname.place_forget()
        self.EntryDeliteUserSurname.place_forget()
        self.lbDeliteUserPassword.place_forget()
        self.EntryDeliteUserPassword.place_forget()
        self.btnConfirmDelite.place_forget()
        self.OPTIONSRemove = [
        "Checking account",
        "Savings account",
        'Certificate of Deposit (CD)',
        'Money market account',
        'Individual Retirement Accounts (IRAs)'
        ] 
        
        self.variableRemove = tk.StringVar(self)
        self.variableRemove .set(self.OPTIONSRemove[0])
        
        self.lbDeliteUser = tk.Label(self, text = 'Delite account type')
        self.lbDeliteUserType = tk.Label(self, text = 'Chose account type')
        self.lbDeliteUserUsername = tk.Label(self, text = 'Enter your username')
        self.lbDeliteUserSurname = tk.Label(self, text = 'Enter your surname')
        self.lbDeliteUserPassword = tk.Label(self, text = 'Enter your password')

        self.EntryDeliteUserUsername = tk.Entry(self)
        self.EntryDeliteUserSurname = tk.Entry(self)
        self.EntryDeliteUserPassword = tk.Entry(self)
        
        self.wRequestAcc = tk.OptionMenu(self, self.variableRemove, *self.OPTIONSRemove)
        
        self.btnConfirmDelite = tk.Button(self,text ='Confirm')  
        
        self.lbDeliteUser.place(x = 280, y = 25)
        self.lbDeliteUserType.place(x = 280, y = 60)
        self.wRequestAcc.place(x = 450, y = 60)
        self.lbDeliteUserUsername.place(x = 280, y = 95)
        self.EntryDeliteUserUsername.place(x = 450, y = 95)
        self.lbDeliteUserSurname.place(x = 280, y = 130)
        self.EntryDeliteUserSurname.place(x = 450, y = 130)
        self.lbDeliteUserPassword.place(x = 280, y = 165)
        self.EntryDeliteUserPassword.place(x = 450, y = 165)
        self.btnConfirmDelite.place(x = 280, y = 200)
        
class Acc1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
    
        self.labelUsername = tk.Label(self, text = 'Acc1Page')
        
        self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        
        self.labelUsername.pack()
        self.buttonBack.pack()
        
class Acc2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
    
        self.labelUsername = tk.Label(self, text = 'Acc2Page')
        
        self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        
        self.labelUsername.pack()
        self.buttonBack.pack()
        
class Acc3Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
    
        self.labelUsername = tk.Label(self, text = 'Acc3Page')
        
        self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        
        self.labelUsername.pack()
        self.buttonBack.pack()

        
class AdminPageBase(tk.Frame):
     def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'admin page')
        self.label.pack()
        
        buttonAddUser = ttk.Button(self, text = 'Add user', command = lambda: controller.show_frame(AdminPage))
        buttonAddUser.pack()
        
        buttonSearch = tk.Button(self, text = 'Search users', command = lambda: controller.show_frame(AdminPageSearch))
        buttonSearch.pack()
        
        buttonEditAppointments = tk.Button(self, text = 'Manadge appointments', command = lambda: controller.show_frame(AdminManadgeAppointments))
        buttonEditAppointments.pack()
        
        buttonLogIntoUser = tk.Button(self, text = 'Log into user', command = lambda: controller.show_frame(MoveToUser))
        buttonLogIntoUser.pack()
        
        buttonManagmentReport = tk.Button(self, text = 'Request management report', command = lambda: controller.show_frame(ManagmentReport))
        buttonManagmentReport.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(LoginPage))
        buttonBack.pack()
        
class ManagmentReport(tk.Frame):
     def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Data:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        
        self.NumberOfCustomers = tk.Button(self.frm,text ='Number of customers', command = self.AllUsers)
        self.NumberOfCustomers.pack(expand=False, fill='x')
        
        self.SumMoney = tk.Button(self.frm,text ='Sum of all money',command = self.SumOfMoney)
        self.SumMoney.pack(expand=False, fill='x')
        
        self.SumInterest = tk.Button(self.frm,text ='Sum of interest rate', command = self.SumOfInterest)
        self.SumInterest.pack(expand=False, fill='x')
        
        self.Total = tk.Button(self.frm,text ='Toal overdrafts', command = self.SumOfOverdrafts)
        self.Total.pack(expand=False, fill='x')
        
        self.back = tk.Button(self.frm,text ='Back', command = lambda: controller.show_frame(AdminPageBase))
        self.back.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()              

     def AllUsers(self):     
        self.tv.grid_remove()    
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'nul')
        self.tv.heading("#0", text='User sum')
        self.tv.column("#0", anchor='center', width=200)
        self.tv.heading('nul', text='')
        self.tv.column('nul', anchor='center', width=0)

        self.treeview = self.tv
  
        c.execute("SELECT COUNT(Users.userAccType) FROM Users WHERE Users.userAccType is 'user'")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            BalanceSum = operator.itemgetter(0)(row)
            self.treeview.insert('', 'end',text=BalanceSum)
            
     def SumOfMoney(self):   
        self.tv.grid_remove()    
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'nul')
        self.tv.heading("#0", text='Balance sum')
        self.tv.column("#0", anchor='center', width=200)
        self.tv.heading('nul', text='')
        self.tv.column('nul', anchor='center', width=0)

        self.treeview = self.tv
  
        c.execute("SELECT SUM(Balance.balance) FROM Balance")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            BalanceSum = operator.itemgetter(0)(row)
            self.treeview.insert('', 'end',text=BalanceSum)
            
     def SumOfInterest(self):
        self.tv.grid_remove()    
        for i in self.tv.get_children():
            self.tv.delete(i)
            
        BalanceSum1 = 0
        InterestRate1 = 0
        BalanceSum2 = 0
        InterestRate2 = 0
        BalanceSum3 = 0
        InterestRate3 = 0
        BalanceSum4 = 0
        InterestRate4 = 0
        BalanceSum5 = 0
        InterestRate5 = 0
        
        c.execute("SELECT  sum(balance) FROM Balance WHERE balance > 0 and InterestId like 1")
        for row in c.fetchall():
            BalanceSum1 = float(operator.itemgetter(0)(row) or 0)
           
        c.execute("SELECT Rate FROM Interest Where InterestId like 1")
        for row in c.fetchall():   
            InterestRate1 = float(operator.itemgetter(0)(row) or 0)
            
        c.execute("SELECT  sum(balance) FROM Balance WHERE balance > 0 and InterestId like 2")
        for row in c.fetchall():
            BalanceSum2 = float(operator.itemgetter(0)(row) or 0)
           
        c.execute("SELECT Rate FROM Interest Where InterestId like 2")
        for row in c.fetchall():   
            InterestRate2 = float(operator.itemgetter(0)(row) or 0)
            
        c.execute("SELECT  sum(balance) FROM Balance WHERE balance > 0 and InterestId like 3")
        for row in c.fetchall():
            BalanceSum3 = float(operator.itemgetter(0)(row) or 0)
           
        c.execute("SELECT Rate FROM Interest Where InterestId like 3")
        for row in c.fetchall():   
            InterestRate3 = float(operator.itemgetter(0)(row) or 0)
            
        c.execute("SELECT  sum(balance) FROM Balance WHERE balance > 0 and InterestId like 4")
        for row in c.fetchall():
            BalanceSum4 = float(operator.itemgetter(0)(row) or 0)
            
        c.execute("SELECT Rate FROM Interest Where InterestId like 4")
        for row in c.fetchall():   
            InterestRate4 = float(operator.itemgetter(0)(row) or 0)
            
        c.execute("SELECT  sum(balance) FROM Balance WHERE balance > 0 and InterestId like 5")
        for row in c.fetchall():
            BalanceSum5 = float(operator.itemgetter(0)(row) or 0)
           
        c.execute("SELECT Rate FROM Interest Where InterestId like 5")
        for row in c.fetchall():   
            InterestRate5 = float(operator.itemgetter(0)(row) or 0)
            
        print(        
            BalanceSum1,
            InterestRate1,
            BalanceSum2,
            InterestRate2,
            BalanceSum3,
            InterestRate3,
            BalanceSum4,
            InterestRate4,
            BalanceSum5,
            InterestRate5)
        total = (BalanceSum1*InterestRate1) + (BalanceSum2*InterestRate2) + (BalanceSum3*InterestRate3) + (BalanceSum4*InterestRate4) + (BalanceSum5*InterestRate5)
            
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'SumYear')
        self.tv.heading("#0", text='Sum for one month')
        self.tv.column("#0", anchor='center', width=200)
        self.tv.heading('SumYear', text='SumFor one year')
        self.tv.column('SumYear', anchor='center', width=200)
        self.treeview = self.tv
 
        self.treeview.insert('', 'end',text=total,  values = (total*12))
        
     def SumOfOverdrafts(self):   
        self.tv.grid_remove()    
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'nul')
        self.tv.heading("#0", text='Overdrafts sum')
        self.tv.column("#0", anchor='center', width=200)
        self.tv.heading('nul', text='')
        self.tv.column('nul', anchor='center', width=0)

        self.treeview = self.tv
  
        c.execute("SELECT SUM(UserOverdrafts.Quantity) FROM UserOverdrafts")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            OverSum = operator.itemgetter(0)(row)
            self.treeview.insert('', 'end',text=OverSum)

class MoveToUser(tk.Frame):
     def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.lbUserName = tk.Label(self, text = 'Insert user name')
        self.lbUserSurname = tk.Label(self, text = 'Insert user surname')

        self.EntryUserName  = tk.Entry(self)
        self.EntryUserSurname = tk.Entry(self)
        
        self.buttonLogin = ttk.Button(self, text = 'Login', command = self.MoveOn)
        
        self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(AdminPageBase))
   
        self.lbUserName.place(x = 800, y = 70)
        self.EntryUserName.place(x = 950, y = 70)
        self.lbUserSurname.place(x = 800, y = 105)
        self.EntryUserSurname.place(x = 950, y = 105)
        self.buttonLogin.place(x = 800, y = 140)
        self.buttonBack.place(x = 890, y = 140)
        
     def MoveOn(self):
        global GlIdUser
        GotUserName = str(self.EntryUserName.get())
        GotUserSurname = str(self.EntryUserSurname.get())
        
        c.execute("SELECT userId From Users WHERE Users.userName is '{}' and Users.userSurname is '{}' and Users.userAccType is 'user'".format(GotUserName,GotUserSurname))
        for row in c.fetchall():
            GlIdUser = operator.itemgetter(0)(row) 
            
        self.EntryUserName.delete(0, 'end')
        self.EntryUserSurname.delete(0, 'end')
        b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UserPageAccSelect))
        b.invoke()
             
class AdminManadgeAppointments(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = 'nil'
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Data:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.OPTIONS = [
        "Loc1",
        "Loc2",
        "Loc3"
        ] 
        
        self.OPTIONSyear = [
        "2018",
        "2019",
        "2020"
        ] 
        
        self.OPTIONSmonth = [    
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'
        ] 
        
        self.OPTIONSday = [
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            '24',
            '25',
            '26',
            '27',
            '28',
            '29',
            '30',
            '31'
        ] 
        
        self.variable = tk.StringVar(self)
        self.variable.set(self.OPTIONS[0])
        
        self.variableyear = tk.StringVar(self)
        self.variableyear.set(self.OPTIONSyear[0])
        
        self.variablemonth = tk.StringVar(self)
        self.variablemonth.set(self.OPTIONSmonth[0])
        
        self.variableday = tk.StringVar(self)
        self.variableday.set(self.OPTIONSday[0])
        
        
        self.labelAppointmentID = tk.Label(self, text = 'Enter appointment ID')
        self.labelUserID = tk.Label(self, text = 'Enter user ID')
        self.labelUserName = tk.Label(self, text = 'Enter user name:')
        self.labelUserSurname = tk.Label(self, text = 'Enter user surname:')
        self.labelAppointmentAddress = tk.Label(self, text = 'Enter address of appointment:')
        self.w = tk.OptionMenu(self, self.variable, *self.OPTIONS)   
        self.labelAppointmentDate = tk.Label(self, text = 'Enter date of appointment:')
        self.wyear = tk.OptionMenu(self, self.variableyear, *self.OPTIONSyear)
        self.wmonth = tk.OptionMenu(self, self.variablemonth, *self.OPTIONSmonth)
        self.wday = tk.OptionMenu(self, self.variableday, *self.OPTIONSday)
        self.labelAppointmentStatus = tk.Label(self, text = 'Enter appintment status:')
        self.labelAppointmentComment= tk.Label(self, text = 'Add coment if you want:')
        self.enterAppointmentID = tk.Entry(self)
        self.enterUserID = tk.Entry(self)
        self.entryUserName = tk.Entry(self)
        self.entryUserSurname = tk.Entry(self)
        self.entryAppointmentStatus = tk.Entry(self)
        self.entryAppointmentComment = tk.Entry(self)
        self.buttonBook = ttk.Button(self, text = 'Update', command = self.updateToDb)
        
        self.labelAppointmentIDFind = tk.Label(self, text = 'Appointment ID:')
        self.labelUserIDFind = tk.Label(self, text = 'User ID:')
        self.labelPlaceFind = tk.Label(self, text = 'Place:')
        self.labelDateFind = tk.Label(self, text = 'Date of appointment:')
        self.labelAppointmentStatusFind = tk.Label(self, text = 'Appointment status:')
        self.labelUserNameFind = tk.Label(self, text = 'User name:')
        self.labelUserSurnameFind = tk.Label(self, text = 'User surname:')
        self.labelUserCommentFind = tk.Label(self, text = 'User comment:')
        self.EntryAppointmentIDFind = tk.Entry(self) 
        self.EntryUserIDFind = tk.Entry(self)
        self.EntryPlaceFind = tk.Entry(self)
        self.EntryDateFind = tk.Entry(self)
        self.EntryAppointmentStatusFind = tk.Entry(self)
        self.EntryUserNameFind = tk.Entry(self)
        self.EntryUserSurnameFind = tk.Entry(self)
        self.EntryUserCommentFind = tk.Entry(self)
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelAppointmentID.place_forget()
        self.enterAppointmentID.place_forget()
        self.labelUserID.place_forget()
        self.enterUserID.place_forget()
        self.labelUserName.place_forget()
        self.entryUserName.place_forget()
        self.labelUserSurname.place_forget()
        self.entryUserSurname.place_forget()
        self.labelAppointmentAddress.place_forget()
        self.w.place_forget()
        self.labelAppointmentDate.place_forget()
        self.wday.place_forget()
        self.wmonth.place_forget()
        self.wyear.place_forget()
        self.labelAppointmentStatus.place_forget()
        self.entryAppointmentStatus.place_forget()
        self.labelAppointmentComment.place_forget()
        self.entryAppointmentComment.place_forget()
        self.buttonBook.place_forget()
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.showAll = tk.Button(self.frm,text ='Show all', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.Find = tk.Button(self.frm,text ='Find appointment', command = self.FindList)
        self.Find.pack(expand=False, fill='x')
        
        self.btnEditAppoitmnet = tk.Button(self.frm,text ='Edit appointment', command = self.EditAppointment)
        self.btnEditAppoitmnet.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(AdminPageBase))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()          

    def EditAppointment(self):     
        self.labelAppointmentID.place_forget()
        self.enterAppointmentID.place_forget()
        self.labelUserID.place_forget()
        self.enterUserID.place_forget()
        self.labelUserName.place_forget()
        self.entryUserName.place_forget()
        self.labelUserSurname.place_forget()
        self.entryUserSurname.place_forget()
        self.labelAppointmentAddress.place_forget()
        self.w.place_forget()
        self.labelAppointmentDate.place_forget()
        self.wday.place_forget()
        self.wmonth.place_forget()
        self.wyear.place_forget()
        self.labelAppointmentStatus.place_forget()
        self.entryAppointmentStatus.place_forget()
        self.labelAppointmentComment.place_forget()
        self.entryAppointmentComment.place_forget()
        self.buttonBook.place_forget()
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid_forget() 
        
        self.OPTIONS = [
        "Loc1",
        "Loc2",
        "Loc3"
        ] 
        
        self.OPTIONSyear = [
        "2018",
        "2019",
        "2020"
        ] 
        
        self.OPTIONSmonth = [    
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'
        ] 
        
        self.OPTIONSday = [
            "1",
            "2",
            "3",
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            '24',
            '25',
            '26',
            '27',
            '28',
            '29',
            '30',
            '31'
        ] 
        
        self.variable = tk.StringVar(self)
        self.variable.set(self.OPTIONS[0])
        
        self.variableyear = tk.StringVar(self)
        self.variableyear.set(self.OPTIONSyear[0])
        
        self.variablemonth = tk.StringVar(self)
        self.variablemonth.set(self.OPTIONSmonth[0])
        
        self.variableday = tk.StringVar(self)
        self.variableday.set(self.OPTIONSday[0])
        
        self.labelAppointmentID = tk.Label(self, text = 'Enter appointment ID')
        self.labelUserID = tk.Label(self, text = 'Enter user ID')
        self.labelUserName = tk.Label(self, text = 'Enter user name:')
        self.labelUserSurname = tk.Label(self, text = 'Enter user surname:')
        self.labelAppointmentAddress = tk.Label(self, text = 'Enter address of appointment:')
        self.w = tk.OptionMenu(self, self.variable, *self.OPTIONS)
        
        self.labelAppointmentDate = tk.Label(self, text = 'Enter date of appointment:')
        self.wyear = tk.OptionMenu(self, self.variableyear, *self.OPTIONSyear)
        self.wmonth = tk.OptionMenu(self, self.variablemonth, *self.OPTIONSmonth)
        self.wday = tk.OptionMenu(self, self.variableday, *self.OPTIONSday)
        
        self.labelAppointmentStatus = tk.Label(self, text = 'Enter appintment status:')
        self.labelAppointmentComment= tk.Label(self, text = 'Add coment if you want:')
        
        self.enterAppointmentID = tk.Entry(self)
        self.enterUserID = tk.Entry(self)
        self.entryUserName = tk.Entry(self)
        self.entryUserSurname = tk.Entry(self)
        self.entryAppointmentStatus = tk.Entry(self)
        self.entryAppointmentComment = tk.Entry(self)
        
        self.entryUserName.delete(0, 'end')
        
        self.buttonBook = ttk.Button(self, text = 'Update', command = self.updateToDb)
         
        self.labelAppointmentID.place(x = 170,y = 25) 
        self.enterAppointmentID.place(x = 370,y = 25)
        self.labelUserID.place(x = 170,y = 60)
        self.enterUserID.place(x = 370,y = 60)
        self.labelUserName.place(x = 170,y = 95)
        self.entryUserName.place(x = 370,y = 95)
        self.labelUserSurname.place(x = 170,y = 130)
        self.entryUserSurname.place(x = 370,y = 130)
        self.labelAppointmentAddress.place(x = 170,y = 165)
        self.w.place(x = 370,y = 165)
        self.labelAppointmentDate.place(x = 170,y = 200)
        self.wday.place(x = 370,y = 200)
        self.wmonth.place(x = 410,y = 200)
        self.wyear.place(x = 450,y = 200)
        self.labelAppointmentStatus.place(x = 170,y = 235)
        self.entryAppointmentStatus.place(x = 370,y = 235)
        self.labelAppointmentComment.place(x = 170,y = 270)
        self.entryAppointmentComment.place(x = 370,y = 270)
        
        self.buttonBook.place(x = 180,y = 305)
        
    def updateToDb(self):
        a = (calendar.monthrange(int(str(self.variableyear.get())),int(str(self.variablemonth.get())))[1])

        if(a < int(self.variableday.get())):
            print('error')
            self.variableday.set(a)
            
        Sep = '.'
        AllDates = (str(self.variableday.get())), (str(self.variablemonth.get())),((str(self.variableyear.get()))) 
        
        GotAppintmentID = str(self.enterAppointmentID.get())
        GotUserID = str(self.enterUserID.get())
        GotPlace = str(self.variable.get())
        GotDate = Sep.join(AllDates)
        GotUserStatus = str(self.entryAppointmentStatus.get())
        GotUserName = str(self.entryUserName.get())
        GotUserSurname = str(self.entryUserSurname.get())
        GotUserComment = str(self.entryAppointmentComment.get())
        print('1')
        print(GotAppintmentID,GotUserID, GotPlace, GotDate, GotUserStatus, GotUserName, GotUserSurname, GotUserComment)
        data.updateIntoAppointments(GotAppintmentID,GotUserID, GotPlace, GotDate, GotUserStatus, GotUserName, GotUserSurname, GotUserComment)
        
        self.variable.set(self.OPTIONS[0])
        self.variableyear.set(self.OPTIONSyear[0])
        self.variablemonth.set(self.OPTIONSmonth[0])
        self.variableday.set(self.OPTIONSday[0])
        self.enterAppointmentID.delete(0,'end')
        self.enterUserID.delete(0, 'end')        
        self.entryUserName.delete(0, 'end')
        self.entryUserSurname.delete(0, 'end')    
        self.entryAppointmentStatus.delete(0, 'end') 
        self.entryAppointmentComment.delete(0, 'end')       

    def PrintAll(self):      
        self.labelAppointmentID.place_forget()
        self.enterAppointmentID.place_forget()
        self.labelUserID.place_forget()
        self.enterUserID.place_forget()
        self.labelUserName.place_forget()
        self.entryUserName.place_forget()
        self.labelUserSurname.place_forget()
        self.entryUserSurname.place_forget()
        self.labelAppointmentAddress.place_forget()
        self.w.place_forget()
        self.labelAppointmentDate.place_forget()
        self.wday.place_forget()
        self.wmonth.place_forget()
        self.wyear.place_forget()
        self.labelAppointmentStatus.place_forget()
        self.entryAppointmentStatus.place_forget()
        self.labelAppointmentComment.place_forget()
        self.entryAppointmentComment.place_forget()
        self.buttonBook.place_forget()
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid_forget() 
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'userId', 'placeOfAppintment','dateOfAppointment','appointmentStatus','userName','userSurname','userComment')
        self.tv.heading("#0", text='Appointmetn ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('userId', text='User ID')
        self.tv.column('userId', anchor='center', width=100)
        self.tv.heading('placeOfAppintment', text='Place of appintment')
        self.tv.column('placeOfAppintment', anchor='center', width=100)
        self.tv.heading('dateOfAppointment', text='Date of appointment')
        self.tv.column('dateOfAppointment', anchor='center', width=100)
        self.tv.heading('appointmentStatus', text='Appointment status')
        self.tv.column('appointmentStatus', anchor='center', width=100)
        self.tv.heading('userName', text='user name')
        self.tv.column('userName', anchor='center', width=100)
        self.tv.heading('userSurname', text='user surname')
        self.tv.column('userSurname', anchor='center', width=100)
        self.tv.heading('userComment', text='user comment')
        self.treeview = self.tv
  
        c.execute("SELECT * FROM Appointments")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            appointmetnId ,userId, placeOfAppintment, dateOfAppointment, appointmentStatus, userName ,userSurname, userComment = operator.itemgetter(0,1,2,3,4,5,6,7)(row)
            self.treeview.insert('', 'end',text=appointmetnId,  values=(userId, placeOfAppintment, dateOfAppointment, appointmentStatus, userName ,userSurname, userComment))
           
    def FindList(self):  
        self.labelAppointmentID.place_forget()
        self.enterAppointmentID.place_forget()
        self.labelUserID.place_forget()
        self.enterUserID.place_forget()
        self.labelUserName.place_forget()
        self.entryUserName.place_forget()
        self.labelUserSurname.place_forget()
        self.entryUserSurname.place_forget()
        self.labelAppointmentAddress.place_forget()
        self.w.place_forget()
        self.labelAppointmentDate.place_forget()
        self.wday.place_forget()
        self.wmonth.place_forget()
        self.wyear.place_forget()
        self.labelAppointmentStatus.place_forget()
        self.entryAppointmentStatus.place_forget()
        self.labelAppointmentComment.place_forget()
        self.entryAppointmentComment.place_forget()
        self.buttonBook.place_forget()
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid_forget() 
        
        self.labelAppointmentIDFind = tk.Label(self, text = 'Appointment ID:')
        self.labelUserIDFind = tk.Label(self, text = 'User ID:')
        self.labelPlaceFind = tk.Label(self, text = 'Place:')
        self.labelDateFind = tk.Label(self, text = 'Date of appointment:')
        self.labelAppointmentStatusFind = tk.Label(self, text = 'Appointment status:')
        self.labelUserNameFind = tk.Label(self, text = 'User name:')
        self.labelUserSurnameFind = tk.Label(self, text = 'User surname:')
        self.labelUserCommentFind = tk.Label(self, text = 'User comment:')
        
        self.EntryAppointmentIDFind = tk.Entry(self) 
        self.EntryUserIDFind = tk.Entry(self)
        self.EntryPlaceFind = tk.Entry(self)
        self.EntryDateFind = tk.Entry(self)
        self.EntryAppointmentStatusFind = tk.Entry(self)
        self.EntryUserNameFind = tk.Entry(self)
        self.EntryUserSurnameFind = tk.Entry(self)
        self.EntryUserCommentFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelAppointmentIDFind.place(x = 170,y = 25)
        self.labelUserIDFind.place(x = 170,y = 60)
        self.labelPlaceFind.place(x = 170,y = 95)
        self.labelDateFind.place(x = 170,y = 130)
        self.labelAppointmentStatusFind.place(x = 170,y = 165)
        self.labelUserNameFind.place(x = 170,y = 200)
        self.labelUserSurnameFind.place(x = 170,y = 235)
        self.labelUserCommentFind.place(x = 170,y = 270)
                
        self.EntryAppointmentIDFind.place(x = 350,y = 25)
        self.EntryUserIDFind.place(x = 350,y = 60)
        self.EntryPlaceFind.place(x = 350,y = 95)
        self.EntryDateFind.place(x = 350,y = 130)
        self.EntryAppointmentStatusFind.place(x = 350,y = 165)
        self.EntryUserNameFind.place(x = 350,y = 200)
        self.EntryUserSurnameFind.place(x = 350,y = 235)
        self.EntryUserCommentFind.place(x = 350,y = 270)
        
        self.BtnGetDataFind.place(x = 180,y = 300)

    def ShowGottenData(self):         
        self.labelAppointmentID.place_forget()
        self.enterAppointmentID.place_forget()
        self.labelUserID.place_forget()
        self.enterUserID.place_forget()
        self.labelUserName.place_forget()
        self.entryUserName.place_forget()
        self.labelUserSurname.place_forget()
        self.entryUserSurname.place_forget()
        self.labelAppointmentAddress.place_forget()
        self.w.place_forget()
        self.labelAppointmentDate.place_forget()
        self.wday.place_forget()
        self.wmonth.place_forget()
        self.wyear.place_forget()
        self.labelAppointmentStatus.place_forget()
        self.entryAppointmentStatus.place_forget()
        self.labelAppointmentComment.place_forget()
        self.entryAppointmentComment.place_forget()
        self.buttonBook.place_forget()
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid_forget() 
        
        GotAppointmentID = str(self.EntryAppointmentIDFind.get())
        GotUserID = str(self.EntryUserIDFind.get())
        GotPlace = str(self.EntryPlaceFind.get())
        GotDate = str(self.EntryDateFind.get())
        GotStatus = str(self.EntryAppointmentStatusFind.get())
        GotUserName = str(self.EntryUserNameFind.get())
        GotUserSurname = str(self.EntryUserSurnameFind.get())
        GotUserComment = str(self.EntryUserCommentFind.get())
        
        self.labelAppointmentIDFind.place_forget()
        self.labelUserIDFind.place_forget()
        self.labelPlaceFind.place_forget()
        self.labelDateFind.place_forget()
        self.labelAppointmentStatusFind.place_forget()
        self.labelUserNameFind.place_forget()
        self.labelUserSurnameFind.place_forget()
        self.labelUserCommentFind.place_forget()
                
        self.EntryAppointmentIDFind.place_forget()
        self.EntryUserIDFind.place_forget()
        self.EntryPlaceFind.place_forget()
        self.EntryDateFind.place_forget()
        self.EntryAppointmentStatusFind.place_forget()
        self.EntryUserNameFind.place_forget()
        self.EntryUserSurnameFind.place_forget()
        self.EntryUserCommentFind.place_forget()
        
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'userId', 'placeOfAppintment','dateOfAppointment','appointmentStatus','userName','userSurname','userComment')
        self.tv.heading("#0", text='Appointmetn ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('userId', text='User ID')
        self.tv.column('userId', anchor='center', width=100)
        self.tv.heading('placeOfAppintment', text='Place of appintment')
        self.tv.column('placeOfAppintment', anchor='center', width=100)
        self.tv.heading('dateOfAppointment', text='Date of appointment')
        self.tv.column('dateOfAppointment', anchor='center', width=100)
        self.tv.heading('appointmentStatus', text='Appointment status')
        self.tv.column('appointmentStatus', anchor='center', width=100)
        self.tv.heading('userName', text='user name')
        self.tv.column('userName', anchor='center', width=100)
        self.tv.heading('userSurname', text='user surname')
        self.tv.column('userSurname', anchor='center', width=100)
        self.tv.heading('userComment', text='user comment')
        self.treeview = self.tv
        
        c.execute("SELECT * FROM Appointments WHERE appointmentsId = '{}' OR userId = '{}' OR placeOfAppointment = '{}' OR dateOfAppointment = '{}' OR appointmentStatus = '{}' OR userName = '{}' OR userSurname = '{}' OR userComment = '{}'".format(GotAppointmentID, GotUserID, GotPlace, GotDate, GotStatus, GotUserName, GotUserSurname, GotUserComment))
        lis = []
        for row in c.fetchall():
            lis.append(row)     
            appointmetnId ,userId, placeOfAppintment, dateOfAppointment, appointmentStatus, userName ,userSurname, userComment= operator.itemgetter(0,1,2,3,4,5,6,7)(row)
            self.treeview.insert('', 'end',text=appointmetnId,  values=(userId, placeOfAppintment, dateOfAppointment, appointmentStatus, userName ,userSurname, userComment))
        
class AdminPage(tk.Frame):
        def __init__ (self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                self.status = ''
                
                self.labelPageName = tk.Label(self, text = 'admin page')
                self.labelAddUser = tk.Label(self, text = 'Add user')
                
                self.labelUserName = tk.Label(self, text = 'Enter user name:')
                self.labelUserMiddleName = tk.Label(self, text = 'Enter user middle name (optional)')
                self.labelUserSurname = tk.Label(self, text = 'Enter user surname:')
                self.labelUserPassword = tk.Label(self, text = 'Enter user password:')
                self.labelUserHouseNumber = tk.Label(self, text = 'Enter user house number:')
                self.labelUserStreet = tk.Label(self, text = 'Enter user street address:')
                self.labelUserCity = tk.Label(self, text = 'Enter user city:')
                self.labelUserPostcode = tk.Label(self, text = 'Enter user post code:')
                self.labelUserStatus = tk.Label(self, text = 'Enter user status:')
            
                self.entryUserName = tk.Entry(self)
                self.enteryUserMiddleName = tk.Entry(self)
                self.entryUserSurname = tk.Entry(self)
                self.entryUserPassword = tk.Entry(self)
                self.entryUserHouseNumber = tk.Entry(self)
                self.entryUserStreet = tk.Entry(self)
                self.entryUserCity = tk.Entry(self)
                self.entryUserPostcode = tk.Entry(self)
                
                self.rb1 = tk.Radiobutton(self,text='user', variable= self.status, 
                                  value="user", command=self.selected1)
        
                self.rb2 = tk.Radiobutton(self,text='admin', variable=self.status, 
                                  value="admin", command=self.selected2)
                
                self.checkedCa = False
                self.checkSa = False
                self.checkCOd = False
                self.checkMMa = False
                self.checkIRa = False
                
                self.buttonAddUser = ttk.Button(self, text = 'Add user to system', command = self.printInfo)
                self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(AdminPageBase))
                
                self.checkCA = tk.Checkbutton(self, text="Checking Account",command = self.checkCA)
                self.checkSA = tk.Checkbutton(self, text="Savings account",command = self.checkSA)
                self.checkCOD = tk.Checkbutton(self, text="Certificate of Deposit (CD)",command = self.checkCOD)
                self.checkMMA = tk.Checkbutton(self, text="Money market account",command = self.checkMMA)
                self.checkIRA = tk.Checkbutton(self, text="Individual Retirement Accounts (IRAs)",command = self.checkIRA)
                    
                self.flag = 0
                
                self.labelPageName.pack()
                self.labelAddUser.pack()
                
                self.labelUserName.pack()
                self.entryUserName.pack()
                
                self.labelUserMiddleName.pack()
                self.enteryUserMiddleName.pack()
                
                self.labelUserSurname.pack()
                self.entryUserSurname.pack()
                
                self.labelUserPassword.pack()
                self.entryUserPassword.pack()
                
                self.labelUserHouseNumber.pack()
                self.entryUserHouseNumber.pack()
                
                self.labelUserStreet.pack()
                self.entryUserStreet.pack()
                
                self.labelUserCity.pack()
                self.entryUserCity.pack()
                
                self.labelUserPostcode.pack()
                self.entryUserPostcode.pack()
                
                self.labelUserStatus.pack()
                self.rb1.pack()
                self.rb2.pack()
                
                self.checkCA.pack()
                self.checkSA.pack()
                self.checkCOD.pack()
                self.checkMMA.pack()
                self.checkIRA.pack()
                
                self.buttonAddUser.pack()
                self.buttonBack.pack()
        
        def checkCA(self):
            if (self.checkedCa == True):
                self.checkedCa = False
            elif(self.checkedCa == False):
                self.checkedCa = True
            
        def checkSA(self):
            if (self.checkSa == True):
                self.checkSa = False
            elif(self.checkSa == False):
                self.checkSa = True
                
        def checkCOD(self):
            if (self.checkCOd == True):
                self.checkCOd = False
            elif(self.checkCOd == False):
                self.checkCOd = True
                
        def checkMMA(self):
            if (self.checkMMa == True):
                self.checkMMa = False
            elif(self.checkMMa == False):
                self.checkMMa = True
                
        def checkIRA(self):
            if (self.checkIRa == True):
                self.checkIRa = False
            elif(self.checkIRa == False):
                self.checkIRa = True
           
        def selected1(self):
            self.flag = 1
            
        def selected2(self):
            self.flag = 2
                
        def printInfo(self):
            UserName = str(self.entryUserName.get())
            UserMiddleName = str(self.enteryUserMiddleName.get())
            UserSurname = str(self.entryUserSurname.get())
            UserPassword = str(self.entryUserPassword.get())
            UserHouseNumber = str(self.entryUserHouseNumber.get())
            UserStreet = str(self.entryUserStreet.get())
            UserCity = str(self.entryUserCity.get())
            UserPostcode = str(self.entryUserPostcode.get())
            UserCA = str(self.checkedCa)
            UserSA = str(self.checkSa)
            UserCOD = str(self.checkCOd)
            UserMMA = str(self.checkMMa)
            UserIRA = str(self.checkIRa)
            
            UserPassword = data.hash_password(UserPassword)
            
            if self.flag == 1:
                UserStatus = 'user'
            elif self.flag == 2:
                UserStatus = 'admin'
                UserCA = False
                UserSA = False
                UserCOD = False
                UserMMA = False
                UserIRA = False
            else:
                print ('No option selected')
            
            self.entryUserName.delete(0, 'end')
            self.enteryUserMiddleName.delete(0, 'end')
            self.entryUserSurname.delete(0, 'end')
            self.entryUserPassword.delete(0, 'end')
            self.entryUserHouseNumber.delete(0, 'end')
            self.entryUserStreet.delete(0, 'end')
            self.entryUserHouseNumber.delete(0, 'end')
            self.entryUserCity.delete(0, 'end') 
            self.entryUserPostcode.delete(0, 'end')
            self.rb1.deselect()
            self.rb2.deselect()
            self.checkCa = False
            self.checkSa = False
            self.checkCOd = False
            self.checkMMa = False
            self.checkIRa = False
            self.checkCA.deselect()
            self.checkSA.deselect()
            self.checkCOD.deselect()
            self.checkMMA.deselect()
            self.checkIRA.deselect()
            
            datenow = str(datetime.datetime.now())
            data.dynamic_data_entry(UserName,UserMiddleName, UserSurname, UserPassword, UserHouseNumber,UserStreet, UserCity,UserPostcode,datenow , UserStatus, datenow)
            x = data.returnUserID(UserName,UserSurname,UserPassword,UserCity)
            y = str(x)
            x = ",()"
            for char in x:
                y = y.replace(char, "")
            data.insertIntoAccType(y,UserCA, UserSA, UserCOD, UserMMA,UserIRA)
            if(UserCA == 'True'):
                data.InsertIntoDepositAmmount(y,'0','CA','1','1')
            if(UserSA == 'True'):
                data.InsertIntoDepositAmmount(y,'0','SA','1','1')
            if(UserCOD == 'True'):
                data.InsertIntoDepositAmmount(y,'0','COD','1','1')
            if(UserMMA == 'True'):
                data.InsertIntoDepositAmmount(y,'0','MMA','1','1')
            if(UserIRA == 'True'):
                data.InsertIntoDepositAmmount(y,'0','IRA','1','1')
        
class AdminPageSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = 'nil'
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Data:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.labelIDFind = tk.Label(self, text = 'ID:')
        self.labelNameFind = tk.Label(self, text = 'Name:')
        self.labelSurnameFind = tk.Label(self, text = 'Surname:')
        self.labelHouseNumberFind = tk.Label(self, text = 'House number:')
        self.labelStreetFind = tk.Label(self, text = 'Street:')
        self.labelCityFind = tk.Label(self, text = 'City:')
        self.labelPostCodeFind = tk.Label(self, text = 'Post code:')
        self.labelAccountTypeFind = tk.Label(self, text = 'Account type:')
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entrySurnameFind = tk.Entry(self)
        self.entryHouseNumberFind = tk.Entry(self)
        self.entryStreetFind = tk.Entry(self)
        self.entryCityFind = tk.Entry(self)
        self.entryPostCodeFind = tk.Entry(self)
        self.entryAccountTypeFind = tk.Entry(self)
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelSurnameFind.place(x = 170,y = 95)
        self.labelHouseNumberFind.place(x = 170,y = 130)
        self.labelStreetFind.place(x = 170,y = 165)
        self.labelCityFind.place(x = 170,y = 200)
        self.labelPostCodeFind.place(x = 170,y = 235)
        self.labelAccountTypeFind.place(x = 170,y = 270)
        self.entryIDFind.place(x = 350,y = 25)
        self.entryNameFind.place(x = 350,y = 60)
        self.entrySurnameFind.place(x = 350,y = 95)
        self.entryHouseNumberFind.place(x = 350,y = 130)
        self.entryStreetFind.place(x = 350,y = 165)
        self.entryCityFind.place(x = 350,y = 200)
        self.entryPostCodeFind.place(x = 350,y = 235)
        self.entryAccountTypeFind.place(x = 350,y = 270)
        self.BtnGetDataFind.place(x = 180,y = 300)

        
        self.labelIdEditUser = tk.Label(self, text = 'ID:')
        self.labelNewNameEditUser = tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditUser = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditUser = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditUser = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditUser = tk.Label(self, text = 'New street:')
        self.labelNewCityEditUser = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditUser = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditUser = tk.Label(self, text = 'New account type:')
        self.entryIdEditUser = tk.Entry(self)
        self.entryNewNameEditUser = tk.Entry(self)
        self.entryNewMiddleNameEditUser = tk.Entry(self)
        self.entryNewSurnameEditUser = tk.Entry(self)
        self.entryNewHouseNumberEditUser = tk.Entry(self) 
        self.entryNewStreetEditUser = tk.Entry(self)
        self.entryNewCityEditUser = tk.Entry(self)
        self.entryNewPostCodeEditUser = tk.Entry(self)
        self.entryNewAccountTypeEditUser = tk.Entry(self)
        self.BtnUpdateDataEditUser = tk.Button(self,text ='Update', command = self.UpdateToUser)
        self.labelIdEditUser.place(x = 170,y = 25)
        self.labelNewNameEditUser.place(x = 170,y = 60)
        self.labelNewMiddleNameEditUser.place(x = 170,y = 95)
        self.labelNewSurnameEditUser.place(x = 170,y = 130)
        self.labelNewHouseNumberEditUser.place(x = 170,y = 165)
        self.labelNewStreetEditUser.place(x = 170,y = 200)
        self.labelNewCityEditUser.place(x = 170,y = 235)
        self.labelNewPostCodeEditUser.place(x = 170,y = 270)
        self.labelNewAccountTypeEditUser.place(x = 170,y = 305)
        self.entryIdEditUser.place(x = 350,y = 25)
        self.entryNewNameEditUser.place(x = 350,y = 60)
        self.entryNewMiddleNameEditUser.place(x = 350,y = 95)
        self.entryNewSurnameEditUser.place(x = 350,y = 130)
        self.entryNewHouseNumberEditUser.place(x = 350,y = 165)
        self.entryNewStreetEditUser.place(x = 350,y = 200)
        self.entryNewCityEditUser.place(x = 350,y = 235)
        self.entryNewPostCodeEditUser.place(x = 350,y = 270)
        self.entryNewAccountTypeEditUser.place(x = 350,y = 305)
        self.BtnUpdateDataEditUser.place(x = 180,y = 340)
        
        self.labelNewNameEditAdmin= tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditAdmin = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditAdmin = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditAdmin = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditAdmin = tk.Label(self, text = 'New street:')
        self.labelNewCityEditAdmin = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditAdmin = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditAdmin = tk.Label(self, text = 'New account type:')
        self.entryNewNameEditAdmin = tk.Entry(self)
        self.entryNewMiddleNameEditAdmin = tk.Entry(self)
        self.entryNewSurnameEditAdmin = tk.Entry(self)
        self.entryNewHouseNumberEditAdmin = tk.Entry(self) 
        self.entryNewStreetEditAdmin = tk.Entry(self)
        self.entryNewCityEditAdmin = tk.Entry(self)
        self.entryNewPostCodeEditAdmin = tk.Entry(self)
        self.entryNewAccountTypeEditAdmin = tk.Entry(self)
        self.BtnUpdateDataEditAdmin = tk.Button(self,text ='Update', command = self.UpdateToAdmin)
        self.labelNewNameEditAdmin.place(x = 170,y = 25)
        self.labelNewMiddleNameEditAdmin.place(x = 170,y = 60)
        self.labelNewSurnameEditAdmin.place(x = 170,y = 95)
        self.labelNewHouseNumberEditAdmin.place(x = 170,y = 130)
        self.labelNewStreetEditAdmin.place(x = 170,y = 165)
        self.labelNewCityEditAdmin.place(x = 170,y = 200)
        self.labelNewPostCodeEditAdmin.place(x = 170,y = 235)
        self.labelNewAccountTypeEditAdmin.place(x = 170,y = 270)
        self.entryNewNameEditAdmin.place(x = 350,y = 25)
        self.entryNewMiddleNameEditAdmin.place(x = 350,y = 60)
        self.entryNewSurnameEditAdmin.place(x = 350,y = 95)
        self.entryNewHouseNumberEditAdmin.place(x = 350,y = 130)
        self.entryNewStreetEditAdmin.place(x = 350,y = 165)
        self.entryNewCityEditAdmin.place(x = 350,y = 200)
        self.entryNewPostCodeEditAdmin.place(x = 350,y = 235)
        self.entryNewAccountTypeEditAdmin.place(x = 350,y = 270)
        self.BtnUpdateDataEditAdmin.place(x = 180,y = 305)
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.showAll = tk.Button(self.frm,text ='Show all', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.Find = tk.Button(self.frm,text ='Find user', command = self.FindList)
        self.Find.pack(expand=False, fill='x')
        
        self.EditUser = tk.Button(self.frm,text ='Edit user', command = self.EditUser)
        self.EditUser.pack(expand=False, fill='x')
        
        self.EditAdmin = tk.Button(self.frm,text ='Edit own admin status', command = self.EditAdminAcc)
        self.EditAdmin.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(AdminPageBase))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()          

    def EditUser(self):        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.tv.grid_forget()

        self.labelIdEditUser = tk.Label(self, text = 'ID:')
        self.labelNewNameEditUser = tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditUser = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditUser = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditUser = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditUser = tk.Label(self, text = 'New street:')
        self.labelNewCityEditUser = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditUser = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditUser = tk.Label(self, text = 'New account type:')
        
        self.entryIdEditUser = tk.Entry(self)
        self.entryNewNameEditUser = tk.Entry(self)
        self.entryNewMiddleNameEditUser = tk.Entry(self)
        self.entryNewSurnameEditUser = tk.Entry(self)
        self.entryNewHouseNumberEditUser = tk.Entry(self) 
        self.entryNewStreetEditUser = tk.Entry(self)
        self.entryNewCityEditUser = tk.Entry(self)
        self.entryNewPostCodeEditUser = tk.Entry(self)
        self.entryNewAccountTypeEditUser = tk.Entry(self)
        
        self.BtnUpdateDataEditUser = tk.Button(self,text ='Update', command = self.UpdateToUser)
        
        self.labelIdEditUser.place(x = 170,y = 25)
        self.labelNewNameEditUser.place(x = 170,y = 60)
        self.labelNewMiddleNameEditUser.place(x = 170,y = 95)
        self.labelNewSurnameEditUser.place(x = 170,y = 130)
        self.labelNewHouseNumberEditUser.place(x = 170,y = 165)
        self.labelNewStreetEditUser.place(x = 170,y = 200)
        self.labelNewCityEditUser.place(x = 170,y = 235)
        self.labelNewPostCodeEditUser.place(x = 170,y = 270)
        self.labelNewAccountTypeEditUser.place(x = 170,y = 305)
        
        self.entryIdEditUser.place(x = 350,y = 25)
        self.entryNewNameEditUser.place(x = 350,y = 60)
        self.entryNewMiddleNameEditUser.place(x = 350,y = 95)
        self.entryNewSurnameEditUser.place(x = 350,y = 130)
        self.entryNewHouseNumberEditUser.place(x = 350,y = 165)
        self.entryNewStreetEditUser.place(x = 350,y = 200)
        self.entryNewCityEditUser.place(x = 350,y = 235)
        self.entryNewPostCodeEditUser.place(x = 350,y = 270)
        self.entryNewAccountTypeEditUser.place(x = 350,y = 305)
        
        self.BtnUpdateDataEditUser.place(x = 180,y = 340)
    
    def UpdateToUser(self):    
        GotId = str(self.entryIdEditUser.get())
        GotNewName = str(self.entryNewNameEditUser.get())
        GotNewMiddleName = str(self.entryNewMiddleNameEditUser.get())
        GotNewSurname = str(self.entryNewSurnameEditUser.get())
        GotNewHouseNumber = str(self.entryNewHouseNumberEditUser.get())
        GotNewStreet = str(self.entryNewStreetEditUser.get())
        GotNewCity = str(self.entryNewCityEditUser.get())
        GotNewPostCode = str(self.entryNewPostCodeEditUser.get())
        GotNewAccountTypeDisable = str(self.entryNewAccountTypeEditUser.get())
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            
            if(userAccType.lower() == 'user' or userAccType.lower() == 'close' or userAccType.lower() == 'closed'):
                if(GotNewName == ''):
                    GotNewName = userName
                if(userMiddleName != '' and GotNewMiddleName == ''):
                    GotNewMiddleName = userMiddleName
                if(GotNewSurname == ''):
                    GotNewSurname = userSurname
                if(GotNewHouseNumber == ''):
                    GotNewHouseNumber = HouseNumber
                if(GotNewStreet == ''):
                    GotNewStreet = Street
                if(GotNewCity == ''):
                    GotNewCity = City
                if(GotNewPostCode == ''):
                    GotNewPostCode = PostCode
                if(GotNewAccountTypeDisable == ''):
                    GotNewAccountTypeDisable = PostCode
                
                data.updateUserAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable)
                
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessUserFromAdmin))
                b.invoke()
                
            else:
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorPageUserFromAdmin))
                b.invoke()
        
    def PrintAll(self):   
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserName', 'UserMiddleName','UserSurname','HouseNumber','Street','City','PostCode','UserCreationDate','UserAccType','UserLastLogin')
        self.tv.heading("#0", text='User ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserName', text='User name')
        self.tv.column('UserName', anchor='center', width=100)
        self.tv.heading('UserMiddleName', text='User middle name')
        self.tv.column('UserMiddleName', anchor='center', width=100)
        self.tv.heading('UserSurname', text='User surname')
        self.tv.column('UserSurname', anchor='center', width=100)
        self.tv.heading('HouseNumber', text='House number')
        self.tv.column('HouseNumber', anchor='center', width=100)
        self.tv.heading('Street', text='Street')
        self.tv.column('Street', anchor='center', width=100)
        self.tv.heading('City', text='City')
        self.tv.column('City', anchor='center', width=100)
        self.tv.heading('PostCode', text='Post code')
        self.tv.column('PostCode', anchor='center', width=100)
        self.tv.heading('UserCreationDate', text='User creation date')
        self.tv.column('UserCreationDate', anchor='center', width=100)
        self.tv.heading('UserAccType', text='User account type')
        self.tv.column('UserAccType', anchor='center', width=100)
        self.tv.heading('UserLastLogin', text='User last login')
        self.tv.column('UserLastLogin', anchor='center', width=100)
        self.treeview = self.tv
  
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime FROM Users")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime = operator.itemgetter(0,1,2,3,4,5,6,7,8,9,10)(row)
            self.treeview.insert('', 'end',text=userId,  values=(userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime))
           
    def FindList(self):        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIDFind = tk.Label(self, text = 'ID:')
        self.labelNameFind = tk.Label(self, text = 'Name:')
        self.labelSurnameFind = tk.Label(self, text = 'Surname:')
        self.labelHouseNumberFind = tk.Label(self, text = 'House number:')
        self.labelStreetFind = tk.Label(self, text = 'Street:')
        self.labelCityFind = tk.Label(self, text = 'City:')
        self.labelPostCodeFind = tk.Label(self, text = 'Post code:')
        self.labelAccountTypeFind = tk.Label(self, text = 'Account type:')
        
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entrySurnameFind = tk.Entry(self)
        self.entryHouseNumberFind = tk.Entry(self)
        self.entryStreetFind = tk.Entry(self)
        self.entryCityFind = tk.Entry(self)
        self.entryPostCodeFind = tk.Entry(self)
        self.entryAccountTypeFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelSurnameFind.place(x = 170,y = 95)
        self.labelHouseNumberFind.place(x = 170,y = 130)
        self.labelStreetFind.place(x = 170,y = 165)
        self.labelCityFind.place(x = 170,y = 200)
        self.labelPostCodeFind.place(x = 170,y = 235)
        self.labelAccountTypeFind.place(x = 170,y = 270)
                
        self.entryIDFind.place(x = 350,y = 25)
        self.entryNameFind.place(x = 350,y = 60)
        self.entrySurnameFind.place(x = 350,y = 95)
        self.entryHouseNumberFind.place(x = 350,y = 130)
        self.entryStreetFind.place(x = 350,y = 165)
        self.entryCityFind.place(x = 350,y = 200)
        self.entryPostCodeFind.place(x = 350,y = 235)
        self.entryAccountTypeFind.place(x = 350,y = 270)
        
        self.BtnGetDataFind.place(x = 180,y = 300)

    def ShowGottenData(self):  
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        GotID = str(self.entryIDFind.get())
        GotName = str(self.entryNameFind.get())
        GotSurname = str(self.entrySurnameFind.get())
        GotHouseNumber = str(self.entryHouseNumberFind.get())
        GotStreet = str(self.entryStreetFind.get())
        GotCity = str(self.entryCityFind.get())
        GotPostCode = str(self.entryPostCodeFind.get())
        GotAccountType = str(self.entryAccountTypeFind.get())
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.BtnGetData.place_forget()
                       
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserName', 'UserMiddleName','UserSurname','HouseNumber','Street','City','PostCode','UserAccType')
        self.tv.heading("#0", text='User ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserName', text='User name')
        self.tv.column('UserName', anchor='center', width=100)
        self.tv.heading('UserMiddleName', text='User middle name')
        self.tv.column('UserMiddleName', anchor='center', width=100)
        self.tv.heading('UserSurname', text='User surname')
        self.tv.column('UserSurname', anchor='center', width=100)
        self.tv.heading('HouseNumber', text='House number')
        self.tv.column('HouseNumber', anchor='center', width=100)
        self.tv.heading('Street', text='Street')
        self.tv.column('Street', anchor='center', width=100)
        self.tv.heading('City', text='City')
        self.tv.column('City', anchor='center', width=100)
        self.tv.heading('PostCode', text='Post code')
        self.tv.column('PostCode', anchor='center', width=100)
        self.tv.heading('UserAccType', text='User account type')
        self.tv.column('UserAccType', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' OR userName = '{}' OR userSurname = '{}' OR HouseNumber = '{}' OR Street = '{}' OR City = '{}' OR PostCode = '{}' OR userAccType = '{}'".format(GotID, GotName, GotSurname, GotHouseNumber, GotStreet, GotCity, GotPostCode, GotAccountType))
        lis = []
        for row in c.fetchall():
            lis.append(row)     
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=userId,  values=(userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType))

    def EditAdminAcc(self):  
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.tv.grid_forget()
        
        self.labelNewNameEditAdmin= tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditAdmin = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditAdmin = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditAdmin = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditAdmin = tk.Label(self, text = 'New street:')
        self.labelNewCityEditAdmin = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditAdmin = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditAdmin = tk.Label(self, text = 'New account type:')
        
        self.entryNewNameEditAdmin = tk.Entry(self)
        self.entryNewMiddleNameEditAdmin = tk.Entry(self)
        self.entryNewSurnameEditAdmin = tk.Entry(self)
        self.entryNewHouseNumberEditAdmin = tk.Entry(self) 
        self.entryNewStreetEditAdmin = tk.Entry(self)
        self.entryNewCityEditAdmin = tk.Entry(self)
        self.entryNewPostCodeEditAdmin = tk.Entry(self)
        self.entryNewAccountTypeEditAdmin = tk.Entry(self)
        
        self.BtnUpdateDataEditAdmin = tk.Button(self,text ='Update', command = self.UpdateToAdmin)
        
        self.labelNewNameEditAdmin.place(x = 170,y = 25)
        self.labelNewMiddleNameEditAdmin.place(x = 170,y = 60)
        self.labelNewSurnameEditAdmin.place(x = 170,y = 95)
        self.labelNewHouseNumberEditAdmin.place(x = 170,y = 130)
        self.labelNewStreetEditAdmin.place(x = 170,y = 165)
        self.labelNewCityEditAdmin.place(x = 170,y = 200)
        self.labelNewPostCodeEditAdmin.place(x = 170,y = 235)
        self.labelNewAccountTypeEditAdmin.place(x = 170,y = 270)
        
        self.entryNewNameEditAdmin.place(x = 350,y = 25)
        self.entryNewMiddleNameEditAdmin.place(x = 350,y = 60)
        self.entryNewSurnameEditAdmin.place(x = 350,y = 95)
        self.entryNewHouseNumberEditAdmin.place(x = 350,y = 130)
        self.entryNewStreetEditAdmin.place(x = 350,y = 165)
        self.entryNewCityEditAdmin.place(x = 350,y = 200)
        self.entryNewPostCodeEditAdmin.place(x = 350,y = 235)
        self.entryNewAccountTypeEditAdmin.place(x = 350,y = 270)
        
        self.BtnUpdateDataEditAdmin.place(x = 180,y = 305)
    
    def UpdateToAdmin(self):    
        GotId = str(GlIdUser)
        GotNewName = str(self.entryNewNameEditAdmin.get())
        GotNewMiddleName = str(self.entryNewMiddleNameEditAdmin.get())
        GotNewSurname = str(self.entryNewSurnameEditAdmin.get())
        GotNewHouseNumber = str(self.entryNewHouseNumberEditAdmin.get())
        GotNewStreet = str(self.entryNewStreetEditAdmin.get())
        GotNewCity = str(self.entryNewCityEditAdmin.get())
        GotNewPostCode = str(self.entryNewPostCodeEditAdmin.get())
        GotNewAccountTypeDisable = str(self.entryNewAccountTypeEditAdmin.get())
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            
            if(userAccType.lower() == 'admin'):
                if(GotNewName == ''):
                    GotNewName = userName
                if(userMiddleName != '' and GotNewMiddleName == ''):
                    GotNewMiddleName = userMiddleName
                if(GotNewSurname == ''):
                    GotNewSurname = userSurname
                if(GotNewHouseNumber == ''):
                    GotNewHouseNumber = HouseNumber
                if(GotNewStreet == ''):
                    GotNewStreet = Street
                if(GotNewCity == ''):
                    GotNewCity = City
                if(GotNewPostCode == ''):
                    GotNewPostCode = PostCode
                if(GotNewAccountTypeDisable == ''):
                    GotNewAccountTypeDisable = PostCode
                
                data.updateAdminAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable)

                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessAdmin))
                b.invoke()
                
            else:
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorPageAdmin))
                b.invoke()

        
class BankBasePage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'bank page')
        self.label.pack()
        
        buttonAddUser = ttk.Button(self, text = 'Add user', command = lambda: controller.show_frame(BankPage))
        buttonAddUser.pack()
        
        buttonSearch = tk.Button(self, text = 'Search users', command = lambda: controller.show_frame(BankPageSearch))
        buttonSearch.pack()
        
        buttonInvestments = tk.Button(self, text = 'Investments', command = lambda: controller.show_frame(InvestmentsPage))
        buttonInvestments.pack()
        
        buttonInterest = tk.Button(self, text = 'Interest rate', command = lambda: controller.show_frame(InterestRatePage))
        buttonInterest.pack()
        
        buttonManadgeLoadns = tk.Button(self,text ='Manadge loans', command = lambda: controller.show_frame(ManadgeLoadns))
        buttonManadgeLoadns.pack()
        
        buttonBankBalance = tk.Button(self, text = 'Bank balance', command = lambda: controller.show_frame(BankBalance))
        buttonBankBalance.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(LoginPage))
        buttonBack.pack()

class ManadgeLoadns(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Loans:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Investments:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        self.labelLoanIdAprove = tk.Label(self, text = 'Loan ID:')
        self.labelLoanStatusAprove = tk.Label(self, text = 'Insert aprove or reject:')
        self.labelLoanCommentAprove = tk.Label(self, text = 'Insert comment:')
        self.entryLoanIdAprove = tk.Entry(self)
        self.entryLoanStatusAprove = tk.Entry(self)
        self.entryLoanCommentAprove = tk.Entry(self)
        self.BtnChangeStatusAprove = tk.Button(self,text ='Add interest', command = self.InsertLoanStatusToDB)
        self.labelLoanIdAprove.place(x = 170,y = 25)
        self.labelLoanStatusAprove.place(x = 170,y = 60)
        self.labelLoanCommentAprove.place(x = 170,y = 95)
        self.entryLoanIdAprove.place(x = 305,y = 25)
        self.entryLoanStatusAprove.place(x = 305,y = 60)
        self.entryLoanCommentAprove.place(x = 305,y = 95)
        self.BtnChangeStatusAprove.place(x = 180,y = 130)
        
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        

        self.showAll = tk.Button(self.frm,text ='Show all loans', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.AllPendingLoans = tk.Button(self.frm,text ='Show all pending loans', command = self.PrintAllPending)
        self.AllPendingLoans.pack(expand=False, fill='x')
        
        self.AllApprovedLoans = tk.Button(self.frm,text ='Show all approved loans', command = self.PrintAllAproved)
        self.AllApprovedLoans.pack(expand=False, fill='x')
        
        self.AllRejectedLoans = tk.Button(self.frm,text ='Show all rejected loans', command = self.PrintAllRejected)
        self.AllRejectedLoans.pack(expand=False, fill='x')
        
        self.ManadgeInterestRate = tk.Button(self.frm,text ='Aprove/Rejected loan', command = self.LoanStatusAprove)
        self.ManadgeInterestRate.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(BankBasePage))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()          

    def PrintAll(self):       
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserLoanId', 'LoanStatus','LoanAmount','LoanMonthlyPlan','LoanComments', 'LoanChanged', 'LoanAdded', 'LoanRemoved')
        self.tv.heading("#0", text='Loand ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserLoanId', text='User ID')
        self.tv.column('UserLoanId', anchor='center', width=100)
        self.tv.heading('LoanStatus', text='Loan status')
        self.tv.column('LoanStatus', anchor='center', width=100)
        self.tv.heading('LoanAmount', text='Loan amount')
        self.tv.column('LoanAmount', anchor='center', width=100)
        self.tv.heading('LoanMonthlyPlan', text='Pay plan per month')
        self.tv.column('LoanMonthlyPlan', anchor='center', width=100)
        self.tv.heading('LoanComments', text='Loan comments')
        self.tv.column('LoanComments', anchor='center', width=100)
        self.tv.heading('LoanChanged', text='Changes made to the loan')
        self.tv.column('LoanChanged', anchor='center', width=100)
        self.tv.heading('LoanAdded', text='Loan added')
        self.tv.column('LoanAdded', anchor='center', width=100)
        self.tv.heading('LoanRemoved', text='Loan removed')
        self.tv.column('LoanRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Loans")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            LoandID,UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=LoandID,  values=(UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved))
 
    def PrintAllPending(self):       
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserLoanId', 'LoanStatus','LoanAmount','LoanMonthlyPlan','LoanComments', 'LoanChanged', 'LoanAdded', 'LoanRemoved')
        self.tv.heading("#0", text='Loand ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserLoanId', text='User ID')
        self.tv.column('UserLoanId', anchor='center', width=100)
        self.tv.heading('LoanStatus', text='Loan status')
        self.tv.column('LoanStatus', anchor='center', width=100)
        self.tv.heading('LoanAmount', text='Loan amount')
        self.tv.column('LoanAmount', anchor='center', width=100)
        self.tv.heading('LoanMonthlyPlan', text='Pay plan per month')
        self.tv.column('LoanMonthlyPlan', anchor='center', width=100)
        self.tv.heading('LoanComments', text='Loan comments')
        self.tv.column('LoanComments', anchor='center', width=100)
        self.tv.heading('LoanChanged', text='Changes made to the loan')
        self.tv.column('LoanChanged', anchor='center', width=100)
        self.tv.heading('LoanAdded', text='Loan added')
        self.tv.column('LoanAdded', anchor='center', width=100)
        self.tv.heading('LoanRemoved', text='Loan removed')
        self.tv.column('LoanRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Loans Where LoanStatus is 'pending'")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            LoandID,UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=LoandID,  values=(UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved))

    def PrintAllAproved(self):       
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserLoanId', 'LoanStatus','LoanAmount','LoanMonthlyPlan','LoanComments', 'LoanChanged', 'LoanAdded', 'LoanRemoved')
        self.tv.heading("#0", text='Loand ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserLoanId', text='User ID')
        self.tv.column('UserLoanId', anchor='center', width=100)
        self.tv.heading('LoanStatus', text='Loan status')
        self.tv.column('LoanStatus', anchor='center', width=100)
        self.tv.heading('LoanAmount', text='Loan amount')
        self.tv.column('LoanAmount', anchor='center', width=100)
        self.tv.heading('LoanMonthlyPlan', text='Pay plan per month')
        self.tv.column('LoanMonthlyPlan', anchor='center', width=100)
        self.tv.heading('LoanComments', text='Loan comments')
        self.tv.column('LoanComments', anchor='center', width=100)
        self.tv.heading('LoanChanged', text='Changes made to the loan')
        self.tv.column('LoanChanged', anchor='center', width=100)
        self.tv.heading('LoanAdded', text='Loan added')
        self.tv.column('LoanAdded', anchor='center', width=100)
        self.tv.heading('LoanRemoved', text='Loan removed')
        self.tv.column('LoanRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Loans Where LoanStatus is 'aproved'")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            LoandID,UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=LoandID,  values=(UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved))

    def PrintAllRejected(self):       
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserLoanId', 'LoanStatus','LoanAmount','LoanMonthlyPlan','LoanComments', 'LoanChanged', 'LoanAdded', 'LoanRemoved')
        self.tv.heading("#0", text='Loand ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserLoanId', text='User ID')
        self.tv.column('UserLoanId', anchor='center', width=100)
        self.tv.heading('LoanStatus', text='Loan status')
        self.tv.column('LoanStatus', anchor='center', width=100)
        self.tv.heading('LoanAmount', text='Loan amount')
        self.tv.column('LoanAmount', anchor='center', width=100)
        self.tv.heading('LoanMonthlyPlan', text='Pay plan per month')
        self.tv.column('LoanMonthlyPlan', anchor='center', width=100)
        self.tv.heading('LoanComments', text='Loan comments')
        self.tv.column('LoanComments', anchor='center', width=100)
        self.tv.heading('LoanChanged', text='Changes made to the loan')
        self.tv.column('LoanChanged', anchor='center', width=100)
        self.tv.heading('LoanAdded', text='Loan added')
        self.tv.column('LoanAdded', anchor='center', width=100)
        self.tv.heading('LoanRemoved', text='Loan removed')
        self.tv.column('LoanRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Loans Where LoanStatus is 'rejected'")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            LoandID,UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=LoandID,  values=(UserLoanId, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComments, LoanChanged, LoanAdded, LoanRemoved))


    def LoanStatusAprove(self):
        self.labelLoanIdAprove.place_forget()
        self.labelLoanStatusAprove.place_forget()
        self.labelLoanCommentAprove.place_forget()
        self.entryLoanIdAprove.place_forget()
        self.entryLoanStatusAprove.place_forget()
        self.entryLoanCommentAprove.place_forget()
        self.BtnChangeStatusAprove.place_forget()
        self.tv.grid_forget()

        self.labelLoanIdAprove = tk.Label(self, text = 'Loan ID:')
        self.labelLoanStatusAprove = tk.Label(self, text = 'Insert aprove or reject:')
        self.labelLoanCommentAprove = tk.Label(self, text = 'Insert comment:')
        
        self.entryLoanIdAprove = tk.Entry(self)
        self.entryLoanStatusAprove = tk.Entry(self)
        self.entryLoanCommentAprove = tk.Entry(self)
        
        self.BtnChangeStatusAprove = tk.Button(self,text ='Add interest', command = self.InsertLoanStatusToDB)
        
        self.labelLoanIdAprove.place(x = 170,y = 25)
        self.labelLoanStatusAprove.place(x = 170,y = 60)
        self.labelLoanCommentAprove.place(x = 170,y = 95)
                
        self.entryLoanIdAprove.place(x = 305,y = 25)
        self.entryLoanStatusAprove.place(x = 305,y = 60)
        self.entryLoanCommentAprove.place(x = 305,y = 95)
        
        self.BtnChangeStatusAprove.place(x = 180,y = 130)
        
    def InsertLoanStatusToDB(self):
        GotID = str(self.entryLoanIdAprove.get())
        GotStatus = str(self.entryLoanStatusAprove.get())
        GotComment = str(self.entryLoanCommentAprove.get())
        
        if(GotID != '' and GotStatus != '' and GotStatus != ''):
            if(GotStatus.lower() == 'aprove' or GotStatus.lower() == 'aproved'): 
                    if(GotStatus.lower() == 'aprove' or GotStatus.lower() == 'aproved'): 
                        GotStatus = 'aprove'
                    if(GotStatus.lower() == 'reject' or GotStatus.lower() == 'rejected' ):
                        GotStatus = 'reject'
                
                    data.insertIntoLoansStatus(GotID, GotStatus, GotComment)
                    b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessLoan))
                    b.invoke()
            else:
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorUpdatingLoans))
                b.invoke()
        else:
            b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorUpdatingLoans))
            b.invoke()

        
class BankPage(tk.Frame):
    #c1
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.status = ''
        
        self.labelPageName = tk.Label(self, text = 'bank page')
        self.labelAddUser = tk.Label(self, text = 'Add user')
        
        self.labelUserName = tk.Label(self, text = 'Enter user name:')
        self.labelUserMiddleName = tk.Label(self, text = 'Enter user middle name (optional)')
        self.labelUserSurname = tk.Label(self, text = 'Enter user surname:')
        self.labelUserPassword = tk.Label(self, text = 'Enter user password:')
        self.labelUserHouseNumber = tk.Label(self, text = 'Enter user house number:')
        self.labelUserStreet = tk.Label(self, text = 'Enter user street address:')
        self.labelUserCity = tk.Label(self, text = 'Enter user city:')
        self.labelUserPostcode = tk.Label(self, text = 'Enter user post code:')
        self.labelUserStatus = tk.Label(self, text = 'Enter user status:')
    
        self.entryUserName = tk.Entry(self)
        self.enteryUserMiddleName = tk.Entry(self)
        self.entryUserSurname = tk.Entry(self)
        self.entryUserPassword = tk.Entry(self)
        self.entryUserHouseNumber = tk.Entry(self)
        self.entryUserStreet = tk.Entry(self)
        self.entryUserCity = tk.Entry(self)
        self.entryUserPostcode = tk.Entry(self)
        
        self.rb1 = tk.Radiobutton(self,text='user', variable= self.status, 
                          value="user", command=self.selected1)

        self.rb2 = tk.Radiobutton(self,text='admin', variable=self.status, 
                          value="admin", command=self.selected2)
        
        self.checkedCa = False
        self.checkSa = False
        self.checkCOd = False
        self.checkMMa = False
        self.checkIRa = False
        
        self.buttonAddUser = ttk.Button(self, text = 'Add user to system', command = self.printInfo)
        self.buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankBasePage))
        
        self.checkCA = tk.Checkbutton(self, text="Checking Account",command = self.checkCA)
        self.checkSA = tk.Checkbutton(self, text="Savings account",command = self.checkSA)
        self.checkCOD = tk.Checkbutton(self, text="Certificate of Deposit (CD)",command = self.checkCOD)
        self.checkMMA = tk.Checkbutton(self, text="Money market account",command = self.checkMMA)
        self.checkIRA = tk.Checkbutton(self, text="Individual Retirement Accounts (IRAs)",command = self.checkIRA)
            
        self.flag = 0
        
        self.labelPageName.pack()
        self.labelAddUser.pack()
        
        self.labelUserName.pack()
        self.entryUserName.pack()
        
        self.labelUserMiddleName.pack()
        self.enteryUserMiddleName.pack()
        
        self.labelUserSurname.pack()
        self.entryUserSurname.pack()
        
        self.labelUserPassword.pack()
        self.entryUserPassword.pack()
        
        self.labelUserHouseNumber.pack()
        self.entryUserHouseNumber.pack()
        
        self.labelUserStreet.pack()
        self.entryUserStreet.pack()
        
        self.labelUserCity.pack()
        self.entryUserCity.pack()
        
        self.labelUserPostcode.pack()
        self.entryUserPostcode.pack()
        
        self.labelUserStatus.pack()
        self.rb1.pack()
        self.rb2.pack()
        
        self.checkCA.pack()
        self.checkSA.pack()
        self.checkCOD.pack()
        self.checkMMA.pack()
        self.checkIRA.pack()
        
        self.buttonAddUser.pack()
        self.buttonBack.pack()
        
    def checkCA(self):
        if (self.checkedCa == True):
            self.checkedCa = False
        elif(self.checkedCa == False):
            self.checkedCa = True
        
    def checkSA(self):
        if (self.checkSa == True):
            self.checkSa = False
        elif(self.checkSa == False):
            self.checkSa = True
            
    def checkCOD(self):
        if (self.checkCOd == True):
            self.checkCOd = False
        elif(self.checkCOd == False):
            self.checkCOd = True
            
    def checkMMA(self):
        if (self.checkMMa == True):
            self.checkMMa = False
        elif(self.checkMMa == False):
            self.checkMMa = True
            
    def checkIRA(self):
        if (self.checkIRa == True):
            self.checkIRa = False
        elif(self.checkIRa == False):
            self.checkIRa = True
       
    def selected1(self):
        self.flag = 1
        
    def selected2(self):
        self.flag = 2
            
    def printInfo(self):
        UserName = str(self.entryUserName.get())
        UserMiddleName = str(self.enteryUserMiddleName.get())
        UserSurname = str(self.entryUserSurname.get())
        UserPassword = str(self.entryUserPassword.get())
        UserHouseNumber = str(self.entryUserHouseNumber.get())
        UserStreet = str(self.entryUserStreet.get())
        UserCity = str(self.entryUserCity.get())
        UserPostcode = str(self.entryUserPostcode.get())
        UserCA = str(self.checkedCa)
        UserSA = str(self.checkSa)
        UserCOD = str(self.checkCOd)
        UserMMA = str(self.checkMMa)
        UserIRA = str(self.checkIRa)
        
        UserPassword = data.hash_password(UserPassword)
        
        if self.flag == 1:
            UserStatus = 'user'
        elif self.flag == 2:
            UserStatus = 'admin'
            UserCA = False
            UserSA = False
            UserCOD = False
            UserMMA = False
            UserIRA = False
        else:
            print ('No option selected')
        
        self.entryUserName.delete(0, 'end')
        self.enteryUserMiddleName.delete(0, 'end')
        self.entryUserSurname.delete(0, 'end')
        self.entryUserPassword.delete(0, 'end')
        self.entryUserHouseNumber.delete(0, 'end')
        self.entryUserStreet.delete(0, 'end')
        self.entryUserHouseNumber.delete(0, 'end')
        self.entryUserCity.delete(0, 'end') 
        self.entryUserPostcode.delete(0, 'end')
        self.rb1.deselect()
        self.rb2.deselect()
        self.checkCa = False
        self.checkSa = False
        self.checkCOd = False
        self.checkMMa = False
        self.checkIRa = False
        self.checkCA.deselect()
        self.checkSA.deselect()
        self.checkCOD.deselect()
        self.checkMMA.deselect()
        self.checkIRA.deselect()
        
        datenow = str(datetime.datetime.now())
        data.dynamic_data_entry(UserName,UserMiddleName, UserSurname, UserPassword, UserHouseNumber,UserStreet, UserCity,UserPostcode,datenow , UserStatus, datenow)
        x = data.returnUserID(UserName,UserSurname,UserPassword,UserCity)
        y = str(x)
        x = ",()"
        for char in x:
            y = y.replace(char, "")
        data.insertIntoAccType(y,UserCA, UserSA, UserCOD, UserMMA,UserIRA)
        if(UserCA == 'True'):
            data.InsertIntoDepositAmmount(y,'0','CA','1','1')
        if(UserSA == 'True'):
            data.InsertIntoDepositAmmount(y,'0','SA','1','1')
        if(UserCOD == 'True'):
            data.InsertIntoDepositAmmount(y,'0','COD','1','1')
        if(UserMMA == 'True'):
            data.InsertIntoDepositAmmount(y,'0','MMA','1','1')
        if(UserIRA == 'True'):
            data.InsertIntoDepositAmmount(y,'0','IRA','1','1')
        
class BankPageSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Data:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.labelIDFind = tk.Label(self, text = 'ID:')
        self.labelNameFind = tk.Label(self, text = 'Name:')
        self.labelSurnameFind = tk.Label(self, text = 'Surname:')
        self.labelHouseNumberFind = tk.Label(self, text = 'House number:')
        self.labelStreetFind = tk.Label(self, text = 'Street:')
        self.labelCityFind = tk.Label(self, text = 'City:')
        self.labelPostCodeFind = tk.Label(self, text = 'Post code:')
        self.labelAccountTypeFind = tk.Label(self, text = 'Account type:')
        self.BtnGetDataFind = tk.Button(self,text ='test', command = self.ShowGottenData)
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entrySurnameFind = tk.Entry(self)
        self.entryHouseNumberFind = tk.Entry(self)
        self.entryStreetFind = tk.Entry(self)
        self.entryCityFind = tk.Entry(self)
        self.entryPostCodeFind = tk.Entry(self)
        self.entryAccountTypeFind = tk.Entry(self) 
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelSurnameFind.place(x = 170,y = 130)
        self.labelHouseNumberFind.place(x = 170,y = 165)
        self.labelStreetFind.place(x = 170,y = 200)
        self.labelCityFind.place(x = 170,y = 235)
        self.labelPostCodeFind.place(x = 170,y = 270)
        self.labelAccountTypeFind.place(x = 170,y = 305)
        self.entryIDFind.place(x = 350,y = 25)
        self.entryNameFind.place(x = 350,y = 60)
        self.entrySurnameFind.place(x = 350,y = 130)
        self.entryHouseNumberFind.place(x = 350,y = 165)
        self.entryStreetFind.place(x = 350,y = 200)
        self.entryCityFind.place(x = 350,y = 235)
        self.entryPostCodeFind.place(x = 350,y = 270)
        self.entryAccountTypeFind.place(x = 350,y = 305)  
        self.BtnGetDataFind.place(x = 180,y = 355)
        
        self.labelIdEditUser = tk.Label(self, text = 'ID:')
        self.labelNewNameEditUser = tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditUser = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditUser = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditUser= tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditUser = tk.Label(self, text = 'New street:')
        self.labelNewCityEditUser = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditUser = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditUser = tk.Label(self, text = 'New account type:')
        self.entryIdEditUser = tk.Entry(self)
        self.entryNewNameEditUser = tk.Entry(self)
        self.entryNewMiddleNameEditUser = tk.Entry(self)
        self.entryNewSurnameEditUser = tk.Entry(self)
        self.entryNewHouseNumberEditUser = tk.Entry(self) 
        self.entryNewStreetEditUser = tk.Entry(self)
        self.entryNewCityEditUser = tk.Entry(self)
        self.entryNewPostCodeEditUser = tk.Entry(self)
        self.entryNewAccountTypeEditUser = tk.Entry(self)
        
        self.labelNewInterestIdEditUser = tk.Label(self, text = 'New interest id:')
        self.labelNewOverdraftIdEditUser = tk.Label(self, text = 'New overdraft id:') 
        self.entryNewInterestIdEditUser = tk.Entry(self)
        self.entryNewOverdraftIdEditUser = tk.Entry(self)
        
        self.BtnUpdateDataEditUser = tk.Button(self,text ='Update', command = self.UpdateToUser)
        self.labelIdEditUser.place(x = 170,y = 25)
        self.labelNewNameEditUser.place(x = 170,y = 60)
        self.labelNewMiddleNameEditUser.place(x = 170,y = 95)
        self.labelNewSurnameEditUser.place(x = 170,y = 130)
        self.labelNewHouseNumberEditUser.place(x = 170,y = 165)
        self.labelNewStreetEditUser.place(x = 170,y = 200)
        self.labelNewCityEditUser.place(x = 170,y = 235)
        self.labelNewPostCodeEditUser.place(x = 170,y = 270)
        self.labelNewAccountTypeEditUser.place(x = 170,y = 305)
        self.entryIdEditUser.place(x = 350,y = 25)
        self.entryNewNameEditUser.place(x = 350,y = 60)
        self.entryNewMiddleNameEditUser.place(x = 350,y = 95)
        self.entryNewSurnameEditUser.place(x = 350,y = 130)
        self.entryNewHouseNumberEditUser.place(x = 350,y = 165)
        self.entryNewStreetEditUser.place(x = 350,y = 200)
        self.entryNewCityEditUser.place(x = 350,y = 235)
        self.entryNewPostCodeEditUser.place(x = 350,y = 270)
        self.entryNewAccountTypeEditUser.place(x = 350,y = 305)
        self.BtnUpdateDataEditUser.place(x = 180,y = 340)
        
        self.labelIdEditAdmin = tk.Label(self, text = 'ID:')
        self.labelNewNameEditAdmin = tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditAdmin = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditAdmin = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditAdmin = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditAdmin = tk.Label(self, text = 'New street:')
        self.labelNewCityEditAdmin = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditAdmin = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditAdmin = tk.Label(self, text = 'New account type:')
        self.entryIdEditAdmin = tk.Entry(self)
        self.entryNewNameEditAdmin = tk.Entry(self)
        self.entryNewMiddleNameEditAdmin = tk.Entry(self)
        self.entryNewSurnameEditAdmin = tk.Entry(self)
        self.entryNewHouseNumberEditAdmin = tk.Entry(self) 
        self.entryNewStreetEditAdmin = tk.Entry(self)
        self.entryNewCityEditAdmin = tk.Entry(self)
        self.entryNewPostCodeEditAdmin = tk.Entry(self)
        self.entryNewAccountTypeEditAdmin = tk.Entry(self)
        self.BtnUpdateDataEditAdmin = tk.Button(self,text ='Update', command = self.UpdateToAdmin)
        self.labelIdEditAdmin.place(x = 170,y = 25)
        self.labelNewNameEditAdmin.place(x = 170,y = 60)
        self.labelNewMiddleNameEditAdmin.place(x = 170,y = 95)
        self.labelNewSurnameEditAdmin.place(x = 170,y = 130)
        self.labelNewHouseNumberEditAdmin.place(x = 170,y = 165)
        self.labelNewStreetEditAdmin.place(x = 170,y = 200)
        self.labelNewCityEditAdmin.place(x = 170,y = 235)
        self.labelNewPostCodeEditAdmin.place(x = 170,y = 270)
        self.labelNewAccountTypeEditAdmin.place(x = 170,y = 305)
        self.entryIdEditAdmin.place(x = 350,y = 25)
        self.entryNewNameEditAdmin.place(x = 350,y = 60)
        self.entryNewMiddleNameEditAdmin.place(x = 350,y = 95)
        self.entryNewSurnameEditAdmin.place(x = 350,y = 130)
        self.entryNewHouseNumberEditAdmin.place(x = 350,y = 165)
        self.entryNewStreetEditAdmin.place(x = 350,y = 200)
        self.entryNewCityEditAdmin.place(x = 350,y = 235)
        self.entryNewPostCodeEditAdmin.place(x = 350,y = 270)
        self.entryNewAccountTypeEditAdmin.place(x = 350,y = 305)
        self.BtnUpdateDataEditAdmin.place(x = 180,y = 340)
        
        self.labelIdRemoveUser = tk.Label(self, text = 'ID:')
        self.entryIdRemoveUser = tk.Entry(self)
        self.BtnRemoveUser = tk.Button(self,text ='Remove user', command = self.RemoveUserFromDB)

        self.labelIdRemoveAdmin = tk.Label(self, text = 'ID:')
        self.entryIdRemoveAdmin = tk.Entry(self)
        self.BtnRemoveAdmin = tk.Button(self,text ='Remove admin', command = self.RemoveAdminFromDB)
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()

        self.showAll = tk.Button(self.frm,text ='Show all', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.Find = tk.Button(self.frm,text ='Find user', command = self.FindList)
        self.Find.pack(expand=False, fill='x')
        
        self.btnEditUser = tk.Button(self.frm,text ='Edit user', command = self.EditUser)
        self.btnEditUser.pack(expand=False, fill='x')
        
        self.btnRemoveUser = tk.Button(self.frm,text ='Remove user', command = self.RemoveUser)
        self.btnRemoveUser.pack(expand=False, fill='x')
        
        self.btnEditAdmin = tk.Button(self.frm,text ='Edit admin', command = self.EditAdmin)
        self.btnEditAdmin.pack(expand=False, fill='x')
        
        self.btnRemoveAdmin = tk.Button(self.frm,text ='Remove admin', command = self.RemoveAdmin)
        self.btnRemoveAdmin.pack(expand=False, fill='x')
                
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(BankBasePage))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()     
            
    def RemoveUser(self):
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIdRemoveUser = tk.Label(self, text = 'ID:')
        
        self.entryIdRemoveUser = tk.Entry(self)
        
        self.BtnRemoveUser = tk.Button(self,text ='Remove user', command = self.RemoveUserFromDB)
        
        self.labelIdRemoveUser.place(x = 170,y = 25)
        self.entryIdRemoveUser.place(x = 200,y = 25)
        self.BtnRemoveUser.place(x = 170,y = 60)
         
    def RemoveUserFromDB(self):        
        GotId = str(self.entryIdRemoveUser.get())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()        
        c.execute("SELECT userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userAccType = operator.itemgetter(0)(row)
            
            if(userAccType.lower() == 'user'):
                c.execute("DELETE FROM  Balance WHERE  Balance.userId like {} ".format(GotId))
                c.execute("DELETE FROM  AccType WHERE  AccType.userId like {} ".format(GotId))
                c.execute("DELETE FROM  Appointments WHERE  Appointments.userId like {} ".format(GotId))
                c.execute("DELETE FROM  Loans WHERE  Loans.UserLoanId like {} ".format(GotId))
                c.execute("DELETE FROM  UserInvestments WHERE  UserInvestments.userID like {} ".format(GotId))
                c.execute("DELETE FROM  UserInvestments WHERE  UserInvestments.userID like {} ".format(GotId))

                c.execute("DELETE FROM  Users WHERE  Users.userId like {} ".format(GotId))

        conn.commit()
        c.close()
        conn.close()
        
    def RemoveAdmin(self):
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIdRemoveAdmin = tk.Label(self, text = 'ID:')
        
        self.entryIdRemoveAdmin = tk.Entry(self)
        
        self.BtnRemoveAdmin = tk.Button(self,text ='Remove admin', command = self.RemoveAdminFromDB)
        
        self.labelIdRemoveAdmin.place(x = 170,y = 25)
        self.entryIdRemoveAdmin.place(x = 200,y = 25)
        self.BtnRemoveAdmin.place(x = 170,y = 60)
         
    def RemoveAdminFromDB(self):
        GotId = str(self.entryIdRemoveAdmin.get())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("SELECT userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userAccType = operator.itemgetter(0)(row)
            
            if(userAccType.lower() == 'admin'):
                print('test')
                c.execute("DELETE FROM  Balance WHERE  Balance.userId like {} ".format(GotId))
                c.execute("DELETE FROM  AccType WHERE  AccType.userId like {} ".format(GotId))
                c.execute("DELETE FROM  Appointments WHERE  Appointments.userId like {} ".format(GotId))
                c.execute("DELETE FROM  Loans WHERE  Loans.UserLoanId like {} ".format(GotId))
                c.execute("DELETE FROM  UserInvestments WHERE  UserInvestments.userID like {} ".format(GotId))
                c.execute("DELETE FROM  UserInvestments WHERE  UserInvestments.userID like {} ".format(GotId))

                c.execute("DELETE FROM  Users WHERE  Users.userId like {} ".format(GotId))

        conn.commit()
        c.close()
        conn.close()
    
    def EditUser(self):
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()

        self.labelIdEditUser = tk.Label(self, text = 'ID:')
        self.labelNewNameEditUser = tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditUser = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditUser = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditUser = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditUser = tk.Label(self, text = 'New street:')
        self.labelNewCityEditUser = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditUser = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditUser = tk.Label(self, text = 'New account type:')
        self.labelNewInterestIdEditUser = tk.Label(self, text = 'New interest id:')
        self.labelNewOverdraftIdEditUser = tk.Label(self, text = 'New overdraft id:')
        
        self.entryIdEditUser = tk.Entry(self)
        self.entryNewNameEditUser = tk.Entry(self)
        self.entryNewMiddleNameEditUser = tk.Entry(self)
        self.entryNewSurnameEditUser = tk.Entry(self)
        self.entryNewHouseNumberEditUser = tk.Entry(self) 
        self.entryNewStreetEditUser = tk.Entry(self)
        self.entryNewCityEditUser = tk.Entry(self)
        self.entryNewPostCodeEditUser = tk.Entry(self)
        self.entryNewAccountTypeEditUser = tk.Entry(self)
        self.entryNewInterestIdEditUser = tk.Entry(self)
        self.entryNewOverdraftIdEditUser = tk.Entry(self)
        
        self.BtnUpdateDataEditUser = tk.Button(self,text ='Update', command = self.UpdateToUser)
        
        self.labelIdEditUser.place(x = 170,y = 25)
        self.labelNewNameEditUser.place(x = 170,y = 60)
        self.labelNewMiddleNameEditUser.place(x = 170,y = 95)
        self.labelNewSurnameEditUser.place(x = 170,y = 130)
        self.labelNewHouseNumberEditUser.place(x = 170,y = 165)
        self.labelNewStreetEditUser.place(x = 170,y = 200)
        self.labelNewCityEditUser.place(x = 170,y = 235)
        self.labelNewPostCodeEditUser.place(x = 170,y = 270)
        self.labelNewAccountTypeEditUser.place(x = 170,y = 305)
        self.labelNewInterestIdEditUser.place(x = 170,y = 340)
        self.labelNewOverdraftIdEditUser.place(x = 170,y = 375)
        
        self.entryIdEditUser.place(x = 350,y = 25)
        self.entryNewNameEditUser.place(x = 350,y = 60)
        self.entryNewMiddleNameEditUser.place(x = 350,y = 95)
        self.entryNewSurnameEditUser.place(x = 350,y = 130)
        self.entryNewHouseNumberEditUser.place(x = 350,y = 165)
        self.entryNewStreetEditUser.place(x = 350,y = 200)
        self.entryNewCityEditUser.place(x = 350,y = 235)
        self.entryNewPostCodeEditUser.place(x = 350,y = 270)
        self.entryNewAccountTypeEditUser.place(x = 350,y = 305)
        self.entryNewInterestIdEditUser.place(x = 350,y = 340)
        self.entryNewOverdraftIdEditUser.place(x = 350,y = 375)
        
        self.BtnUpdateDataEditUser.place(x = 180,y = 410)
    
    def UpdateToUser(self):    
        GotId = str(self.entryIdEditUser.get())
        GotNewName = str(self.entryNewNameEditUser.get())
        GotNewMiddleName = str(self.entryNewMiddleNameEditUser.get())
        GotNewSurname = str(self.entryNewSurnameEditUser.get())
        GotNewHouseNumber = str(self.entryNewHouseNumberEditUser.get())
        GotNewStreet = str(self.entryNewStreetEditUser.get())
        GotNewCity = str(self.entryNewCityEditUser.get())
        GotNewPostCode = str(self.entryNewPostCodeEditUser.get())
        GotNewAccountTypeDisable = str(self.entryNewAccountTypeEditUser.get())
        GotNewInterest = str(self.entryNewInterestIdEditUser.get())
        GotNewOverdraft = str(self.entryNewOverdraftIdEditUser.get())
        
        print(GotNewInterest, GotNewOverdraft)
        

        
        c.execute("SELECT InterestId, OverdraftID From balance WHERE  Balance.userId is {}".format(GotId))
        for row in c.fetchall():
            interestId, overdraftId = operator.itemgetter(0,1)(row)
        
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
        
        print(userAccType)
        if(userAccType.lower() == 'user' or userAccType.lower() == 'close' or userAccType.lower() == 'closed'):
                print('test')
                if(GotNewName == ''):
                    GotNewName = userName
                if(userMiddleName != '' and GotNewMiddleName == ''):
                    GotNewMiddleName = userMiddleName
                if(GotNewSurname == ''):
                    GotNewSurname = userSurname
                if(GotNewHouseNumber == ''):
                    GotNewHouseNumber = HouseNumber
                if(GotNewStreet == ''):
                    GotNewStreet = Street
                if(GotNewCity == ''):
                    GotNewCity = City
                if(GotNewPostCode == ''):
                    GotNewPostCode = PostCode
                if(GotNewAccountTypeDisable == ''):
                    GotNewAccountTypeDisable = PostCode
                if(GotNewInterest == ''):
                    GotNewInterest = interestId
                if(GotNewOverdraft == ''):
                    GotNewOverdraft = overdraftId
                
                data.updateUserAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable)
                data.updateBalanceAcc(GotId,GotNewInterest,GotNewOverdraft)
                
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessUser))
                b.invoke()
                
        else:
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorPageUser))
                b.invoke()
               
    def EditAdmin(self):
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()

        self.labelIdEditAdmin= tk.Label(self, text = 'ID:')
        self.labelNewNameEditAdmin= tk.Label(self, text = 'New name:')
        self.labelNewMiddleNameEditAdmin = tk.Label(self, text = 'New middle name:')
        self.labelNewSurnameEditAdmin = tk.Label(self, text = 'New surname:')
        self.labelNewHouseNumberEditAdmin = tk.Label(self, text = 'New house number:')
        self.labelNewStreetEditAdmin = tk.Label(self, text = 'New street:')
        self.labelNewCityEditAdmin = tk.Label(self, text = 'New city:')
        self.labelNewPostCodeEditAdmin = tk.Label(self, text = 'New post code:')
        self.labelNewAccountTypeEditAdmin = tk.Label(self, text = 'New account type:')
        
        self.entryIdEditAdmin = tk.Entry(self)
        self.entryNewNameEditAdmin = tk.Entry(self)
        self.entryNewMiddleNameEditAdmin = tk.Entry(self)
        self.entryNewSurnameEditAdmin = tk.Entry(self)
        self.entryNewHouseNumberEditAdmin = tk.Entry(self) 
        self.entryNewStreetEditAdmin = tk.Entry(self)
        self.entryNewCityEditAdmin = tk.Entry(self)
        self.entryNewPostCodeEditAdmin = tk.Entry(self)
        self.entryNewAccountTypeEditAdmin = tk.Entry(self)
        
        self.BtnUpdateDataEditAdmin = tk.Button(self,text ='Update', command = self.UpdateToAdmin)
        
        self.labelIdEditAdmin.place(x = 170,y = 25)
        self.labelNewNameEditAdmin.place(x = 170,y = 60)
        self.labelNewMiddleNameEditAdmin.place(x = 170,y = 95)
        self.labelNewSurnameEditAdmin.place(x = 170,y = 130)
        self.labelNewHouseNumberEditAdmin.place(x = 170,y = 165)
        self.labelNewStreetEditAdmin.place(x = 170,y = 200)
        self.labelNewCityEditAdmin.place(x = 170,y = 235)
        self.labelNewPostCodeEditAdmin.place(x = 170,y = 270)
        self.labelNewAccountTypeEditAdmin.place(x = 170,y = 305)
        
        self.entryIdEditAdmin.place(x = 350,y = 25)
        self.entryNewNameEditAdmin.place(x = 350,y = 60)
        self.entryNewMiddleNameEditAdmin.place(x = 350,y = 95)
        self.entryNewSurnameEditAdmin.place(x = 350,y = 130)
        self.entryNewHouseNumberEditAdmin.place(x = 350,y = 165)
        self.entryNewStreetEditAdmin.place(x = 350,y = 200)
        self.entryNewCityEditAdmin.place(x = 350,y = 235)
        self.entryNewPostCodeEditAdmin.place(x = 350,y = 270)
        self.entryNewAccountTypeEditAdmin.place(x = 350,y = 305)
        
        self.BtnUpdateDataEditAdmin.place(x = 180,y = 340)
    
    def UpdateToAdmin(self):    
        GotId = str(self.entryIdEditAdmin.get())
        GotNewName = str(self.entryNewNameEditAdmin.get())
        GotNewMiddleName = str(self.entryNewMiddleNameEditAdmin.get())
        GotNewSurname = str(self.entryNewSurnameEditAdmin.get())
        GotNewHouseNumber = str(self.entryNewHouseNumberEditAdmin.get())
        GotNewStreet = str(self.entryNewStreetEditAdmin.get())
        GotNewCity = str(self.entryNewCityEditAdmin.get())
        GotNewPostCode = str(self.entryNewPostCodeEditAdmin.get())
        GotNewAccountTypeDisable = str(self.entryNewAccountTypeEditAdmin.get())
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' ".format(GotId))
        lis = []
        for row in c.fetchall():
            lis.append(row)
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            
            if(userAccType.lower() == 'admin'):
                if(GotNewName == ''):
                    GotNewName = userName
                if(userMiddleName != '' and GotNewMiddleName == ''):
                    GotNewMiddleName = userMiddleName
                if(GotNewSurname == ''):
                    GotNewSurname = userSurname
                if(GotNewHouseNumber == ''):
                    GotNewHouseNumber = HouseNumber
                if(GotNewStreet == ''):
                    GotNewStreet = Street
                if(GotNewCity == ''):
                    GotNewCity = City
                if(GotNewPostCode == ''):
                    GotNewPostCode = PostCode
                if(GotNewAccountTypeDisable == ''):
                    GotNewAccountTypeDisable = PostCode
                
                data.updateAdminAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable)

                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(UpdateSucessAdmin))
                b.invoke()
                
            else:
                b = tk.Button(self, text = '',command = lambda: self.controller.show_frame(ErrorPageAdmin))
                b.invoke()

    def PrintAll(self):   
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserName', 'UserMiddleName','UserSurname','HouseNumber','Street','City','PostCode','UserCreationDate','UserAccType','UserLastLogin')
        self.tv.heading("#0", text='User ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserName', text='User name')
        self.tv.column('UserName', anchor='center', width=100)
        self.tv.heading('UserMiddleName', text='User middle name')
        self.tv.column('UserMiddleName', anchor='center', width=100)
        self.tv.heading('UserSurname', text='User surname')
        self.tv.column('UserSurname', anchor='center', width=100)
        self.tv.heading('HouseNumber', text='House number')
        self.tv.column('HouseNumber', anchor='center', width=100)
        self.tv.heading('Street', text='Street')
        self.tv.column('Street', anchor='center', width=100)
        self.tv.heading('City', text='City')
        self.tv.column('City', anchor='center', width=100)
        self.tv.heading('PostCode', text='Post code')
        self.tv.column('PostCode', anchor='center', width=100)
        self.tv.heading('UserCreationDate', text='User creation date')
        self.tv.column('UserCreationDate', anchor='center', width=100)
        self.tv.heading('UserAccType', text='User account type')
        self.tv.column('UserAccType', anchor='center', width=100)
        self.tv.heading('UserLastLogin', text='User last login')
        self.tv.column('UserLastLogin', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime FROM Users")
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime = operator.itemgetter(0,1,2,3,4,5,6,7,8,9,10)(row)
            self.treeview.insert('', 'end',text=userId,  values=(userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime))
           
    def FindList(self):    
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIDFind = tk.Label(self, text = 'ID:')
        self.labelNameFind = tk.Label(self, text = 'Name:')
        self.labelSurnameFind = tk.Label(self, text = 'Surname:')
        self.labelHouseNumberFind = tk.Label(self, text = 'House number:')
        self.labelStreetFind = tk.Label(self, text = 'Street:')
        self.labelCityFind = tk.Label(self, text = 'City:')
        self.labelPostCodeFind = tk.Label(self, text = 'Post code:')
        self.labelAccountTypeFind = tk.Label(self, text = 'Account type:')
        
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entrySurnameFind = tk.Entry(self)
        self.entryHouseNumberFind = tk.Entry(self)
        self.entryStreetFind = tk.Entry(self)
        self.entryCityFind = tk.Entry(self)
        self.entryPostCodeFind = tk.Entry(self)
        self.entryAccountTypeFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelSurnameFind.place(x = 170,y = 95)
        self.labelHouseNumberFind.place(x = 170,y = 130)
        self.labelStreetFind.place(x = 170,y = 165)
        self.labelCityFind.place(x = 170,y = 200)
        self.labelPostCodeFind.place(x = 170,y = 235)
        self.labelAccountTypeFind.place(x = 170,y = 270)
                
        self.entryIDFind.place(x = 350,y = 25)
        self.entryNameFind.place(x = 350,y = 60)
        self.entrySurnameFind.place(x = 350,y = 95)
        self.entryHouseNumberFind.place(x = 350,y = 130)
        self.entryStreetFind.place(x = 350,y = 165)
        self.entryCityFind.place(x = 350,y = 200)
        self.entryPostCodeFind.place(x = 350,y = 235)
        self.entryAccountTypeFind.place(x = 350,y = 270)
        
        self.BtnGetDataFind.place(x = 180,y = 300)

    def ShowGottenData(self):       
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelSurnameFind.place_forget()
        self.labelHouseNumberFind.place_forget()
        self.labelStreetFind.place_forget()
        self.labelCityFind.place_forget()
        self.labelPostCodeFind.place_forget()
        self.labelAccountTypeFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entrySurnameFind.place_forget()
        self.entryHouseNumberFind.place_forget()
        self.entryStreetFind.place_forget()
        self.entryCityFind.place_forget()
        self.entryPostCodeFind.place_forget()
        self.entryAccountTypeFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelIdEditUser.place_forget()
        self.labelNewNameEditUser.place_forget()
        self.labelNewMiddleNameEditUser.place_forget()
        self.labelNewSurnameEditUser.place_forget()
        self.labelNewHouseNumberEditUser.place_forget()
        self.labelNewStreetEditUser.place_forget()
        self.labelNewCityEditUser.place_forget()
        self.labelNewPostCodeEditUser.place_forget()
        self.labelNewAccountTypeEditUser.place_forget()
        self.entryIdEditUser.place_forget()
        self.entryNewNameEditUser.place_forget()
        self.entryNewMiddleNameEditUser.place_forget()
        self.entryNewSurnameEditUser.place_forget()
        self.entryNewHouseNumberEditUser.place_forget()
        self.entryNewStreetEditUser.place_forget()
        self.entryNewCityEditUser.place_forget()
        self.entryNewPostCodeEditUser.place_forget()
        self.entryNewAccountTypeEditUser.place_forget()
        self.labelNewInterestIdEditUser.place_forget()
        self.labelNewOverdraftIdEditUser.place_forget()
        self.entryNewInterestIdEditUser.place_forget()
        self.entryNewOverdraftIdEditUser.place_forget()
        self.BtnUpdateDataEditUser.place_forget()
        
        self.labelIdEditAdmin.place_forget()
        self.labelNewNameEditAdmin.place_forget()
        self.labelNewMiddleNameEditAdmin.place_forget()
        self.labelNewSurnameEditAdmin.place_forget()
        self.labelNewHouseNumberEditAdmin.place_forget()
        self.labelNewStreetEditAdmin.place_forget()
        self.labelNewCityEditAdmin.place_forget()
        self.labelNewPostCodeEditAdmin.place_forget()
        self.labelNewAccountTypeEditAdmin.place_forget()
        self.entryIdEditAdmin.place_forget()
        self.entryNewNameEditAdmin.place_forget()
        self.entryNewMiddleNameEditAdmin.place_forget()
        self.entryNewSurnameEditAdmin.place_forget()
        self.entryNewHouseNumberEditAdmin.place_forget()
        self.entryNewStreetEditAdmin.place_forget()
        self.entryNewCityEditAdmin.place_forget()
        self.entryNewPostCodeEditAdmin.place_forget()
        self.entryNewAccountTypeEditAdmin.place_forget()
        self.BtnUpdateDataEditAdmin.place_forget()
        
        self.labelIdRemoveUser.place_forget()
        self.entryIdRemoveUser.place_forget()
        self.BtnRemoveUser.place_forget()
        
        self.labelIdRemoveAdmin.place_forget()
        self.entryIdRemoveAdmin.place_forget()
        self.BtnRemoveAdmin.place_forget()
        
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        GotID = str(self.entryIDFind.get())
        GotName = str(self.entryNameFind.get())
        GotSurname = str(self.entrySurnameFind.get())
        GotHouseNumber = str(self.entryHouseNumberFind.get())
        GotStreet = str(self.entryStreetFind.get())
        GotCity = str(self.entryCityFind.get())
        GotPostCode = str(self.entryPostCodeFind.get())
        GotAccountType = str(self.entryAccountTypeFind.get())
                       
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'UserName', 'UserMiddleName','UserSurname','HouseNumber','Street','City','PostCode','UserAccType')
        self.tv.heading("#0", text='User ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('UserName', text='User name')
        self.tv.column('UserName', anchor='center', width=100)
        self.tv.heading('UserMiddleName', text='User middle name')
        self.tv.column('UserMiddleName', anchor='center', width=100)
        self.tv.heading('UserSurname', text='User surname')
        self.tv.column('UserSurname', anchor='center', width=100)
        self.tv.heading('HouseNumber', text='House number')
        self.tv.column('HouseNumber', anchor='center', width=100)
        self.tv.heading('Street', text='Street')
        self.tv.column('Street', anchor='center', width=100)
        self.tv.heading('City', text='City')
        self.tv.column('City', anchor='center', width=100)
        self.tv.heading('PostCode', text='Post code')
        self.tv.column('PostCode', anchor='center', width=100)
        self.tv.heading('UserAccType', text='User account type')
        self.tv.column('UserAccType', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType FROM Users Where userId = '{}' OR userName = '{}' OR userSurname = '{}' OR HouseNumber = '{}' OR Street = '{}' OR City = '{}' OR PostCode = '{}' OR userAccType = '{}'".format(GotID, GotName, GotSurname, GotHouseNumber, GotStreet, GotCity, GotPostCode, GotAccountType))
        lis = []
        for row in c.fetchall():
            lis.append(row)     
            userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType = operator.itemgetter(0,1,2,3,4,5,6,7,8)(row)
            self.treeview.insert('', 'end',text=userId,  values=(userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userAccType))
            
class InvestmentsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Investments:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
      
        self.labelNameAdd= tk.Label(self, text = 'Investment name:')
        self.labelValueAdd = tk.Label(self, text = 'Investment value:')
        
        self.entryNameAdd = tk.Entry(self)
        self.entryValueAdd = tk.Entry(self)
        
        self.BtnAddInvestmentAdd = tk.Button(self,text ='Add investment', command = self.AddInvestmentToDB)
        
        self.labelNameAdd.place(x = 170,y = 25)
        self.labelValueAdd.place(x = 170,y = 60)
                
        self.entryNameAdd.place(x = 300,y = 25)
        self.entryValueAdd.place(x = 300,y = 60)
        
        self.BtnAddInvestmentAdd.place(x = 180,y = 95)
        
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind= tk.Label(self, text = 'ID:')
        self.labelNameFind= tk.Label(self, text = 'Name:')
        self.labelValueFind = tk.Label(self, text = 'Value:')
        
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entryValueFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelValueFind.place(x = 170,y = 95)
                
        self.entryIDFind.place(x = 300,y = 25)
        self.entryNameFind.place(x = 300,y = 60)
        self.entryValueFind.place(x = 300,y = 95)
        
        self.BtnGetDataFind.place(x = 180,y = 120)
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()   
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.labelNameUpdate= tk.Label(self, text = 'Name:')
        self.labelNewNameUpdate= tk.Label(self, text = 'New name:')
        self.labelNewValueUpdate = tk.Label(self, text = 'Value:')
        self.labelDisableUpdate= tk.Label(self, text = 'Disable:')
        
        self.entryNameUpdate = tk.Entry(self)
        self.entryNewNameUpdate = tk.Entry(self)
        self.entryNewValueUpdate = tk.Entry(self)
        self.entryDisableUpdate = tk.Entry(self) 
        
        self.BtnGetDataUpdate = tk.Button(self,text ='Update', command = self.UpdateToInvestments)
        
        self.labelNameUpdate.place(x = 170,y = 25)
        self.labelNewNameUpdate.place(x = 170,y = 60)
        self.labelNewValueUpdate.place(x = 170,y = 95)
        self.labelDisableUpdate.place(x = 170,y = 130)
        
        self.entryNameUpdate.place(x = 300,y = 25)
        self.entryNewNameUpdate.place(x = 300,y = 60)
        self.entryNewValueUpdate.place(x = 300,y = 95)
        self.entryDisableUpdate.place(x = 300,y = 130)
        
        self.BtnGetDataUpdate.place(x = 180,y = 155)

        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.showAll = tk.Button(self.frm,text ='Show investments', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.Find = tk.Button(self.frm,text ='Find investments', command = self.FindList)
        self.Find.pack(expand=False, fill='x')
        
        self.AddInvestment = tk.Button(self.frm,text ='Add investments', command = self.AddInvestmetn)
        self.AddInvestment.pack(expand=False, fill='x')
        
        self.ManadgeInvestment = tk.Button(self.frm,text ='Manadge investments', command = self.UpdateInvestments)
        self.ManadgeInvestment.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(BankBasePage))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()          
               
    def PrintAll(self):       
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'InvestmentName', 'InvestmentValue','InvestmentDateChanged','InvestmentDateCreated','InvestmentDateRemoved')
        self.tv.heading("#0", text='Investment ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('InvestmentName', text='Investment name')
        self.tv.column('InvestmentName', anchor='center', width=100)
        self.tv.heading('InvestmentValue', text='Investment value')
        self.tv.column('InvestmentValue', anchor='center', width=100)
        self.tv.heading('InvestmentDateChanged', text='Investments last change')
        self.tv.column('InvestmentDateChanged', anchor='center', width=100)
        self.tv.heading('InvestmentDateCreated', text='When was investment created')
        self.tv.column('InvestmentDateCreated', anchor='center', width=100)
        self.tv.heading('InvestmentDateRemoved', text='When was investment removed')
        self.tv.column('InvestmentDateRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Investments")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InvestmentId, InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved = operator.itemgetter(0,1,2,3,4,5)(row)
            self.treeview.insert('', 'end',text=InvestmentId,  values=(InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved))
    
    def AddInvestmetn(self):
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        self.labelNameAdd= tk.Label(self, text = 'Investment name:')
        self.labelValueAdd = tk.Label(self, text = 'Investment value:')
        
        self.entryNameAdd = tk.Entry(self)
        self.entryValueAdd = tk.Entry(self)
        
        self.BtnAddInvestmentAdd = tk.Button(self,text ='Add investment', command = self.AddInvestmentToDB)
        
        self.labelNameAdd.place(x = 170,y = 25)
        self.labelValueAdd.place(x = 170,y = 60)
                
        self.entryNameAdd.place(x = 300,y = 25)
        self.entryValueAdd.place(x = 300,y = 60)
        
        self.BtnAddInvestmentAdd.place(x = 180,y = 95)
        
    def AddInvestmentToDB(self):
        GotName = str(self.entryNameAdd.get())
        GotValue = str(self.entryValueAdd.get())
        
        data.insertIntoInvestments(GotName, GotValue)
        
    def FindList(self):
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIDFind= tk.Label(self, text = 'ID:')
        self.labelNameFind= tk.Label(self, text = 'Name:')
        self.labelValueFind = tk.Label(self, text = 'Value:')
        
        self.entryIDFind = tk.Entry(self) 
        self.entryNameFind = tk.Entry(self)
        self.entryValueFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelIDFind.place(x = 170,y = 25)
        self.labelNameFind.place(x = 170,y = 60)
        self.labelValueFind.place(x = 170,y = 95)
                
        self.entryIDFind.place(x = 300,y = 25)
        self.entryNameFind.place(x = 300,y = 60)
        self.entryValueFind.place(x = 300,y = 95)
        
        self.BtnGetDataFind.place(x = 180,y = 120)

    def ShowGottenData(self):  
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()

        for i in self.tv.get_children():
            self.tv.delete(i)
        
        GotID = str(self.entryIDFind.get())
        GotName = str(self.entryNameFind.get())
        GotValue = str(self.entryValueFind.get())
              
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'InvestmentName', 'InvestmentValue','InvestmentDateChanged','InvestmentDateCreated','InvestmentDateRemoved')
        self.tv.heading("#0", text='Investment ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('InvestmentName', text='Investment name')
        self.tv.column('InvestmentName', anchor='center', width=100)
        self.tv.heading('InvestmentValue', text='Investment value')
        self.tv.column('InvestmentValue', anchor='center', width=100)
        self.tv.heading('InvestmentDateChanged', text='Investments last change')
        self.tv.column('InvestmentDateChanged', anchor='center', width=100)
        self.tv.heading('InvestmentDateCreated', text='When was investment created')
        self.tv.column('InvestmentDateCreated', anchor='center', width=100)
        self.tv.heading('InvestmentDateRemoved', text='When was investment removed')
        self.tv.column('InvestmentDateRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * FROM Investments Where InvestmentsId = '{}' OR InvestmentName = '{}' OR InvestmentValue = '{}' ".format(GotID, GotName, GotValue))
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InvestmentId, InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved = operator.itemgetter(0,1,2,3,4,5)(row)
            self.treeview.insert('', 'end',text=InvestmentId,  values=(InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved))
            
    def UpdateInvestments(self):
        self.labelNameAdd.place_forget()
        self.labelValueAdd.place_forget()
        self.entryNameAdd.place_forget()
        self.entryValueAdd.place_forget()
        self.BtnAddInvestmentAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelNameFind.place_forget()
        self.labelValueFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryNameFind.place_forget()
        self.entryValueFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewValueUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewValueUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()

        self.labelNameUpdate= tk.Label(self, text = 'Name:')
        self.labelNewNameUpdate= tk.Label(self, text = 'New name:')
        self.labelNewValueUpdate = tk.Label(self, text = 'Value:')
        self.labelDisableUpdate= tk.Label(self, text = 'Disable:')
        
        self.entryNameUpdate = tk.Entry(self)
        self.entryNewNameUpdate = tk.Entry(self)
        self.entryNewValueUpdate = tk.Entry(self)
        self.entryDisableUpdate = tk.Entry(self) 
        
        self.BtnGetDataUpdate = tk.Button(self,text ='Update', command = self.UpdateToInvestments)
        
        self.labelNameUpdate.place(x = 170,y = 25)
        self.labelNewNameUpdate.place(x = 170,y = 60)
        self.labelNewValueUpdate.place(x = 170,y = 95)
        self.labelDisableUpdate.place(x = 170,y = 130)
        
        self.entryNameUpdate.place(x = 300,y = 25)
        self.entryNewNameUpdate.place(x = 300,y = 60)
        self.entryNewValueUpdate.place(x = 300,y = 95)
        self.entryDisableUpdate.place(x = 300,y = 130)
        
        self.BtnGetDataUpdate.place(x = 180,y = 155)
    
    def UpdateToInvestments(self):    
        GotName = str(self.entryNameUpdate.get())
        GotNewName = str(self.entryNewNameUpdate.get())
        GotNewValue = str(self.entryNewValueUpdate.get())
        GotDisable = str(self.entryDisableUpdate.get())
        
        data.updateInvestments(GotNewName,GotNewValue, GotDisable, GotName)
        
class InterestRatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        self.grid(sticky = 'nswe')
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        
        self.lbl1 = tk.Label(self, text="Options:", fg='black', font=("Helvetica", 16, "bold"))
        self.lbl2 = tk.Label(self, text="Investments:", fg='black', font=("Helvetica", 16,"bold"))
        self.lbl1.grid(row=0, column=0, sticky='w')
        self.lbl2.grid(row=0, column=1, sticky='w')
        
        self.frm = tk.Frame(self)
        self.frm.grid(row=1, column=0, sticky='ns')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        self.labelInterestAdd= tk.Label(self, text = 'Interest name:')
        self.labelRateAdd = tk.Label(self, text = 'Interest rate:')
        self.entryInterestAdd = tk.Entry(self)
        self.entryRateAdd = tk.Entry(self)
        self.BtnAddInterestAdd = tk.Button(self,text ='Add interest', command = self.AddInterestToDB)
        self.labelInterestAdd.place(x = 170,y = 25)
        self.labelRateAdd.place(x = 170,y = 60)
        self.entryInterestAdd.place(x = 300,y = 25)
        self.entryRateAdd.place(x = 300,y = 60)
        self.BtnAddInterestAdd.place(x = 180,y = 95)
        
        self.labelIDFind= tk.Label(self, text = 'ID:')
        self.labelInterestFind= tk.Label(self, text = 'Interest:')
        self.labelRateFind = tk.Label(self, text = 'Rate:')
        self.entryIDFind = tk.Entry(self) 
        self.entryInterestFind = tk.Entry(self)
        self.entryRateFind = tk.Entry(self)
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        self.labelIDFind.place(x = 170,y = 25)
        self.labelInterestFind.place(x = 170,y = 60)
        self.labelRateFind.place(x = 170,y = 95)
        self.entryIDFind.place(x = 300,y = 25)
        self.entryInterestFind.place(x = 300,y = 60)
        self.entryRateFind.place(x = 300,y = 95)
        self.BtnGetDataFind.place(x = 180,y = 120)

        self.labelNameUpdate= tk.Label(self, text = 'Interest name:')
        self.labelNewNameUpdate= tk.Label(self, text = 'New interest name:')
        self.labelNewRateUpdate = tk.Label(self, text = 'Rate:')
        self.labelDisableUpdate= tk.Label(self, text = 'Disable:')
        self.entryNameUpdate = tk.Entry(self)
        self.entryNewNameUpdate = tk.Entry(self)
        self.entryNewRateUpdate = tk.Entry(self)
        self.entryDisableUpdate = tk.Entry(self) 
        self.BtnGetDataUpdate = tk.Button(self,text ='Update', command = self.UpdateToInterest)
        self.labelNameUpdate.place(x = 170,y = 25)
        self.labelNewNameUpdate.place(x = 170,y = 60)
        self.labelNewRateUpdate.place(x = 170,y = 95)
        self.labelDisableUpdate.place(x = 170,y = 130)        
        self.entryNameUpdate.place(x = 300,y = 25)
        self.entryNewNameUpdate.place(x = 300,y = 60)
        self.entryNewRateUpdate.place(x = 300,y = 95)
        self.entryDisableUpdate.place(x = 300,y = 130)
        self.BtnGetDataUpdate.place(x = 180,y = 155)
        
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()    

        self.showAll = tk.Button(self.frm,text ='Show interest rates', command = self.PrintAll)
        self.showAll.pack(expand=False, fill='x')
        
        self.Find = tk.Button(self.frm,text ='Find interest rates', command = self.FindList)
        self.Find.pack(expand=False, fill='x')
        
        self.AddInterestRate = tk.Button(self.frm,text ='Add interest rate', command = self.AddInterest)
        self.AddInterestRate.pack(expand=False, fill='x')
        
        self.ManadgeInterestRate = tk.Button(self.frm,text ='Manadge interest rate', command = self.UpdateInterest)
        self.ManadgeInterestRate.pack(expand=False, fill='x')
        
        self.buttonBack = tk.Button(self.frm,text ='go back', command = lambda: controller.show_frame(BankBasePage))
        self.buttonBack.pack(expand=False, fill='x')
        
        self.listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection.grid(row=1, column=1, sticky='nswe')
        self.listSelection.grid_forget()   
        
        self.listSelection1 = tk.Listbox(self, height=4, font=("Helvetica", 12))
        self.listSelection1.grid(row=1, column=1, sticky='nswe')
        self.listSelection1.grid_forget() 
        
        self.tv = ttk.Treeview(self,height=4)
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv.grid_forget()          

    def PrintAll(self):       
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'InterestName', 'InterestRate','InterestDateChanged','InterestDateCreated','InterestDateRemoved')
        self.tv.heading("#0", text='Interest ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('InterestName', text='Interest name')
        self.tv.column('InterestName', anchor='center', width=100)
        self.tv.heading('InterestRate', text='Interest rate')
        self.tv.column('InterestRate', anchor='center', width=100)
        self.tv.heading('InterestDateChanged', text='Interest last change')
        self.tv.column('InterestDateChanged', anchor='center', width=100)
        self.tv.heading('InterestDateCreated', text='When was interest created')
        self.tv.column('InterestDateCreated', anchor='center', width=100)
        self.tv.heading('InterestDateRemoved', text='When was Interest removed')
        self.tv.column('InterestDateRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * From Interest")
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InterestId, InterestName, InterestRate, InterestDateChanged,InterestDateCreated, InterestDateRemoved = operator.itemgetter(0,1,2,3,4,5)(row)
            self.treeview.insert('', 'end',text=InterestId,  values=(InterestName, InterestRate, InterestDateChanged,InterestDateCreated, InterestDateRemoved))
    
    def AddInterest(self):
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        self.labelInterestAdd= tk.Label(self, text = 'Interest name:')
        self.labelRateAdd = tk.Label(self, text = 'Interest rate:')
        
        self.entryInterestAdd = tk.Entry(self)
        self.entryRateAdd = tk.Entry(self)
        
        self.BtnAddInterestAdd = tk.Button(self,text ='Add interest', command = self.AddInterestToDB)
        
        self.labelInterestAdd.place(x = 170,y = 25)
        self.labelRateAdd.place(x = 170,y = 60)
                
        self.entryInterestAdd.place(x = 305,y = 25)
        self.entryRateAdd.place(x = 305,y = 60)
        
        self.BtnAddInterestAdd.place(x = 180,y = 95)
        
    def AddInterestToDB(self):
        GotName = str(self.entryInterestAdd.get())
        GotRate = str(self.entryRateAdd.get())
        
        data.insertIntoInterest(GotName, GotRate)
        
    def FindList(self):
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()
        
        self.labelIDFind= tk.Label(self, text = 'ID:')
        self.labelInterestFind= tk.Label(self, text = 'Interest:')
        self.labelRateFind = tk.Label(self, text = 'Rate:')
        
        self.entryIDFind = tk.Entry(self) 
        self.entryInterestFind = tk.Entry(self)
        self.entryRateFind = tk.Entry(self)
        
        self.BtnGetDataFind = tk.Button(self,text ='Search', command = self.ShowGottenData)
        
        self.labelIDFind.place(x = 170,y = 25)
        self.labelInterestFind.place(x = 170,y = 60)
        self.labelRateFind.place(x = 170,y = 95)
                
        self.entryIDFind.place(x = 305,y = 25)
        self.entryInterestFind.place(x = 305,y = 60)
        self.entryRateFind.place(x = 305,y = 95)
        
        self.BtnGetDataFind.place(x = 180,y = 120)

    def ShowGottenData(self):  
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()

        for i in self.tv.get_children():
            self.tv.delete(i)
        
        GotID = str(self.entryIDFind.get())
        GotInterest = str(self.entryInterestFind.get())
        GotRate = str(self.entryRateFind.get())
              
        self.tv.grid(row=1, column=1, sticky='nswe')
        self.tv['columns'] = ( 'InterestName', 'InterestRate','InterestDateChanged','InterestDateCreated','InterestDateRemoved')
        self.tv.heading("#0", text='Interest ID')
        self.tv.column("#0", anchor='center', width=50)
        self.tv.heading('InterestName', text='Interest name')
        self.tv.column('InterestName', anchor='center', width=100)
        self.tv.heading('InterestRate', text='Interest rate')
        self.tv.column('InterestRate', anchor='center', width=100)
        self.tv.heading('InterestDateChanged', text='Interest last change')
        self.tv.column('InterestDateChanged', anchor='center', width=100)
        self.tv.heading('InterestDateCreated', text='When was interest created')
        self.tv.column('InterestDateCreated', anchor='center', width=100)
        self.tv.heading('InterestDateRemoved', text='When was Interest removed')
        self.tv.column('InterestDateRemoved', anchor='center', width=100)
        self.treeview = self.tv
        
        c.execute("SELECT * FROM Interest Where InterestId = '{}' OR Interest = '{}' OR Rate = '{}' ".format(GotID, GotInterest, GotRate))
        lis = []
        for row in c.fetchall():
            lis.append(row)   
            InterestId, InterestName, InterestRate, InterestDateChanged,InterestDateCreated, InterestDateRemoved = operator.itemgetter(0,1,2,3,4,5)(row)
            self.treeview.insert('', 'end',text=InterestId,  values=(InterestName, InterestRate, InterestDateChanged,InterestDateCreated, InterestDateRemoved))
            
    def UpdateInterest(self):
        self.labelInterestAdd.place_forget()
        self.labelRateAdd.place_forget()
        self.entryInterestAdd.place_forget()
        self.entryRateAdd.place_forget()
        self.BtnAddInterestAdd.place_forget()
        
        self.labelIDFind.place_forget()
        self.labelInterestFind.place_forget()
        self.labelRateFind.place_forget()
        self.entryIDFind.place_forget()
        self.entryInterestFind.place_forget()
        self.entryRateFind.place_forget()
        self.BtnGetDataFind.place_forget()
        
        self.entryNameUpdate.place_forget()
        self.entryNewNameUpdate.place_forget()
        self.entryNewRateUpdate.place_forget()
        self.entryDisableUpdate.place_forget()
        self.labelNameUpdate.place_forget()
        self.labelNewNameUpdate.place_forget()
        self.labelNewRateUpdate.place_forget()
        self.labelDisableUpdate.place_forget()
        self.BtnGetDataUpdate.place_forget()
        
        self.tv.grid_forget()

        self.labelNameUpdate= tk.Label(self, text = 'Interest name:')
        self.labelNewNameUpdate= tk.Label(self, text = 'New interest name:')
        self.labelNewRateUpdate = tk.Label(self, text = 'Rate:')
        self.labelDisableUpdate= tk.Label(self, text = 'Disable:')
        
        self.entryNameUpdate = tk.Entry(self)
        self.entryNewNameUpdate = tk.Entry(self)
        self.entryNewRateUpdate = tk.Entry(self)
        self.entryDisableUpdate = tk.Entry(self) 
        
        self.BtnGetDataUpdate = tk.Button(self,text ='Update', command = self.UpdateToInterest)
        
        self.labelNameUpdate.place(x = 170,y = 25)
        self.labelNewNameUpdate.place(x = 170,y = 60)
        self.labelNewRateUpdate.place(x = 170,y = 95)
        self.labelDisableUpdate.place(x = 170,y = 130)
        
        self.entryNameUpdate.place(x = 305,y = 25)
        self.entryNewNameUpdate.place(x = 305,y = 60)
        self.entryNewRateUpdate.place(x = 305,y = 95)
        self.entryDisableUpdate.place(x = 305,y = 130)
        
        self.BtnGetDataUpdate.place(x = 180,y = 165)
    
    def UpdateToInterest(self):    
        GotName = str(self.entryNameUpdate.get())
        GotNewName = str(self.entryNewNameUpdate.get())
        GotNewRate = str(self.entryNewRateUpdate.get())
        GotDisable = str(self.entryDisableUpdate.get())
        
        data.UpdateInterest(GotNewName,GotNewRate, GotDisable, GotName)
        
class BankBalance(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Balance in the bank')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankBasePage))
        buttonBack.pack()

class UpdateSucessLoan(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Update for loan was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(ManadgeLoadns))
        buttonBack.pack()
        
class UpdateSucessWithdraw(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Withdraw was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        buttonBack.pack()
        
class UpdateSucessDeposit(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Deposit was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        buttonBack.pack()
        
class ErrorUpdateDeposit(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.labelError1 = tk.Label(self, text = 'Error! Deposit failed. The reason might be:')
        self.labelOption1 = tk.Label(self, text = '- wrong account ')
        self.labelOption2 = tk.Label(self, text = '- not enough money')
        self.labelError1.pack()
        self.labelOption1.pack()
        self.labelOption2.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        buttonBack.pack()
        
class ErrorUpdateWithdraw(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.labelError1 = tk.Label(self, text = 'Error! Withdraw failed. The reason might be:')
        self.labelOption1 = tk.Label(self, text = '- wrong account ')
        self.labelOption2 = tk.Label(self, text = '- not enough money')
        self.labelError1.pack()
        self.labelOption1.pack()
        self.labelOption2.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        buttonBack.pack()

        
class ErrorUpdatingLoans(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.labelError1 = tk.Label(self, text = 'Error! Wrong status. Please type one of the fallowing:')
        self.labelOption1 = tk.Label(self, text = '- Aprove')
        self.labelOption2 = tk.Label(self, text = '- Reject')
        self.labelOption3 = tk.Label(self, text = '- Aproved')
        self.labelOption4 = tk.Label(self, text = '- Rejected')
        self.labelError1.pack()
        self.labelOption1.pack()
        self.labelOption2.pack()
        self.labelOption3.pack()
        self.labelOption4.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(ManadgeLoadns))
        buttonBack.pack()

class UpdateSucessUserFromAdmin(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Update for user was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(AdminPageSearch))
        buttonBack.pack()
        
class ErrorPageUserFromAdmin(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Error! Selected user is not an user.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(AdminPageSearch))
        buttonBack.pack()

class UpdateSucessUser(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Update for user was sucessfull.')
        self.label.pack()
        
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankPageSearch))
        buttonBack.pack()

class UpdateSucessAdmin(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Update for admin was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankPageSearch))
        buttonBack.pack()
        
class TransferSucessInternal(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Transfer was sucessfull.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(UserPageAccSelect))
        buttonBack.pack()


class ErrorPageUser(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.labelError1 = tk.Label(self, text = 'Error! Wrong status. Please type one of the fallowing:')
        self.labelOption1 = tk.Label(self, text = '- User')
        self.labelOption2 = tk.Label(self, text = '- Close')
        self.labelOption3 = tk.Label(self, text = '- Closed')
        self.labelError1.pack()
        self.labelOption1.pack()
        self.labelOption2.pack()
        self.labelOption3.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankPageSearch))
        buttonBack.pack()
        
class ErrorPageAdmin(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'Error! Selected user is not an admin.')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(BankPageSearch))
        buttonBack.pack()

class ErrorPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.label = tk.Label(self, text = 'error page')
        self.label.pack()
        
        buttonBack = ttk.Button(self, text = 'Go back', command = lambda: controller.show_frame(LoginPage))
        buttonBack.pack()
        
class WelcomePage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text = 'welcome page')
        self.label1.grid(sticky="nsew")
        self.buttonBack = ttk.Button(self, text = 'Start', command = lambda: controller.show_frame(LoginPage))
        self.buttonBack.grid(sticky="nsew")
               
class BankSystem(object):
    def __init__(self):
        self.load_bank_data()
    
    def load_bank_data(self):
        datenow = str(datetime.datetime.now())
        UserCA = str(True)
        UserSA = str(False)
        UserCOD = str(False)
        UserMMA = str(False)
        UserIRA = str(False)
        
        data.InsertIntoInterestStart('Basic','1')
        data.InsertIntoInterestStart('Extreme','5')
        data.InsertIntoOverdraft('Minimum','-500')
        data.InsertIntoOverdraft('Maximum','-5000')
        
        hashed_password = data.hash_password('bank')
        data.dynamic_data_entry('bank', 'bank','bank', hashed_password,0,'bank','bank', 'bank','OG','bank','OG')   

        hashed_password = data.hash_password('p1')        
        data.dynamic_data_entry('Adam', '','Smith', hashed_password,14,'Wilcot','Bath', 'B5 5RT',datenow,'user',datenow)
        x = data.returnUserID('Adam','Smith',hashed_password,'Bath')
        y = str(x)
        x = ",()"
        for char in x:
            y = y.replace(char, "")
        data.InsertIntoDepositAmmount(y,'5000.00','CA','1','1')
        data.insertIntoAccType(y,UserCA,UserSA,UserCOD,UserMMA,UserIRA)

        hashed_password = data.hash_password('p2')        
        data.dynamic_data_entry('David', '','White', hashed_password,60,'Holborn Viaduc','London', 'EC1A 2FD',datenow,'user',datenow)
        x = data.returnUserID('David','White','p2','London')
        y = str(x)
        x = ",()"
        for char in x:
            y = y.replace(char, "")
        data.InsertIntoDepositAmmount(y,'3200.00','CA','1','1')
        data.insertIntoAccType(y,UserCA,UserSA,UserCOD,UserMMA,UserIRA)

        hashed_password = data.hash_password('p3')        
        data.dynamic_data_entry('Alice', '','Churchil', hashed_password,5,'Cardigan Street','Birmingham', 'B4 7BD',datenow,'user',datenow)  
        x = data.returnUserID('Alice','Churchil',hashed_password,'Birmingham')
        y = str(x)
        x = ",()"
        for char in x:
            y = y.replace(char, "")
        data.InsertIntoDepositAmmount(y,'18000.00','CA','1','1')
        data.insertIntoAccType(y,UserCA,UserSA,UserCOD,UserMMA,UserIRA)

        hashed_password = data.hash_password('p4')        
        data.dynamic_data_entry('Ali', '','Abdallah', hashed_password,44,'Churchill Way West','Basingstoke', 'RG21 6YR',datenow,'user',datenow) 
        x = data.returnUserID('Ali','Abdallah',hashed_password,'Basingstoke')
        y = str(x)
        x = ",()"
        for char in x:
            y = y.replace(char, "")
        data.InsertIntoDepositAmmount(y,'40.00','CA','1','1')
        data.insertIntoAccType(y,UserCA,UserSA,UserCOD,UserMMA,UserIRA)
        
        hashed_password = data.hash_password('1441')
        data.dynamic_data_entry('Julian', '','Padget', hashed_password,12,'London Road','Birmingham', 'B95 7TT',datenow,'admin',datenow)    
        hashed_password = data.hash_password('2442')
        data.dynamic_data_entry('Cathy', '','Newman', hashed_password,47,'Mars Street','Newcastle', 'NE12 6TZ',datenow,'admin',datenow)    
      
    def search_admins_by_name():
        testName = 'Cathy'
        c.execute("SELECT * FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row) 
        
    def search_customers_by_name():
        testName = 'David'
        c.execute("SELECT * FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row)

    def print_all_accounts_details():
        data.read_from_db() 

class CustomerAccount:
    def get_first_name():
        testSurname = 'White'
        c.execute("SELECT Username FROM Users Where userSurname = '{}'" .format(testSurname))
        for row in c.fetchall():
            print(row)
            
    def get_last_name():
        testName = 'David'
        c.execute("SELECT UserSurname FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row)
            
    def get_address():
        testName = 'David'
        c.execute("SELECT HouseNumber, Street, City, PostCode FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row) 
            
    def print_balance():
        testName = 'David'
        c.execute("SELECT UserBal FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row) 
            
    def get_account_no():
        testName = 'David'
        c.execute("SELECT AccNum FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row)

class Admin:
    def get_first_name():
        testSurname = 'Newman'
        c.execute("SELECT Username FROM Users Where UserSurname = '{}'" .format(testSurname))
        for row in c.fetchall():
            print(row) 
    
    def get_last_name():
        testName = 'Cathy'
        c.execute("SELECT UserSurname FROM Users Where Username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row) 
            
    def get_address():
        testName = 'Cathy'
        c.execute("SELECT HouseNumber, Street, City, PostCode FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row)    
    
    def get_password():
        testName = 'Cathy'
        c.execute("SELECT Password FROM Users Where username = '{}'" .format(testName))
        for row in c.fetchall():
            print(row)
    
class data():
    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS "AccType" ( "AccTypeId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "userId"	INTEGER NOT NULL UNIQUE, "CA"	TEXT, "SA"	TEXT, "COD"	TEXT, "MMA"	TEXT, "IRA"	TEXT)')
        c.execute('CREATE TABLE IF NOT EXISTS "Appointments" ( "appointmentsId"	INTEGER, "userId"	INTEGER, "placeOfAppointment"	TEXT NOT NULL, "dateOfAppointment"	TEXT NOT NULL, "appointmentStatus"	TEXT NOT NULL, "userName"	TEXT NOT NULL, "userSurname"	TEXT NOT NULL, "userComment"	TEXT, PRIMARY KEY("appointmentsId"), FOREIGN KEY("userId") REFERENCES "Users")')
        c.execute('CREATE TABLE IF NOT EXISTS "Balance" (balanceId INTEGER PRIMARY KEY, userId INTEGER not NULL,accType TEXT not null, balance TEXT NOT NULL, dateOfChange TEXT NOT NULL,InterestId TEXT NOT NULL,OverdraftID TEXT NOT NULL, FOREIGN KEY(userId) REFERENCES Users)')
        c.execute('CREATE TABLE IF NOT EXISTS "DepositAndWithdraw" (DepositAndWithdrawId INTEGER PRIMARY KEY, Amount INTEGER not NULL, Status INTEGER not NULL, DateAdded TEXT not NULL, DateRemoved TEXT not NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Interest" (InterestId INTEGER PRIMARY KEY, Interest TEXT not NULL, Rate INTEGER not NULL, DateChanged TEXT not NULL, DateAdded TEXT not NULL, DateRemoved TEXT not NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Investments" (InvestmentsId INTEGER PRIMARY KEY, InvestmentName TEXT not NULL,InvestmentValue INTEGER not NULL, InvestmentDateChanged TEXT not NULL, InvestmentDateCreated TEXT not NULL, InvestmentDateRemoved TEXT not NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Loans" ("LoansId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "UserLoanId" INTEGER NOT NULL, "UserAccID" INTEGER NOT NULL, "LoanStatus"	TEXT NOT NULL, "LoanAmount" INTEGER NOT NULL, "LoanMonthlyPlan" INTEGER NOT NULL, "LoanComents" TEXT NOT NULL, "LoanChanged"	TEXT NOT NULL, "LoanAdded" TEXT NOT NULL, "LoanRemoved" TEXT NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Transactions" (TransactionId INTEGER PRIMARY KEY, userId INTEGER not NULL,TransferMoneyId INTEGER NOT NULL,LoansId INTEGER NOT NULL,InvestmentsId INTEGER NOT NULL,DepositAndWithdrawId INTEGER NOT NULL,InterestId INTEGER NOT NULL, DateChange TEXT NOT NULL, FOREIGN KEY(userId) REFERENCES Users, FOREIGN KEY(TransferMoneyId) REFERENCES Transfers, FOREIGN KEY(LoansId) REFERENCES Loans, FOREIGN KEY(InvestmentsId) REFERENCES Investments, FOREIGN KEY(DepositAndWithdrawId) REFERENCES DepostitsAndWothdraw, FOREIGN KEY(InterestId) REFERENCES Interests)')
        c.execute('CREATE TABLE IF NOT EXISTS "TransferMoney" (TransferMoneyId INTEGER PRIMARY KEY, TransfferFrom INTEGER not NULL,TransferTo INTEGER not NULL, TransferAmount INTEGER not NULL,TransferReason TEXT not NULL,TransferFee INTEGER not NULL,TransferStatus TEXT not NULL, TransferDateSend TEXT not NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "UserInvestments" ("UIID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "InvestmentID" INTEGER NOT NULL, "UserID" INTEGER NOT NULL, "Quantity" INTEGER NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Users" (userId INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT NOT NULL, userMiddleName TEXT, userSurname TEXT NOT NULL, userPass TEXT NOT NULL, HouseNumber INTIGER, Street TEXT, City TEXT, PostCode TEXT, userCreationDate TEXT NOT NULL, userAccType TEXT NOT NULL, userLastLoginTime TEXT NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "Overdraft" ("OverdraftID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "NameOfOverdraft" TEXT NOT NULL UNIQUE, "LimitOfOverdraft" TEXT NOT NULL,"ReachedToday" TEXT NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS "UserOverdrafts" ("UOID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "OVID"	INTEGER NOT NULL UNIQUE, "USID"	INTEGER NOT NULL UNIQUE, "Quantity" INTEGER NOT NULL,"Date" INTEGER NOT NULL)')
        
    def returnUserID(username, usersurname, userpass, usercity):      
        c.execute("SELECT userId FROM Users Where userName like '{}' and userSurname like '{}' and userPass like '{}' and City like '{}'" .format(username, usersurname, userpass, usercity))
        for row in c.fetchall():
            return(row)
            
    def updateIntoAppointments(GotAppointmentID,GotUserID, GotPlace, GotDate, GotUserStatus, GotUserName, GotUserSurname, GotUserComment):
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("UPDATE Appointments SET userId = '{}', placeOfAppointment = '{}', dateOfAppointment = '{}', appointmentStatus = '{}', userName = '{}', userSurname = '{}', userComment = '{}' WHERE appointmentsId = '{}'".format(GotUserID, GotPlace, GotDate, GotUserStatus, GotUserName, GotUserSurname, GotUserComment,GotAppointmentID))
        conn.commit()
        
        c.close()
        conn.close()
        
        
    def InsertIntoWithdrawAmmount(GotId, GotAmmount, GotAccount):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("Insert INTO Balance(userId, accType, balance, dateOfChange) VALUES (?,?,?,?)",(GotId,GotAccount, GotAmmount, datenow))
        conn.commit()
        
        c.close()
        conn.close()   
        
        
    def InsertIntoDepositAmmount(GotId, GotAmmount, GotAccount, GotInterestId,GotOverdraftID):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("Insert INTO Balance(userId, accType, balance, dateOfChange, InterestId, OverdraftID) VALUES (?,?,?,?,?,?)",(GotId,GotAccount, GotAmmount,datenow, GotInterestId,GotOverdraftID))
        conn.commit()
        
        c.close()
        conn.close()
        
    def InsertIntoOverdraft(Name, Limit):
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("Insert INTO Overdraft(NameOfOverdraft,LimitOfOverdraft,ReachedToday) VALUES (?,?,?)",(Name, Limit,''))
        conn.commit()
        
        c.close()
        conn.close()
        
    def InsertIntoUserInvestments(GotId,GotInvestment, GotAmount, GotAccount, GotStatus):
        if (GotAccount == "Checking account"):
            GotAccount = 'CA'
        
        if (GotAccount == "Savings account"):
            GotAccount = 'SA'
        
        if (GotAccount == 'Certificate of Deposit (CD)'):
            GotAccount = 'COD'
        
        if (GotAccount == 'Money market account'):
            GotAccount = 'MMA'
        
        if (GotAccount == 'Individual Retirement Accounts (IRAs)'):
            GotAccount = 'IRA'
            
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        qu = '' 
        idInvestment = ''
        pr = ''
        
        c.execute("SELECT InvestmentsId, InvestmentValue FROM Investments Where InvestmentName is '{}'".format(GotInvestment))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            idInvestment,pr = operator.itemgetter(0,1)(row)
        
        NewAmount = (float(GotAmount)*float(pr))
        
        c.execute("SELECT Quantity From UserInvestments Where UserID is {} and InvestmentID is {}".format(GotId, idInvestment))
        lis = []
        
        for row in c.fetchall():
            lis.append(row)        
            qu = operator.itemgetter(0)(row)
        
        if(qu != ''):       
            if (GotStatus == 'buy'):
                GotAmount = (float(qu) + float(GotAmount))
            if (GotStatus == 'sell'):
                GotAmount = (float(qu) - float(GotAmount))
            c.execute("UPDATE UserInvestments SET Quantity = '{}' WHERE UserID = '{}' and InvestmentID = '{}'".format(GotAmount,GotId, idInvestment))

        else:          
            c.execute("Insert INTO UserInvestments(UserID, InvestmentID, Quantity) VALUES (?,?,?)",(GotId,idInvestment, GotAmount))
                
        conn.commit()
        c.close()
        conn.close()
        
        if (GotStatus == 'buy'):
            data.UpdateWithdrawAmmount(GotId, NewAmount, GotAccount)
        
        if (GotStatus == 'sell'):
            data.UpdateDepositAmmount(GotId, NewAmount, GotAccount)
            
    def UpdateDepositAmmountToOther(GotUsername,GotSurname, GotAmmount, GotAccount):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        GotId = ''
        ret = ''
        c.execute("SELECT userId, balance From balance Where balance.userId is (SELECT Users.userId From Users Where userName is '{}' and userSurname is '{}')".format(GotUsername,GotSurname))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            GotId,ret = operator.itemgetter(0,1)(row)
        print(ret,GotId)
        GotAmmount = (float(ret) + float(GotAmmount))
        print('')
        print(GotAmmount,GotId)
        c.execute("UPDATE Balance SET balance = '{}', dateOfChange = '{}' WHERE userId = '{}' and accType = '{}'".format(GotAmmount,datenow, GotId, GotAccount))

        conn.commit()
        
        c.close()
        conn.close()   
        
        
    def UpdateDepositAmmount(GotId, GotAmmount, GotAccount):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        am = float(GotAmmount)
        ret = ''
        qua = ''
        c.execute("SELECT balance FROM Balance Where userId is '{}' and accType is '{}' ".format(GotId,GotAccount))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ret = operator.itemgetter(0)(row)

        GotAmmount = (float(ret) + float(GotAmmount))

        c.execute("SELECT Quantity FROM UserOverdrafts Where USID is '{}'".format(GotId))
        for row in c.fetchall():
                qua = float(operator.itemgetter(0)(row) or 0)
             
        print(qua)
        if (qua == ''):
            c.execute("UPDATE Balance SET balance = '{}', dateOfChange = '{}' WHERE userId = '{}' and accType = '{}'".format(GotAmmount,datenow, GotId, GotAccount))

        elif (qua < 0):
            dif = qua + am
            if(dif > 0):    
                c.execute("UPDATE UserOverdrafts SET  Quantity = {}".format(0))
                GotAmmount = GotAmmount + qua
                c.execute("UPDATE Balance SET balance = '{}', dateOfChange = '{}' WHERE userId = '{}' and accType = '{}'".format(GotAmmount,datenow, GotId, GotAccount))
            elif(dif <= 0):
                c.execute("UPDATE UserOverdrafts SET  Quantity = {}".format(dif))

                
        conn.commit()
        
        c.close()
        conn.close()
        
    def UpdateWithdrawAmmount(GotId, GotAmmount, GotAccount):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        ret = ''
        oid = ''
        
        c.execute("SELECT balance, OverdraftID FROM Balance Where userId is '{}' and accType is '{}' ".format(GotId,GotAccount))
        lis = []
        for row in c.fetchall():
            lis.append(row)        
            ret ,oid  = operator.itemgetter(0,1)(row)
            
        print(ret)
        print(GotAmmount)
        if(float(ret) >= float(GotAmmount)):
            GotAmmount = (float(ret) - float(GotAmmount))
            c.execute("UPDATE Balance SET balance = '{}', dateOfChange = '{}' WHERE userId = '{}' and accType = '{}'".format(GotAmmount,datenow, GotId, GotAccount))

        if(float(ret) < float(GotAmmount)):
            overDrId = 0
            overQuan = 0
            c.execute("SELECT UOID FROM UserOverdrafts Where USID is '{}'".format(GotId))
            for row in c.fetchall():
                overDrId = int(operator.itemgetter(0)(row) or 0)
            
            if (overDrId == 0):
                c.execute("SELECT Overdraft.LimitOfOverdraft FROM balance, Overdraft WHERE userId is {} and accType is '{}' AND Overdraft.OverdraftID like balance.OverdraftID".format(GotId,GotAccount))
                for row in c.fetchall():
                    overQuan = int(operator.itemgetter(0)(row) or 0)
                
                Dif = (float(GotAmmount)-float(ret))
                if(overQuan > Dif):
                    print('o4')
                    print('error')
                if(overQuan < Dif):
                    c.execute("Insert INTO UserOverdrafts(OVID, USID, Quantity, Date) VALUES (?,?,?,?)",(oid,GotId, Dif, datenow))

            
            elif(overDrId != 0):
                print('o6')
                bal = ''
                c.execute("SELECT Quantity FROM UserOverdrafts Where USID is {}".format(GotId))
                for row in c.fetchall():
                            bal = float(operator.itemgetter(0)(row) or 0)
                            
                bal =-(float(GotAmmount)-(float(bal)))
                c.execute("SELECT Overdraft.LimitOfOverdraft FROM balance, Overdraft WHERE userId is {} and accType is '{}' AND Overdraft.OverdraftID like balance.OverdraftID".format(GotId,GotAccount))
                for row in c.fetchall():
                    overQuan = int(operator.itemgetter(0)(row) or 0)
                    
                if(overQuan <= bal):
                    print('big')
                    c.execute("UPDATE UserOverdrafts SET  Quantity = {}".format(bal))
                else:
                    print('limit has been reached')
                    
                

        conn.commit()
        
        c.close()
        conn.close()
        
    def insertIntoAppointments(UserID, UserName, UserSurname,GotPlace,GotDate, AppointmentComment):
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("Insert INTO Appointments(userId, placeOfAppointment, dateOfAppointment, appointmentStatus, userName, userSurname, userComment) VALUES (?,?,?,?,?,?,?)",(UserID, GotPlace, GotDate, 'unconfirmed', UserName, UserSurname, AppointmentComment))
        conn.commit()
        
        c.close()
        conn.close()
                
    def insertIntoLoansStatus(GotID,GotStatus,GotComment):  
        print(GotID,GotStatus,GotComment)
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("UPDATE Loans SET LoanStatus = '{}', LoanComents = '{}', LoanChanged = '{}' WHERE LoansId = '{}'".format(GotStatus,GotComment,datenow,GotID))
        if(GotStatus == 'aprove'):
            c.execute("UPDATE Balance SET balance = balance + (SELECT  Loans.LoanAmount FROM Loans WHERE  Loans.LoanStatus like 'aprove') WHERE Balance.userId like (SELECT Loans.UserLoanId FROM Loans WHERE Loans.LoansId like {})".format(GotID))
        conn.commit()
        c.close()
        conn.close() 
        
    def insertIntoLoansRequest(GotUserID, GotAccID, GotAmount, GotComments):
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor() 
        
        c.execute("Insert INTO Loans(UserLoanId, UserAccID, LoanStatus, LoanAmount, LoanMonthlyPlan, LoanComents, LoanChanged, LoanAdded, LoanRemoved) VALUES (?,?,?,?,?,?,?,?,?)",(GotUserID, GotAccID, 'pending', GotAmount, 0, GotComments, datenow, '', ''))
        
        conn.commit()
        
        c.close()
        conn.close()
            
    def insertIntoAccType(userID,UserCA,UserSA,UserCOD,UserMMA,UserIRA):
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor() 
        
        c.execute("Insert INTO AccType(userId, CA, SA, COD, MMA, IRA) VALUES (?,?,?,?,?,?)",(userID,UserCA,UserSA,UserCOD,UserMMA,UserIRA))
        
        conn.commit()
        
        c.close()
        conn.close()
     
    def dynamic_data_entry(username,usermiddlename, usersurname, userpass, housenumber, street, city, postcode, usercreationdate, useracctype, userlastlogintime):  
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("Insert INTO Users(userName, userMiddleName, userSurname, userPass, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(username,usermiddlename, usersurname, userpass, housenumber, street, city, postcode, usercreationdate, useracctype, userlastlogintime))
        conn.commit()
        
        c.close()
        conn.close()
        
    def InsertIntoInterestStart(Interest,Rate):  
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("Insert INTO Interest(Interest, Rate, DateChanged, DateAdded, DateRemoved) VALUES (?,?,?,?,?)",(Interest,Rate,datenow,datenow,''))
        conn.commit()
        
        c.close()
        conn.close()
        
    def updateAdminAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable):  
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("UPDATE Users SET userName = '{}', userMiddleName = '{}', userSurname = '{}', HouseNumber = '{}', Street = '{}', City = '{}', PostCode = '{}', userAccType = '{}' WHERE userId='{}'".format(GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable, GotId))
        conn.commit()
        
        c.close()
        
    def updateUserAcc(GotId,GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable):  
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("UPDATE Users SET userName = '{}', userMiddleName = '{}', userSurname = '{}', HouseNumber = '{}', Street = '{}', City = '{}', PostCode = '{}', userAccType = '{}' WHERE userId='{}'".format(GotNewName, GotNewMiddleName, GotNewSurname, GotNewHouseNumber, GotNewStreet, GotNewCity, GotNewPostCode, GotNewAccountTypeDisable, GotId))
        conn.commit()
        
        c.close()   
        
    def updateBalanceAcc(GotId,GotNewInterest,GotNewOverdraft):  
        print(GotId,GotNewInterest,GotNewOverdraft)
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("UPDATE Balance SET InterestId = '{}' and OverdraftID = '{}' WHERE Balance.userId is {}".format(GotNewInterest,GotNewOverdraft,GotId))
        conn.commit()
        
        c.close()   
    def insertIntoInterest(GotName,GotRate):  
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        c.execute("Insert INTO Interest(Interest, Rate, DateChanged, DateAdded, DateRemoved) VALUES (?,?,?,?,?)",(GotName,GotRate, datenow, datenow, ''))
        conn.commit()
        
        c.close()
        conn.close() 
    
    def UpdateInterest(GotNewName,GotNewRate, GotDisable, GotName):  
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("UPDATE Interest SET Interest = '{}', Rate = '{}', DateChanged = '{}', DateRemoved = '{}' WHERE Interest = '{}'".format(GotNewName,GotNewRate, datenow, GotDisable, GotName))
        conn.commit()
        
        c.close()
        conn.close()
        
        
    def insertIntoInvestments(GotName,GotValue):  
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("Insert INTO Investments(InvestmentName, InvestmentValue, InvestmentDateChanged, InvestmentDateCreated, InvestmentDateRemoved) VALUES (?,?,?,?,?)",(GotName,GotValue, datenow, datenow, ''))
        conn.commit()
        
        c.close()
        conn.close() 
        
    def updateInvestments(GotNewName,GotNewValue, GotDisable, GotName):  
        datenow = str(datetime.datetime.now())
        conn = sqlite3.connect('BankData.db')
        c = conn.cursor()
        
        c.execute("UPDATE Investments SET InvestmentName = '{}', InvestmentValue = '{}', InvestmentDateChanged = '{}', InvestmentDateRemoved = '{}' WHERE InvestmentName='{}'".format(GotNewName,GotNewValue, datenow, GotDisable, GotName))
        conn.commit()
        
        c.close()
        conn.close()
        
    def All_from_db():
        c.execute("SELECT * FROM Users ")
        lis = []
        for row in c.fetchall():
            lis.append(row)
            
        return(lis)
        
    def selectFromUsersSafe():
        c.execute("SELECT userId, userName, userMiddleName, userSurname, HouseNumber, Street, City, PostCode, userCreationDate, userAccType, userLastLoginTime FROM Users")
        lis = []
        for row in c.fetchall():
            lis.append(row)
            
        return(lis)
            
        
    def hash_password(password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
        
    def read_from_db(username, password):
        try:
            checkUN = False
            checkUP = False
            status = ''
            idUser= ''
            
            c.execute("SELECT * FROM Users ")
            for row in c.fetchall():
                if (str(row[1]) == str(username) and (data.check_password(row[4], password))):
                   checkUN = True 
                   checkUP = True
                   status = (str(row[10])).lower()
                   idUser = str(row[0])
                   
                   
            if (checkUN == True and checkUP == True):
               return True, status, idUser
            else:
               return False, status, idUser
       
        except:
            data.create_table()
            BankSystem()
            BankSystem.load_bank_data()
            return True, 'bank', '0'
        
    
def main():  
    app = BankingSystem()
    app.mainloop()
    
if __name__ == '__main__': main()