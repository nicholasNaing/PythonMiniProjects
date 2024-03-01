from ast import Delete
from tkinter import *
from PIL import Image,ImageTk
win=Tk()
win.configure(bg='azure')

blank=Label(win,text='',width=120,fg='white',bg='azure').pack()

head=Label(win,text='Restaurant Menu',font=('Avalon',15,'bold'),bg='azure',width=100).pack()

subhead=Label(win,text='Fast  Foods',font=('Avalon',12,'bold'),padx=400,pady=10,bg='azure').pack(side=TOP,anchor=W)

titles=Frame(win,width=900,height=50,padx=90,pady=10,bg='#fff1cf')
titles.pack(side=TOP,anchor=W,fill=X)
menu=Label(titles,text='MENU',width=10,font=('Garamond',12,'bold'),bg='#fff1cf').grid(row=0,column=0)
tag=Label(titles,text='Price Tag',width=10,padx=100,font=('Garamond',12,'bold'),bg='#fff1cf').grid(row=0,column=1)
piece=Label(titles,text='Pcs',width=4,font=('Garamond',12,'bold'),bg='#fff1cf').grid(row=0,column=2)

main=LabelFrame(win,text='',pady=7 ,bg='#dd1a05')
main.pack(side=LEFT,anchor=N,fill=X)

burg_bill = 0
pcs_burg = 0
def burger(fee):
    global pcs_burg,burg_bill
    pcs_burg=int(burg_spin.get())
    if pcs_burg==0 :
        burg_bill = (fee*pcs_burg)
        return burg_bill
    else :
        burg_bill= (fee*pcs_burg)
        burg_cart['state']=DISABLED
        burg_cart['text']='Ordered'
        burg_cart['bg']='black'
        burg_bill= int((fee*pcs_burg))

def cancel_burg():
    global pcs_burg,burg_bill
    if (pcs_burg!=0 and burg_cart['state']==DISABLED) :
        var_burg.set(0)
        pcs_burg=0
        burg_bill=0
        burg_cart['state']=NORMAL
        burg_cart['text']='Order'
        burg_cart['bg']='white'
        
    else :
        burg_cart['state']=NORMAL

fast1=LabelFrame(main,text='',width=900,height=70,bg='#ffae24',padx=20,pady=10)
fast1.grid(row=0,column=0,padx=5,pady=5)
burg=Label(fast1,text='Hamburgur',bg='#ffae24',padx=20,pady=15,width=10,font=('Avalon',11,'bold')).grid(row=0,column=0,rowspan=2)
burger_img=ImageTk.PhotoImage(Image.open('burger.jpg').resize((100,60)))
burg=Label(fast1,image=burger_img,width=100,font=('Avalon',11,'bold')).grid(row=0,column=1)
burg_price=Label(fast1,text='Price - $5,000 kyats',bg='#ffae24',width=15,padx=40,pady=15,font=('Paramore',11,'bold')).grid(row=0,column=2)
var_burg=IntVar()
burg_spin=Spinbox(fast1,from_=0,to=100,textvariable=var_burg,width=10,relief=SOLID,justify=CENTER,font=('Garamond',13,'bold'))
burg_spin.grid(row=0,column=3)
burg_blank=Label(fast1,text='',bg='#ffae24',width=6).grid(row=0,column=4)
burg_cart=Button(fast1,text='Order',command=lambda : burger(5000),width=5,padx=20,font=('Avalon',10,'bold'))
burg_cart.grid(row=0,column=5)
burg_blank=Label(fast1,text='',bg='#ffae24',width=1).grid(row=0,column=6)
burg_cancel=Button(fast1,text='Cancel',command=cancel_burg,width=5,padx=20,font=('Avalon',10,'bold'))
burg_cancel.grid(row=0,column=7)

pizz_bill=0
pcs_pizz = 0
def pizza(fee):
    global pcs_pizz,pizz_bill  
    pcs_pizz=int(pizz_spin.get())
    if pcs_pizz==0 :
        pizz_bill = (fee*pcs_pizz)
        return pizz_bill
    else :
        pizz_bill= (fee*pcs_pizz)
        pizz_cart['state']=DISABLED
        pizz_cart['text']='Ordered'
        pizz_cart['bg']='black'
        pizz_bill= int((fee*pcs_pizz))

def cancel_pizz():
    global pizz_bill,pcs_pizz
    if (pcs_pizz!=0 and pizz_cart['state']==DISABLED) :
        var_pizz.set(0)
        pizz_bill=0
        pizz_cart['state']=NORMAL
        pizz_cart['text']='Order'
        pizz_cart['bg']='white'
        pcs_pizz = 0
    
        
    else :
        pizz_cart['state']=NORMAL

