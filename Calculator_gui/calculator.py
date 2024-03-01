from tkinter import *

root=Tk()
root.title('Calculator')
root.configure(bg='#C6C6C6')

frame=LabelFrame(root,padx=10,pady=10,bg='#000000')
frame.pack(padx=10,pady=10)
entry=Entry(frame,width=30,bg='#C6C6C6',bd=4,font=('Avalon',12,'bold'))
entry.grid(row=0,column=0,columnspan=3)

def num(num):
    entry.delete(100,END)
    entry.insert(100,num)

def plus():
    numf=entry.get()
    global first
    first=numf
    global math
    math='addition'
    entry.delete(0, END)

def sub():
    numf=entry.get()
    global first
    first=numf
    global math
    math='substraction'
    entry.delete(0, END)

def multi():
    numf=entry.get()
    global first
    first=numf
    global math
    math='multiplication'
    entry.delete(0, END)

def div():
    numf=entry.get()
    global first
    first=numf
    global math
    math='division'
    entry.delete(0, END)
    

def clear():
    entry.delete(0,END)

def equal():
    nums=entry.get()
    global second
    second=nums
    if math=='addition':
        entry.delete(0,END)
        total = float(first)+float(second)
        entry.insert(0,float(total))
    
    if math=='substraction':
        entry.delete(0,END)
        total = float(first)-float(second)
        entry.insert(0,float(total))
    
    if math=='multiplication':
        entry.delete(0,END)
        total = float(first)*float(second)
        entry.insert(0,float(total))
    
    if math=='division':
        entry.delete(0,END)
        total = float(first)/float(second)
        entry.insert(0,float(total))


but7=Button(frame,text='7',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(7),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=1,column=0)
but8=Button(frame,text='8',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(8),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=1,column=1)
but9=Button(frame,text='9',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(9),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=1,column=2)
but4=Button(frame,text='4',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(4),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=2,column=0)
but5=Button(frame,text='5',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(5),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=2,column=1)
but6=Button(frame,text='6',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(6),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=2,column=2)
but1=Button(frame,text='1',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(1),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=3,column=0)
but2=Button(frame,text='2',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(2),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=3,column=1)
but3=Button(frame,text='3',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(3),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=3,column=2)
but0=Button(frame,text='0',font=('Garamond',10,'bold'),relief='solid',command=lambda : num(0),activebackground='skyblue',padx=35,pady=20,borderwidth=5,fg='white',bg='#0c164f').grid(row=4,column=0)


buttot=Button(frame,text='=',command=equal,relief='solid',font=('Garamond',10,'bold'),activebackground='skyblue',padx=82,pady=20,borderwidth=5,fg='white',bg='#292930').grid(row=4,column=1,columnspan=2)
butmul=Button(frame,text='×',command=multi,relief='solid',font=('Garamond',10,'bold'),activebackground='white',padx=38.5,pady=30,borderwidth=1,fg='white',bg='#292930').grid(row=3,column=3)
butdiv=Button(frame,text='÷',command=div,relief='solid',font=('Avalon',10,'bold'),activebackground='white',padx=40,pady=30,borderwidth=1,fg='white',bg='#292930').grid(row=4,column=3)
butC=Button(frame,text='C',command=clear,relief='solid',font=('Garamond',10,'bold'),activebackground='white',padx=38.5,pady=30,borderwidth=1,fg='white',bg='#292930').grid(row=0,column=3)
butp=Button(frame,text='+',command=plus,relief='solid',font=('Garamond',10,'bold'),activebackground='white',padx=38.5,pady=30,borderwidth=1,fg='white',bg='#292930').grid(row=1,column=3)
butm=Button(frame,text='_',command=sub,relief='solid',font=('Garamond',10,'bold'),activebackground='white',padx=40,pady=30,borderwidth=1,fg='white',bg='#292930').grid(row=2,column=3)

root.mainloop()
