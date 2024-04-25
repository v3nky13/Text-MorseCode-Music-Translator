from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import mysql.connector as sqltor
from midiutil import MIDIFile
import datetime

mycon=sqltor.connect(host="localhost", user="root", password="mypass")
cursor=mycon.cursor()


def initialization():
    cursor.execute("create database mydb;")
    cursor.execute("use mydb;")
    cursor.execute("create table user(Username char(50),Password char(50), Email_id char(50), Mobile_no char(20));")
    cursor.execute("create table log(Username char(50),Type char(50), DateTime char(20))")
    cursor.execute("create table morsecode(Alnum char(1), Code char(5));")

    cursor.execute("insert into morsecode values('a','.-');")
    cursor.execute("insert into morsecode values('b','-...');")
    cursor.execute("insert into morsecode values('c','-.-.');")
    cursor.execute("insert into morsecode values('d','-..');")
    cursor.execute("insert into morsecode values('e','.');")
    cursor.execute("insert into morsecode values('f','..-.');")
    cursor.execute("insert into morsecode values('g','--.');")
    cursor.execute("insert into morsecode values('h','....');")
    cursor.execute("insert into morsecode values('i','..');")
    cursor.execute("insert into morsecode values('j','.---');")
    cursor.execute("insert into morsecode values('k','-.-');")
    cursor.execute("insert into morsecode values('l','.-..');")
    cursor.execute("insert into morsecode values('m','--');")
    cursor.execute("insert into morsecode values('n','-.');")
    cursor.execute("insert into morsecode values('o','---');")
    cursor.execute("insert into morsecode values('p','.--.');")
    cursor.execute("insert into morsecode values('q','--.-');")
    cursor.execute("insert into morsecode values('r','.-.');")
    cursor.execute("insert into morsecode values('s','...');")
    cursor.execute("insert into morsecode values('t','-');")
    cursor.execute("insert into morsecode values('u','..-');")
    cursor.execute("insert into morsecode values('v','...-');")
    cursor.execute("insert into morsecode values('w','.--');")
    cursor.execute("insert into morsecode values('x','-..-');")
    cursor.execute("insert into morsecode values('y','-.--');")
    cursor.execute("insert into morsecode values('z','--..');")

    cursor.execute("insert into morsecode values('1','.----');")
    cursor.execute("insert into morsecode values('2','..---');")
    cursor.execute("insert into morsecode values('3','...--');")
    cursor.execute("insert into morsecode values('4','....-');")
    cursor.execute("insert into morsecode values('5','.....');")
    cursor.execute("insert into morsecode values('6','-....');")
    cursor.execute("insert into morsecode values('7','--...');")
    cursor.execute("insert into morsecode values('8','---..');")
    cursor.execute("insert into morsecode values('9','----.');")
    cursor.execute("insert into morsecode values('0','-----');")

    mycon.commit()