fast2=LabelFrame(main,text='',bg='#ffae24',width=900,height=70,padx=20,pady=10)
fast2.grid(row=1,column=0,padx=5,pady=5)
pizza_lab=Label(fast2,text='Pizza',bg='#ffae24',padx=20,pady=17,width=10,font=('Avalon',11,'bold')).grid(row=0,column=0)
pizza_img=ImageTk.PhotoImage(Image.open('pizza.jpg').resize((100,60)))
pizz=Label(fast2,image=pizza_img,width=100,font=('Avalon',11,'bold')).grid(row=0,column=1)
pizz_price=Label(fast2,text='Price - $14,000 kyats',bg='#ffae24',width=15,padx=40,pady=15,font=('Paramore',11,'bold')).grid(row=0,column=2)
var_pizz=IntVar()
pizz_spin=Spinbox(fast2,from_=0,to=100,textvariable=var_pizz,width=10,relief=SOLID,justify=CENTER,font=('Garamond',13,'bold'))
pizz_spin.grid(row=0,column=3)
var_pizz.set(0)
pizz_blank=Label(fast2,text='',bg='#ffae24',width=6).grid(row=0,column=4)
pizz_cart=Button(fast2,text='Order',command=lambda : pizza(14000),width=5,padx=20,font=('Avalon',10,'bold'))
pizz_cart.grid(row=0,column=5)
pizz_blank=Label(fast2,text='',bg='#ffae24',width=1).grid(row=0,column=6)
pizz_cancel=Button(fast2,text='Cancel',command=cancel_pizz,width=5,padx=20,font=('Avalon',10,'bold'))
pizz_cancel.grid(row=0,column=7)

chick_bill = 0
pcs_chick = 0
def chicken(fee):
    global pcs_chick,chick_bill
    pcs_chick=int(chick_spin.get())
    if pcs_chick==0 :
        chick_bill = (fee*pcs_chick)
        return chick_bill
    else :
        chick_bill= (fee*pcs_chick)
        chick_cart['state']=DISABLED
        chick_cart['text']='Ordered'
        chick_cart['bg']='black'
        chick_bill= int((fee*pcs_chick))

def cancel_chick():
    global pcs_chick,chick_bill
    if (pcs_chick!=0 and chick_cart['state']==DISABLED) :
        var_chick.set(0)
        pcs_chick = 0
        chick_bill = 0
        chick_cart['state']=NORMAL
        chick_cart['text']='Order'
        chick_cart['bg']='white'
        
    else :
        chick_cart['state']=NORMAL

fast3=LabelFrame(main,text='',bg='#ffae24',width=900,height=70,padx=20,pady=10)
fast3.grid(row=2,column=0,padx=5,pady=5)
chicken_lab=Label(fast3,text='Fried Chicken',bg='#ffae24',padx=20,pady=17,width=10,font=('Avalon',11,'bold')).grid(row=0,column=0)
chicken_img=ImageTk.PhotoImage(Image.open('chicken.jpg').resize((100,60)))
chick=Label(fast3,image=chicken_img,width=100,font=('Avalon',11,'bold')).grid(row=0,column=1)
chick_price=Label(fast3,text='Price - $4,500 kyats',bg='#ffae24',width=15,padx=40,pady=15,font=('Paramore',11,'bold')).grid(row=0,column=2)
var_chick=IntVar()
chick_spin=Spinbox(fast3,from_=0,to=100,textvariable=var_chick,width=10,relief=SOLID,justify=CENTER,font=('Garamond',13,'bold'))
chick_spin.grid(row=0,column=3)
var_chick.set(0)
chick_blank=Label(fast3,text='',bg='#ffae24',width=6).grid(row=0,column=4)
chick_cart=Button(fast3,text='Order',command=lambda : chicken(4500),width=5,padx=20,font=('Avalon',10,'bold'))
chick_cart.grid(row=0,column=5)
chick_blank=Label(fast3,text='',bg='#ffae24',width=1).grid(row=0,column=6)
chick_cancel=Button(fast3,text='Cancel',command=cancel_chick,width=5,padx=20,font=('Avalon',10,'bold'))
chick_cancel.grid(row=0,column=7)

