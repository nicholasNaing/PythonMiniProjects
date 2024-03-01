from tkinter import *
import qrcode
from PIL import Image,ImageTk
import tkinter.messagebox
import tkinter.filedialog

main=Tk()
main.title('Small Tools')
main.configure(bg='#C6C6C6')
root=LabelFrame(main,padx=10,pady=10,bg='#000000')
root.pack(padx=20,pady=20,side=TOP,anchor=W)
blank=Label(root,text='',bg='#000000').grid(row=0,column=0,columnspan=3)

head=Label(root,text='Change to Qr code',font=('Avalon',12,'bold'),bg='#000000',fg='#ffffff').grid(row=1,column=0,columnspan=3)

blank=Label(root,text='',bg='#000000').grid(row=2,column=0)

intruction=Label(root,text='URL link',bg='#000000',fg='#ffffff',font=('Avalon',10,'bold')).grid(row=3,column=0)

blank=Label(root,text='-',bg='#000000',fg='#ffffff',padx=20).grid(row=3,column=1)

get_src=Entry(root,width=40,bd=3,fg='#ffffff',bg='#000000')
get_src.grid(row=3,column=2)

blank=Label(root,text='',bg='#000000',fg='#ffffff').grid(row=4,column=0)
def image():
    img=Image.open(qr_name)
    img.show()
    

def change_qr(event=None):
    global qr_name
    raw_name=get_name.get()
    path='C:\\Users\\LENOVO\\Documents\\QR_codes\\'
    qr_name=path+raw_name+'.png'
    code=qrcode.make(get_src.get())
    code.save(qr_name,'PNG')
    info=tkinter.messagebox.showinfo('Complete','Converting Qr code is complete')
    root1.destroy()
    image()

def name(event=None):
    if len(get_src.get())!=0:
        global root1
        root1=Tk()
        root1.title('Qr code maker')
        root1.geometry('300x150')
        root1.configure(bg='#000000')
        blank=Label(root1,text='',bg='#000000').pack()
        command=Label(root1,text='Type in Qr code name',font=('Avalon',10,'bold'),bg='#000000',fg='#ffffff')
        command.pack()

        global get_name
        get_name=Entry(root1,width=30,bd=3,fg='#ffffff',bg='#000000')
        get_name.pack()
        root1.bind('<Return>',change_qr)
        confirm=Button(root1,text='confirm',command=change_qr,padx=25,bd=2).pack(side=BOTTOM)
main.bind('<Return>',name)
convert=Button(root,text='Convert',command=name,padx=25,bd=2,font=('Avalon',10,'bold')).grid(row=5,column=2)

#=============================================Changing to Icon=========================================================================================================================================================================

subroot=LabelFrame(main,padx=10,pady=10,bg='#000000')
subroot.pack(padx=20,pady=20,side=TOP,anchor=W)

def change_ico(event=None):
    raw_name=get_name.get()
    path='C:\\Users\\LENOVO\\Documents\\QR_codes\\'
    ico_name=path+raw_name
    img.save(qr_name +'.ico')
    info=tkinter.messagebox.showinfo('Complete','Converting to .ico extension is complete.')
    tk.destroy()


def choose_img():
    global img,tk
    open_file=tkinter.filedialog.askopenfilename(initialdir='C:\\Users\\LENOVO\\Downloads',title='Select an image',filetypes=(('png files','*.png'),('jpg files','*.jpg'),('all files','*.*')))
    img=Image.open(open_file)
    tk=Tk()
    
    tk.title('Icon Name')
    tk.geometry('300x150')
    tk.configure(bg='#000000')
    blank=Label(tk,text='',bg='#000000').pack()
    command=Label(tk,text='Icon Name',font=('Avalon',10,'bold'),bg='#000000',fg='#ffffff')
    command.pack()

    global get_name
    get_name=Entry(tk,width=30,bd=3,fg='#ffffff',bg='#000000')
    get_name.pack()
    tk.bind('<Return>',change_ico)
    confirm=Button(tk,text='confirm',command=change_ico,padx=25,bd=2).pack(side=BOTTOM)
    