def login():
    
    def cmd1():
        u=username.get()
        p=password.get()
        cursor.execute("select Username,Password from user;")
        x=cursor.fetchall()
        for i in x:
            if u==i[0]:
                if p==i[1]:
                    login.withdraw()
                    main(u)
                    break
        else:
            messagebox.showinfo("Can't Login","Credentials doesn't match!")

    def cmd2():
        login.withdraw()
        signup()

    login=Tk()
    login.geometry('800x600')
    login.title("Login Page")
    login.iconbitmap(r'icon.ico')
    login.configure(bg="#87CEFA")
    login.resizable(width = False, height = False)
    
    Label(login,text='DATA ENCRYPTION TOOL',font=('Courier New',25,'bold'),bg='light yellow',width=100).pack(pady=(10,0))
    Label(login,text='LOGIN',font=('Courier',50),bg='#87CEFA').pack(pady=(75,0))
    Label(login,text='To Your Account',font=('Courier',14),bg='#87CEFA').pack()
    
    Label(login,text='Username:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(50,3))
    username=Entry(login,width='25')
    username.pack(pady=(5))
    
    Label(login,text='Password:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    password=Entry(login,show="*",width='25')
    password.pack(pady=(5))
    
    Button(login,text='Login',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd1()).pack(pady=(5,50))
    Label(login,text="Don't have an account?",font=('Helvetica',10),bg='#87CEFA').pack()
    Button(login,text='Sign Up',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd2()).pack()
    
    login.mainloop()


def signup():
    
    def cmd1():
        u=username.get()
        p1=password1.get()
        p2=password2.get()
        e=email.get()
        m=mobileno.get()
        cursor.execute("select Username from user;")
        x=cursor.fetchall()
        b=False
        for i in x:
            if u==i[0]:
                b=True
                break
        if not u or not p1 or not p2 or not e or not m:
            messagebox.showinfo("Info. Not Found","Fill all the details!")
        elif b==True:
            messagebox.showinfo("User Already Exits","Username you've entered already exists, try a different one!")
        elif p1!=p2:
            messagebox.showinfo("Password Doesn't Match","Password you've re-entered doesn't match, check the password!")
        elif m.isdigit()==False:
            messagebox.showinfo("Incorrect Mobile No.","Mobile No. shouldn't contain other characters!")
        else:
            sql="insert into user(Username,Password,Email_id,Mobile_no) values(%s,%s,%s,%s)"
            val=[u,p1,e,m]
            cursor.execute(sql,val)
            mycon.commit()
            messagebox.showinfo("Done!","Account created!")
            signup.withdraw()
            login()

    def cmd2():
        signup.withdraw()
        login()

    signup=Tk()
    signup.geometry('800x600')
    signup.title("Sign Up Page")
    signup.iconbitmap(r'icon.ico')
    signup.configure(bg="#87CEFA")
    signup.resizable(width = False, height = False)
    
    Label(signup,text='DATA ENCRYPTION TOOL',font=('Courier New',25,'bold'),bg='light yellow',width=100).pack(pady=(10,0))
    Label(signup,text='SIGNUP',font=('Courier',50),bg='#87CEFA').pack(pady=(25,0))
    Label(signup,text='Your New Account',font=('Courier',14),bg='#87CEFA').pack()
    
    Label(signup,text='Username:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(25,3))
    username=Entry(signup,width='25')
    username.pack(pady=(5))
    
    Label(signup,text='Password:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    password1=Entry(signup,show="*",width='25')
    password1.pack(pady=(5))

    Label(signup,text='Re-enter Password:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    password2=Entry(signup,show="*",width='25')
    password2.pack(pady=(5))
    
    Label(signup,text='Email:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    email=Entry(signup,width='25')
    email.pack(pady=(5))
    
    Label(signup,text='Mobile No:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    mobileno=Entry(signup,width='25')
    mobileno.pack(pady=(5))
    
    Button(signup,text='Create Account',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd1()).pack(pady=(5,10))
    Button(signup,text='Login Page',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd2()).pack(padx=(650,0))

    signup.mainloop()


def account(user):
    
    def cmd1():
        account.withdraw()
        edit(u)
        
    def cmd2():
        account.withdraw()
        login()

    def cmd3():
        sql1="delete from user where Username=%s;"
        sql2="delete from log where Username=%s;"
        val=[u]
        cursor.execute(sql1,val)
        cursor.execute(sql2,val)
        mycon.commit()
        messagebox.showinfo("Done!","Your account have been deleted!")
        account.withdraw()
        login()

    def cmd4():
        logs.delete(1.0,END)
        sql="delete from log where Username=%s;"
        val=[u]
        cursor.execute(sql,val)
        mycon.commit()
        messagebox.showinfo("Done!","Your logs have been cleared!")

    def cmd5():
        account.withdraw()
        main(u)

    u=user
    account=Tk()
    account.geometry('800x650')
    account.title("Your Account")
    account.iconbitmap(r'icon.ico')
    account.configure(bg="#87CEFA")
    account.resizable(width = False, height = False)

    sql="select Type,DateTime from log where Username=%s"
    val=[u]
    cursor.execute(sql,val)
    y=cursor.fetchall()
    lg=""
    for i in range(-1,-len(y)-1,-1):
        for j in y[i]:
            lg+=j+' '
        lg+='\n'
    
    cursor.execute("select * from user;")
    x=cursor.fetchall()
    for i in x:
        if u==i[0]:
            e="Email: "+i[2]
            m="Mobile No: "+i[3]
    
    Label(account,text='DATA ENCRYPTION TOOL',font=('Courier New',25,'bold'),bg='light yellow',width=100).pack(pady=(10,0))
    Label(account,text=u,font=('Courier',50),bg='#87CEFA').pack(pady=(10,0))
    Label(account,text=e,font=('Courier',14),bg='#87CEFA').pack()
    Label(account,text=m,font=('Courier',14),bg='#87CEFA').pack()

    Button(account,text='Edit',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd1()).pack()
    Button(account,text='Sign Out',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd2()).pack()
    Button(account,text='Delete Account',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd3()).pack()
    
    Label(account,text="LOGS",font=('Courier New',15,'bold'),bg='light yellow',width=60).pack(pady=(10,10))
    logs=scrolledtext.ScrolledText(account,width=90,height=16)
    logs.pack()
    logs.insert(INSERT,lg)
    
    Button(account,text='Clear Logs',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd4()).pack()
    Button(account,text='Back',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd5()).pack(padx=(650,0))
    
    account.mainloop()


def edit(user):
    
    def cmd1():
        u=username.get()
        p1=password1.get()
        p2=password2.get()
        e=email.get()
        m=mobileno.get()
        cursor.execute("select Username from user;")
        x=cursor.fetchall()
        if not u or not p1 or not p2 or not e or not m:
            messagebox.showinfo("Info. Not Found","Fill all the details!")
        elif p1!=p2:
            messagebox.showinfo("Password Doesn't Match","Password you've re-entered doesn't match, check the password!")
        elif m.isdigit()==False:
            messagebox.showinfo("Incorrect Mobile No.","Mobile No. shouldn't contain other characters!")
        else:
            sql1="update user set Username=%s,Password=%s,Email_id=%s,Mobile_no=%s where Username=%s"
            val1=[u,p1,e,m,u1]
            sql2="update log set Username=%s where Username=%s"
            val2=[u,u1]
            cursor.execute(sql1,val1)
            cursor.execute(sql2,val2)
            mycon.commit()
            messagebox.showinfo("Done!","Account details saved!")
            edit.withdraw()
            account(u)

    def cmd2():
        edit.withdraw()
        account(u)

    u1=u=user
    cursor.execute("select * from user;")
    x=cursor.fetchall()
    for i in x:
        if u==i[0]:
            p,e1,m1=i[1],i[2],i[3]

    edit=Tk()
    edit.geometry('800x600')
    edit.title("Edit Your Account")
    edit.iconbitmap(r'icon.ico')
    edit.configure(bg="#87CEFA")
    edit.resizable(width = False, height = False)
    
    Label(edit,text='DATA ENCRYPTION TOOL',font=('Courier New',25,'bold'),bg='light yellow',width=100).pack(pady=(10,0))
    Label(edit,text='EDIT',font=('Courier',50),bg='#87CEFA').pack(pady=(25,0))
    Label(edit,text='Your Account Details',font=('Courier',14),bg='#87CEFA').pack()
    
    Label(edit,text='New Username:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(25,3))
    username=Entry(edit,width='25')
    username.pack(pady=(5))
    username.insert(0,u)
    
    Label(edit,text='New Password:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    password1=Entry(edit,show="*",width='25')
    password1.pack(pady=(5))
    password1.insert(0,p)
    
    Label(edit,text='Re-enter New Password:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    password2=Entry(edit,show="*",width='25')
    password2.pack(pady=(5))
    password2.insert(0,p)
    
    Label(edit,text='New Email:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    email=Entry(edit,width='25')
    email.pack(pady=(5))
    email.insert(0,e1)
    
    Label(edit,text='New Mobile No:',font=('Courier',12,'bold'),bg='#87CEFA').pack(pady=(3))
    mobileno=Entry(edit,width='25')
    mobileno.pack(pady=(5))
    mobileno.insert(0,m1)
    
    Button(edit,text='Save Details',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd1()).pack(pady=(5,10))
    Button(edit,text='Back',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd2()).pack(padx=(650,0))

    edit.mainloop()

    
def main(user):
    
    def cmd1():
        main.withdraw()
        account(u)

    def cmd2():
        c=cb.get()
        e=entry.get(1.0,END)
        e=e.lower()
        cursor.execute("select * from morsecode;")
        x=cursor.fetchall()
        o=""
        date=str(datetime.datetime.today())
        date=date[:19]
        
        if c==ls[0]:
            l=e.split()
            for i in l:
                for j in i:
                    for k in x:
                        if j==k[0]:
                            o+=k[1]
                            break
                    o+=" "
                o+="/ "
                
            output.delete(1.0,END)
            output.insert(INSERT,o)
            
        elif c==ls[1]:
            l=e.split("/")
            for i in l:
                l1=i.split()
                for j in l1:
                    for k in x:
                        if j==k[1]:
                            o+=k[0]
                            break
                o+=" "
                
            output.delete(1.0,END)
            output.insert(INSERT,o)
            
        elif c==ls[2]:
            s=[]
            l=e.split()
            for i in l:
                for j in i:
                    for k in x:
                        if j==k[0]:
                            m=k[1]
                            c1=59
                            for a in m:
                                if a==".":
                                    s.append(c1+1)
                                    c1=c1+1
                                elif a=="-":
                                    s.append(c1+2)
                                    c1=c1+2
                            break
                    s.append(0)
                s.append(0)
            for i in range(len(s)):
                if s[i]==0:
                    s[i]=58
                s[i]+=26

            track=0
            channel=0
            time=0
            duration=10
            tempo=250
            volume=100

            MyMIDI = MIDIFile(1)
            MyMIDI.addTempo(track, time, tempo)

            for i, pitch in enumerate(s):
                MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

            with open("saved_sound.mid", "wb") as f:
                MyMIDI.writeFile(f)

            messagebox.showinfo("Done!","Sound file saved!")

        elif c==ls[3]:
            s=[]
            m=""
            l=e.split("/")
            for i in l:
                l1=i.split()
                for j in l1:
                    c1=59
                    for a in j:
                        if a==".":
                            s.append(c1+1)
                            c1=c1+1
                        elif a=="-":
                            s.append(c1+2)
                            c1=c1+2
            
            for i in range(len(s)):
                if s[i]==0:
                    s[i]=58
                s[i]+=26

            track=0
            channel=0
            time=0
            duration=10
            tempo=250
            volume=100

            MyMIDI = MIDIFile(1)
            MyMIDI.addTempo(track, time, tempo)

            for i, pitch in enumerate(s):
                MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

            with open("saved_sound.mid", "wb") as f:
                MyMIDI.writeFile(f)

            messagebox.showinfo("Done!","Sound file saved!")

        sql="insert into log values(%s,%s,%s);"
        val=[u,c,date]
        cursor.execute(sql,val)
        mycon.commit()

    def cmd3():
        o=output.get(1.0,END)
        f=open("saved_output.txt",'w')
        f.write(o)
        f.close()
        messagebox.showinfo("Done!","File saved!")
        
    def cmd4():
        main.withdraw()
        login()

    u=user
    ls=['Text to Morse Code','Morse Code to Text','Text to Sound','Morse Code to Sound']

    main=Tk()
    main.geometry('800x700')
    main.title("Main Page")
    main.iconbitmap(r'icon.ico')
    main.configure(bg="#87CEFA")
    main.resizable(width = False, height = False)
    
    Label(main,text='DATA ENCRYPTION TOOL',font=('Courier New',25,'bold'),bg='light yellow',width=100).pack(pady=(10,10))
    Button(main,text="Your Account",font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd1()).pack(padx=(700,0))
    Label(main,text="Enter your message here:",font=('Courier New',12),bg='#87CEFA').pack(padx=(0,500))
    
    entry=scrolledtext.ScrolledText(main,width=90,height=13)
    entry.pack()

    cb=ttk.Combobox(main,values=ls)
    cb.pack(pady=(10,0))
    cb.set(ls[0])

    Button(main,text='Convert',font=('Ariel',11),bd=1,bg='light yellow',activebackground='light yellow',command=lambda:cmd2()).pack(pady=(10,10))

    output=scrolledtext.ScrolledText(main,width=90,height=13)
    output.pack()
    
    Button(main,text='Save as File',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd3()).pack(pady=(5,5))
    Button(main,text='Login Page',font=('Helvetica',10,'underline'),bd=0,bg='#87CEFA',activebackground='#87CEFA',command=lambda:cmd4()).pack(padx=(650,0))
    
    main.mainloop()


try:
    initialization()
    signup()
except:  
    cursor.execute("use mydb;")
    login()