nugg_bill = 0
pcs_nugg = 0
def nuggets(fee):
    global pcs_nugg,nugg_bill
    pcs_nugg=int(nugg_spin.get())
    if pcs_nugg==0 :
        nugg_bill = (fee*pcs_nugg)
        return nugg_bill
    else :
        nugg_bill= (fee*pcs_nugg)
        nugg_cart['state']=DISABLED
        nugg_cart['text']='Ordered'
        nugg_cart['bg']='black'
        nugg_bill= int((fee*pcs_nugg))

def cancel_nugg():
    global pcs_nugg,nugg_bill
    if (pcs_nugg!=0 and nugg_cart['state']==DISABLED) :
        var_nugg.set(0)
        pcs_bugg = 0
        nugg_bill = 0
        nugg_cart['state']=NORMAL
        nugg_cart['text']='Order'
        nugg_cart['bg']='white'
        
    else :
        nugg_cart['state']=NORMAL

fast4=LabelFrame(main,text='',bg='#ffae24',width=900,height=70,padx=20,pady=10)
fast4.grid(row=3,column=0,padx=5,pady=5)
nuggets_lab=Label(fast4,text='Nuggets',bg='#ffae24',padx=20,pady=17,width=10,font=('Avalon',11,'bold')).grid(row=0,column=0)
nuggets_img=ImageTk.PhotoImage(Image.open('nuggets.jpg').resize((100,60)))
nugg=Label(fast4,image=nuggets_img,width=100,font=('Avalon',11,'bold')).grid(row=0,column=1)
var_nugg=IntVar()
nugg_price=Label(fast4,text='Price - $7,000 kyats',bg='#ffae24',width=15,padx=40,pady=15,font=('Paramore',11,'bold')).grid(row=0,column=2)
nugg_spin=Spinbox(fast4,from_=0,to=100,textvariable=var_nugg,width=10,relief=SOLID,justify=CENTER,font=('Garamond',13,'bold'))
nugg_spin.grid(row=0,column=3)
var_nugg.set(0)
nugg_blank=Label(fast4,text='',bg='#ffae24',width=6).grid(row=0,column=4)
nugg_cart=Button(fast4,text='Order',command=lambda : nuggets(7000),width=5,padx=20,font=('Avalon',10,'bold'))
nugg_cart.grid(row=0,column=5)
nugg_blank=Label(fast4,text='',bg='#ffae24',width=1).grid(row=0,column=6)
nugg_cancel=Button(fast4,text='Cancel',command=cancel_nugg,width=5,padx=20,font=('Avalon',10,'bold'))
nugg_cancel.grid(row=0,column=7)

sand_bill = 0
pcs_sand= 0
def sandw(fee):
    global pcs_sand,sand_bill
    pcs_sand = 0 
    pcs_sand=int(sand_spin.get())
    sand_bill=(fee*pcs_sand)    
    if pcs_sand != 0 :
        sand_bill= (fee*pcs_sand)
        sand_cart['state']=DISABLED
        sand_cart['text']='Ordered'
        sand_cart['bg']='black'
        sand_bill= int((fee*pcs_sand))
        

def cancel_sand():
    global pcs_sand,sand_bill
    if (pcs_sand!=0 and sand_cart['state']==DISABLED) :
        var_sand.set(0)
        pcs_sand = 0
        sand_bill = 0
        sand_cart['state']=NORMAL
        sand_cart['text']='Order'
        sand_cart['bg']='white'
    else :
        sand_cart['state']=NORMAL

fast5=LabelFrame(main,text='',bg='#ffae24',width=900,height=70,padx=20,pady=10)
fast5.grid(row=4,column=0,padx=5,pady=5)
sandwich=Label(fast5,text='Sandwich',bg='#ffae24',padx=20,pady=17,width=10,font=('Avalon',11,'bold')).grid(row=0,column=0)
sandwich_img=ImageTk.PhotoImage(Image.open('sandwich.jpg').resize((100,60)))
sand=Label(fast5,image=sandwich_img,width=100,font=('Avalon',11,'bold')).grid(row=0,column=1)
var_sand=IntVar()
sand_price=Label(fast5,text='Price - $3,000 kyats',bg='#ffae24',width=15,padx=40,pady=15,font=('Paramore',11,'bold')).grid(row=0,column=2)
sand_spin=Spinbox(fast5,from_=0,to=100,textvariable=var_sand,width=10,relief=SOLID,justify=CENTER,font=('Garamond',13,'bold'))
sand_spin.grid(row=0,column=3)
var_sand.set(0)
sand_blank=Label(fast5,text='',bg='#ffae24',width=6).grid(row=0,column=4)
sand_cart=Button(fast5,text='Order',command=lambda : sandw(3000),width=5,padx=20,font=('Avalon',10,'bold'))
sand_cart.grid(row=0,column=5)
sand_blank=Label(fast5,text='',bg='#ffae24',width=1).grid(row=0,column=6)
sand_cancel=Button(fast5,text='Cancel',command=cancel_sand,width=5,padx=20,font=('Avalon',10,'bold'))
sand_cancel.grid(row=0,column=7)



