import tkinter                                           #tkinter is used for GUI(graphic user interface)
m=tkinter.Tk()                                           #creates main window where m is the main window
m.geometry("220x300")                                    #set the size of the window
def display(a):
    entry.insert("end",a)                                #inserts a at the end of entry, hence displays one after the other
def clear():
    entry.delete(0,"end")                                #deletes entry from starting to end, hence clearing
def calculate():
    a=entry.get()                                        #stores the entry string in a 
    for i in range(0,len(a)):
        if(a[i]=="+"):
            result=float(a[:i])+float(a[i+1:])           #adds the number before "+" and after "+"
        elif(a[i]=="-"):
            result=float(a[:i])-float(a[i+1:])           #subtracts the number before "-" and after "-"
        elif(a[i]=="x"):
            result=float(a[:i])*float(a[i+1:])           #multiplies the number before "x" and after "x"
        elif(a[i]=="/"):
            result=float(a[:i])/float(a[i+1:])           #divides the number before "/" and after "/"
        else:
            pass                                         #eat 5 stars and do nothing ;)
    entry.delete(0,"end")                                #clears entry
    entry.insert(0,result)                               #inserts result as output
entry=tkinter.Entry(m)                                   #creates entry for inputing data from user
entry.place(x=0,y=0)                                     
button1=tkinter.Button(m,text="1",width=4,height=2,relief="ridge",bd=5,command=lambda:display("1"))
button1.place(x=10,y=60)
button2=tkinter.Button(m,text="2",width=4,height=2,relief="ridge",bd=5,command=lambda:display("2"))
button2.place(x=60,y=60)
button3=tkinter.Button(m,text="3",width=4,height=2,relief="ridge",bd=5,command=lambda:display("3"))
button3.place(x=110,y=60)
button_div=tkinter.Button(m,text="/",width=4,height=2,relief="ridge",bd=5,command=lambda:display("/"))
button_div.place(x=160,y=60)
button4=tkinter.Button(m,text="4",width=4,height=2,relief="ridge",bd=5,command=lambda:display("4"))
button4.place(x=10,y=110)
button5=tkinter.Button(m,text="5",width=4,height=2,relief="ridge",bd=5,command=lambda:display("5"))
button5.place(x=60,y=110)
button6=tkinter.Button(m,text="6",width=4,height=2,relief="ridge",bd=5,command=lambda:display("6"))
button6.place(x=110,y=110)
button_mul=tkinter.Button(m,text="x",width=4,height=2,relief="ridge",bd=5,command=lambda:display("x"))
button_mul.place(x=160,y=110)
button7=tkinter.Button(m,text="7",width=4,height=2,relief="ridge",bd=5,command=lambda:display("7"))
button7.place(x=10,y=160)
button8=tkinter.Button(m,text="8",width=4,height=2,relief="ridge",bd=5,command=lambda:display("8"))
button8.place(x=60,y=160)
button9=tkinter.Button(m,text="9",width=4,height=2,relief="ridge",bd=5,command=lambda:display("9"))
button9.place(x=110,y=160)
button_sub=tkinter.Button(m,text="-",width=4,height=2,relief="ridge",bd=5,command=lambda:display("-"))
button_sub.place(x=160,y=160)
buttonC=tkinter.Button(m,text="C",width=4,height=2,relief="ridge",bd=5,command=lambda:clear())              #clears entry
buttonC.place(x=10,y=210)
button0=tkinter.Button(m,text="0",width=4,height=2,relief="ridge",bd=5,command=lambda:display("0"))
button0.place(x=60,y=210)
button_equal=tkinter.Button(m,text="=",width=4,height=2,relief="ridge",bd=5,command=lambda:calculate())     #will display output after clearing the whole entry
button_equal.place(x=110,y=210)
button_plus=tkinter.Button(m,text="+",width=4,height=2,relief="ridge",bd=5,command=lambda:display("+"))
button_plus.place(x=160,y=210)

m.mainloop()                                                                                                #when you want to run your application