blank=Label(subroot,text='',bg='#000000').grid(row=0,column=0,columnspan=3)

head=Label(subroot,text='Change to Icon Extension',font=('Avalon',12,'bold'),bg='#000000',fg='#ffffff').grid(row=1,column=0,columnspan=3)

blank=Label(subroot,text='',bg='#000000').grid(row=2,column=0)

intruction=Label(subroot,text='Choose image',bg='#000000',fg='#ffffff',font=('Avalon',10,'bold')).grid(row=3,column=0)

blank=Label(subroot,text='-',bg='#000000',fg='#ffffff',padx=20).grid(row=3,column=1)

get_image=Button(subroot,width=25,text='Fetch image',font=('Avalon',10,'bold'),command=choose_img,relief=SUNKEN,bd=3,bg='#ffffff')
get_image.grid(row=3,column=2)

blank=Label(subroot,text='',bg='#000000',fg='#ffffff').grid(row=4,column=0)

#==================================Changing to PDF==========================================================================================================================

pdfroot=LabelFrame(main,padx=10,pady=10,bg='#000000')
pdfroot.pack(padx=20,pady=20,side=TOP,anchor=W)

def change_pdf(event=None):
    global pdf_name
    raw_name=get_name.get()
    path='C:\\Users\\LENOVO\\Documents\\QR_codes\\'
    pdf_name=path+raw_name
    img = pdf_img.convert('RGB')
    img.save(pdf_name +'.pdf')
    info=tkinter.messagebox.showinfo('Complete','Converting to pdf file is complete.')
    pdftk.destroy()


def choose_img():
    global pdf_img,pdftk
    open_file=tkinter.filedialog.askopenfilename(initialdir='C:\\Users\\LENOVO\\Downloads',title='Select an image',filetypes=(('png files','*.png'),('jpg files','*.jpg'),('all files','*.*')))
    pdf_img=Image.open(open_file)
    pdftk=Tk()
    
    pdftk.title('PDF Name')
    pdftk.geometry('300x150')
    pdftk.configure(bg='#000000')
    blank=Label(pdftk,text='',bg='#000000').pack()
    command=Label(pdftk,text='pdf Name',font=('Avalon',10,'bold'),bg='#000000',fg='#ffffff')
    command.pack()

    global get_name
    get_name=Entry(pdftk,width=30,bd=3,fg='#ffffff',bg='#000000')
    get_name.pack()
    pdftk.bind('<Return>',change_pdf)
    confirm=Button(pdftk,text='confirm',command=change_pdf,padx=25,bd=2).pack(side=BOTTOM)
    
blank=Label(pdfroot,text='',bg='#000000').grid(row=0,column=0,columnspan=3)

head=Label(pdfroot,text='Change to pdf file',font=('Avalon',12,'bold'),bg='#000000',fg='#ffffff').grid(row=1,column=0,columnspan=3)

blank=Label(pdfroot,text='',bg='#000000').grid(row=2,column=0)

intruction=Label(pdfroot,text='Choose file',bg='#000000',fg='#ffffff',font=('Avalon',10,'bold')).grid(row=3,column=0)

blank=Label(pdfroot,text='-',bg='#000000',fg='#ffffff',padx=20).grid(row=3,column=1)

get_file=Button(pdfroot,width=27,text='Fetch file',padx=4,font=('Avalon',10,'bold'),command=choose_img,relief=SUNKEN,bd=3,bg='#ffffff')
get_file.grid(row=3,column=2)

blank=Label(pdfroot,text='',bg='#000000',fg='#ffffff').grid(row=4,column=0)

# Set the window geometry to fill the screen
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
main.geometry(f"{screen_width}x{screen_height}+0+0")

main.mainloop()