def voucher():
    all_menus = [
    (pcs_burg,'Hamburger',burg_bill),  #This has to be inside this function cuz only after we click the total button
    (pcs_pizz,'Pizza',pizz_bill),      #the totals are calculate and pcs and bill are only come out by then
    (pcs_chick,'Fried Chicken',chick_bill),#So if this array is outside of the function, pcs and bills will only br zero as calculations are not done yet
    (pcs_nugg,'Nuggets',nugg_bill),
    (pcs_sand,'Sandwich',sand_bill)
]
    global bill
    if total_bill != 0 :
        bill=LabelFrame(win)
        bill.pack(side=LEFT,anchor=N)
        name=Label(bill,text='Expensimo\'s Foodbar',padx=0,pady=10,font=('Avalon',13,'bold'))
        name.grid(row=0,column=0,columnspan=3)
        thanks=Label(bill,text='Thank you for chossing us',font=('Avalon',11,'bold')).grid(row=1,column=0,columnspan=3)
        items=LabelFrame(bill)
        items.grid(row=2,column=0,pady=10,columnspan=3)
        list=Label(items,text='List of items',font=('Avalon',11,'bold'),padx=1,pady=11).pack(side=LEFT,padx=15)
        list=Label(items,text='Quantity',font=('Avalon',11,'bold'),padx=1,pady=11).pack(side=LEFT,padx=40)
        list=Label(items,text='Amount',font=('Avalon',11,'bold'),padx=1,pady=11).pack(side=LEFT,padx=15)
        r=3
        for i in all_menus :
            if i[2]!=0 :
                menu=Label(bill,text=(i[1]),font=('Avalon',11,'bold'),padx=1,pady=11).grid(row=r,column=0)
                quantity = Label(bill,text=f'x {i[0]}',font=('Avalon',11,'bold'),padx=50,pady=11).grid(row=r,column=1)
                amount = Label(bill,text=f'{i[2]}ks',font=('Avalon',11,'bold'),padx=1,pady=11).grid(row=r,column=2)
                r+=1
        final_bill=LabelFrame(bill,pady=10)
        final_bill.grid(row=r+1,column=0,columnspan=3,pady=(20,3))
        final_cost_lab=Label(final_bill,text='Cost of the orders - ',font=('Avalon',11,'bold')).grid(row=0,column=1,padx=(10,10))
        final_tax_lab=Label(final_bill,text='Tax(2%) - ',font=('Avalon',11,'bold')).grid(row=1,column=1,padx=(10,10))
        final_cost=Label(final_bill,text=f'{total_bill}ks',font=('Avalon',11,'bold')).grid(row=0,column=2,padx=(55,45))
        final_tax=Label(final_bill,text=f'{tax}ks',font=('Avalon',11,'bold')).grid(row=1,column=2,padx=(55,45))

        final_cost_lab=Label(bill,text='Total Cost',font=('Avalon',11,'bold')).grid(row=r+2,column=1)
        final_cost=Label(bill,text=f'{float(total_bill+tax)}ks',font=('Avalon',11,'bold')).grid(row=r+2,column=2)
        bill_button['state']=DISABLED
        bill_button['bg']='grey'
def all_reset():
    cancel_burg()
    cancel_pizz()
    cancel_chick()
    cancel_nugg()
    cancel_sand()
    bill_button['state']=NORMAL
    bill_button['bg']='#66ff00'
    bill.destroy()

def total_price():
    global total_bill,tax
    total_bill=(burg_bill + pizz_bill + chick_bill + nugg_bill + sand_bill)
    tax = total_bill*(2/100)
    voucher()

bill_button=Button(win,text='Total',font=('Avalon',11,'bold'),fg='#000000',bg='#66ff00',command=total_price)
bill_button.pack(side=TOP,anchor=W,fill=X)
reset_button=Button(win,text='Reset',font=('Avalon',11,'bold'),fg='#ffffff',bg='#ff2c2c',command=all_reset)
reset_button.pack(side=TOP,pady=(3,0),anchor=W,fill=X)

# Set the window geometry to fill the screen
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry(f"{screen_width}x{screen_height}+0+0")


win.mainloop()



