from tkinter import * 
import mysql.connector
import webbrowser
from datetime import date
import randfacts
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title('Studiandante')
root.geometry('500x500')

# Initialize frames
head_frame = Frame(root, bg="white")
main_frame = Frame(root, bg="pink")
# Initialize heading

app_name = Label(head_frame,pady=10, text='Studiandante',bg='black',fg='white',font=('Cascadia Mono',15,'bold'))

#functions
def title_text_focus(e):
    notes_text.focus_set()
def save_button_hover(e):
    count = 0
    for i in show_notes_frame.winfo_children():
        count+=1
    if count == 7 :
        save_button['bg']='white'
    else :
        save_button['bg']='#02198b'
def save_button_leave(e):
    save_button['bg']='#decdb9'
def  show_button_hover(e):
    show_button['bg']='#02198b'
def show_button_leave(e):
    show_button['bg']='#decdb9'
def  delete_button_hover(e):
    show_notes_delete['bg']='red'
def delete_button_leave(e):
    show_notes_delete['bg']='#decdb9'
def google_hover(e):
    if google['fg'] == '#f4c20d' :
        google['fg']='#34a853'
    elif google['fg'] == '#ea4335':
        google['fg'] = '#f4c20d'
    else :
        google['fg']='#ea4335'
def google_hover_leave(e):
    if google['fg'] == '#34a853' :
        google['fg']='#ea4335'
    elif google['fg'] == '#f4c20d':
        google['fg'] = '#34a853'
    else :
        google['fg']='#f4c20d'
def youtube_hover(e):
    youtube['fg'] = '#282828'
def youtube_hover_leave(e):
    youtube['fg'] ='red'

def delete_notes():
    notes_text.delete('1.0','end-1c')
    title_text.delete('1.0','end-1c')
    notes_text.focus_set()

def sql_table():
    sql=Tk()
    sql.geometry('500x500')
    sql.title('Notes Table')    
    connection = mysql.connector.connect(user='root',host='localhost',password='sherlock221b',database='shortnotes')
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM shortnotes ORDER BY Number DESC;")
    i=1
    main_frame = Frame(sql)
    main_frame.pack(fill=BOTH,expand=1)
    main_canvas = Canvas(main_frame)
    main_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    myscroll = ttk.Scrollbar(main_frame,orient=VERTICAL,command=main_canvas.yview)
    myscroll.pack(side=RIGHT,fill=Y)
    main_canvas.configure(yscrollcommand=myscroll.set)
    main_canvas.bind('<Configure>',lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))
    sub_frame = Frame(main_canvas)
    main_canvas.create_window((0,0), window = sub_frame,anchor='nw')
    for student in cursor: 
        frame = LabelFrame(sub_frame,bg='#afcbd9')
        topic_number = Label(frame,text='Number',padx=60,bg='#afcbd9')
        topic_number.grid(row=0,column=0)
        topic_date = Label(frame,text='Date',padx=60,bg='#afcbd9')
        topic_date.grid(row=0,column=1)
        topic_title = Label(frame,text='Title',padx=60,bg='#afcbd9')
        topic_title.grid(row=0,column=2)
        topic_notes = Label(frame,text='Notes',padx=60,bg='#afcbd9')
        topic_notes.grid(row=0,column=3)
        
        for j in range(len(student)):
            e = Label(frame, text=student[j],font=('Comic Sans Ms',11,'bold'),wraplength=800,bg='#afcbd9') 
            e.grid(row=i, column=j,padx=40,pady=10) 
        i=i+1
        frame.pack(side=TOP,anchor=N,fill =X)
    
    connection.commit()
    connection.close()
    sql.mainloop()


def delete_widgets() :
    for widget in show_notes_frame.winfo_children():
        widget.destroy()
    save_button['state']=NORMAL
    save_button['bg'] = '#decdb9'

def save() :
    if len(notes_text.get('1.0','end-1c'))<=151 and len(notes_text.get('1.0','end-1c'))!=0:
        show_notes = Label(show_notes_frame,bg = '#181716',fg='cyan',text=notes_text.get('1.0','end-1c'),font=('Comic Sans MS',11,'bold'),wraplength=450)
        show_notes.pack(fill=X,pady=5)
        counter = 0
        for widget in show_notes_frame.winfo_children():
            counter+=1
        if counter==7 :
            save_button['state']=DISABLED
            save_button['bg']='grey'
        #mysql table
        today = date.today()
        sql_date = str(today)
        connection = mysql.connector.connect(user='root',host='localhost',password='sherlock221b',database='shortnotes')

        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO shortnotes (Date,Title,Notes) VALUES ('{sql_date}','{title_text.get('1.0','end-1c')}','{notes_text.get('1.0','end-1c')}');")
        connection.commit()
        connection.close()
        delete_notes()
    elif len(notes_text.get('1.0','end-1c'))==0 :
        alert = messagebox.showerror('Error','Type in something first')
    else :
        alert = messagebox.showerror('Error','You wrote more than 150 characters')
    
    
#show notes
show_notes_mainframe = Frame(main_frame, bg='#B49561')
show_notes_title_frame = Frame(show_notes_mainframe,bg='#c6c6c6')
show_notes_title = Label(show_notes_title_frame,pady=10,text='Recently Added Notes',bg='#617db4',font=('Avalon',12,'bold'))
show_notes_delete_frame = Frame(show_notes_mainframe,bg='#c6c6c6')
show_notes_delete = Button(show_notes_delete_frame,bg='#decdb9',relief=RIDGE,text='Delete all',font=('Avalon',12,'bold'),command=delete_widgets)
show_notes_frame = Frame(show_notes_mainframe,bg='#B49561')
#show notes pack
show_notes_title_frame.pack(anchor=N, fill=X)
show_notes_mainframe.pack(side=LEFT, fill=BOTH, expand=True)
show_notes_mainframe.pack_propagate(False)
show_notes_frame.pack(fill=BOTH,expand=True)
show_notes_title.pack(fill=X,expand=True)
show_notes_delete_frame.pack(anchor=S,fill=X)
show_notes_delete.pack(fill=X,expand=True)

#take notes section
take_notes_frame = Frame(main_frame, bg='#617db4')
take_notes_title =Label(take_notes_frame,pady=10,text='Short Notes',font=('Avalon',12,'bold'),fg='black',bg='#B49561')
take_notes_discalimer = Label(take_notes_frame,text='The better you understand, shorter the notes are',font=('Avalon',10,'bold'),fg='black',bg='#617db4')
take_notes_ps = Label(take_notes_frame,text="* Don't write more than 150 characters.",font=('Avalon',9,),fg='black',bg='#617db4')
short_notes_title = Label(take_notes_frame,text='Title',font=('Avalon',10,'bold'),fg='black',bg='#617db4')
short_notes = Label(take_notes_frame,text='Notes',font=('Avalon',10,'bold'),fg='black',bg='#617db4')
title_text = Text(take_notes_frame,borderwidth=2,relief=GROOVE,bg='#decdb9',font=('Comic Sans MS',11,'bold'),height = 1,wrap=WORD,padx=10 ,pady=8)
notes_text = Text(take_notes_frame,borderwidth=2,relief=GROOVE,bg='#decdb9',font=('Comic Sans MS',11,'bold'),height = 4,wrap=WORD,padx=10 ,pady=8)
save_button = Button(take_notes_frame,text='Save',relief=RIDGE,font=('Avalon','11','bold'),bg='#decdb9',command=save)
show_button = Button(take_notes_frame,text='Show',relief=RIDGE,font=('Avalon','11','bold'),bg='#decdb9',command=sql_table)
#take notes packing
take_notes_frame.pack(side=LEFT, fill=BOTH, expand=True)
take_notes_frame.pack_propagate(False)
take_notes_title.pack(anchor = N,fill = X)
take_notes_discalimer.pack(anchor = N,fill = X)
take_notes_ps.pack(anchor = N,fill=X,pady=(0,10))
short_notes_title.pack(anchor=W,side=TOP,padx=10,pady=10)
title_text.pack(anchor = N, fill = X,pady=(0,20))
short_notes.pack(anchor=W,side=TOP,padx=10,pady=10)
notes_text.pack(anchor = N, fill = X,pady=(0,30))
save_button.pack(side=LEFT,anchor=N,fill=X,expand=True)
show_button.pack(side=LEFT,anchor=N,fill=X,expand=True)

#study_section
study_frame =Frame(main_frame, bg="#B49561")
study_title =Label(study_frame,pady=10,text='Self-Study',font=('Avalon',12,'bold'),bg='#617db4',fg='black')
#coding practice
def select_practice_code(event):
    for i in practice_code :
        if i == practice_code_values.get() :
            webbrowser.open_new_tab(f"https://www.{i.strip(' ')}.com")
            practice_code_values.set('Practice Coding')
practice_code = ['     leetcode      ',
                '      hackerrank      ',
                '      coderbyte      ',
                '      codechef      ',
                '      hackerearth      ']
practice_code_values = StringVar()
practice_code_values.set('Practice Coding')
practice_code_menu = OptionMenu(study_frame,practice_code_values, *practice_code,command=select_practice_code)
practice_code_menu.config(bg='#617db4',relief=FLAT,font=('Avalon',10,'bold'))
#Websites
def select_coding_websites(event):
    for i in coding_websites_dotcom :
        if i in coding_websites_values.get() :
            webbrowser.open_new_tab(f'https://www.{i}.com')
            coding_websites_values.set('Programming Websites')
    for j in coding_websites_dotorg :
        if j in coding_websites_values.get() :
            webbrowser.open_new_tab(f'https://www.{j}.org')
            coding_websites_values.set('Programming Websites')

coding_websites = ['       freecodecamp      ',
                    '      w3schools      ',
                    '      programiz      ',
                    '      tutorialspoint      ',
                    '      stackoverflow      ',
                    '      geeksforgeeks      ',
                    '      freecodecamp      ',
                    '      javatpoint      ']
coding_websites_dotcom = ['freecodecamp','w3schools','programiz','tutorialspoint','stackoverflow','javatpoint']
coding_websites_dotorg = ['geeksforgeeks','freecodecamp']
coding_websites_values = StringVar()
coding_websites_values.set('Programming Websites')
coding_websites_menu = OptionMenu(study_frame,coding_websites_values, *coding_websites,command=select_coding_websites)
coding_websites_menu.config(bg='#617db4',relief=FLAT,font=('Avalon',10,'bold'))
#youtubes
def select_youtube_channels(event):
    for i in youtube_channels :
        if i == youtube_channels_values.get() :
            webbrowser.open_new_tab(f'https://www.youtube.com/c/{i}')
            youtube_channels_values.set('Coding and Computer Science(Youtube)')
        if 'Mike Dane' in youtube_channels_values.get() :
            webbrowser.open_new_tab(f'https://www.youtube.com/c/GiraffeAcademy')
            youtube_channels_values.set('Coding and Computer Science(Youtube)')
        if 'Computerphile' in youtube_channels_values.get() :
            webbrowser.open_new_tab(f'https://www.youtube.com/user/computerphile')
            youtube_channels_values.set('Coding and Computer Science(Youtube)')
        if 'Corey Schafer' == youtube_channels_values.get() :
            webbrowser.open_new_tab(f'https://www.youtube.com/@coreyms')
            youtube_channels_values.set('Coding and Computer Science(Youtube)')


youtube_channels = ['codeSTACKr','Web Dev Simplified','Corey Schafer'
                    ,'Cyberspatial','David Bombal','Fireship'
                    ,'NeuralNine','Traversy Media','Computerphile'
                    ,'Telusko','Tech With Tim','NetworkChuck'
                    ,'Codemycom','Freecodecamp','cs50','Mike Dane']
youtube_channels_values = StringVar()
youtube_channels_values.set('Coding and Computer Science(Youtube)')
youtube_channels_menu = OptionMenu(study_frame,youtube_channels_values, *youtube_channels,command=select_youtube_channels)
youtube_channels_menu.config(bg='#617db4',relief=FLAT,font=('Avalon',10,'bold'))

#Learning websites
def select_learning_web(event):
    for i in learning_web_com :
        if i == learning_web_values.get() :
            webbrowser.open_new_tab(f'https://www.{i}.com')
            learning_web_values.set('Learning Websites')
    for j in learning_web_org :
        if j == learning_web_values.get():
            webbrowser.open_new_tab(f'https://www.{j}.org')
            learning_web_values.set('Learning Websites')
learning_web = ['Britanicca',
                'Udemy',
                'Mikedane',
                'Unbelievable-Facts',
                'TodayIFoundOut',
                'KnowledgeNuts',
                'TheFactSite',
                'Coursera',
                'Wikipedia',
                'KhanAcademy',
                'Edx']
learning_web_com = ['Britanicca','Udemy','Mikedane','Unbelievable-Facts','TodayIFoundOut','KnowledgeNuts','TheFactSite']
learning_web_org = ['Coursera','Wikipedia','KhanAcademy','Edx']
learning_web_values = StringVar()
learning_web_values.set('Learning Websites')
learning_web_menu = OptionMenu(study_frame,learning_web_values, *learning_web,command=select_learning_web)
learning_web_menu.config(bg='#617db4',relief=FLAT,font=('Avalon',10,'bold'))
#knowledge
def select_knowledge(event):
    for i in knowledge :
        if i == knowledge_values.get() :
            if 'Ted-ed' in knowledge_values.get() :
                webbrowser.open_new_tab(f'https://www.youtube.com/teded')
                knowledge_values.set('Be a Pantomath')
                break
            elif 'Today I Found Out' == knowledge_values.get() :
                webbrowser.open_new_tab(f'https://www.youtube.com/user/TodayIFoundOut')
                knowledge_values.set('Be a Pantomath')
                break
            webbrowser.open_new_tab(f'https://www.youtube.com/c/{knowledge[i]}')
            knowledge_values.set('Be a Pantomath')
          
knowledge = {'Bright side':'brightsideofficial','Ted-ed':'teded','Wired':'Wired','GQ':'GQ','Vsauce':'vsauce1','minutephysics':'minutephysics','Sci show':'Sci show'
            ,'Crash course':'Crash course','Asap science':'asapscience','Oversimplified':'oversimplified'
            ,'Kurzgesagt – In a Nutshell':'inanutshell','What if':'WhatifScienceShow','Simple History':'Simple History'
            ,'Vlogging Through History':'Vlogging Through History','Khan Academy':'khanacademy'
            ,'Kosmo':'Kosmooff','Destiny':'DestinySpace','Mr Supermole':'Mr Supermole','Veritasium':'veritasium'
            ,'Today I Found Out':'TodayIFoundOut','The Infographics Show':'TheInfographicsShowOFFICIAL'}

knowledge_values = StringVar()
knowledge_values.set('Be a Pantomath')
knowledge_menu = OptionMenu(study_frame,knowledge_values, *knowledge,command=select_knowledge)
knowledge_menu.config(bg='#617db4',relief=FLAT,font=('Avalon',10,'bold'))
#google and youtube
def google_search() :
    webbrowser.open_new_tab('https://')
google = Button(study_frame,text='Google',relief=RIDGE,font=('Avalon',11,'bold'),bg='#f1f3f4',fg='#f4c20d',command=google_search)
def youtube_search() :
    webbrowser.open_new_tab('https://www.youtube.com')
youtube = Button(study_frame,text='Youtube',relief=RIDGE,font=('Avalon',11,'bold'),bg='#f1f3f4',fg='#e62117',command=youtube_search)
#packing for study_section
study_title.pack(anchor= N,expand=True,fill=X)
practice_code_menu.pack(expand=True,fill=X)
coding_websites_menu.pack(expand=True,fill=X)
youtube_channels_menu.pack(expand=True,fill=X)
learning_web_menu.pack(expand=True,fill=X)
knowledge_menu.pack(expand=True,fill=X)
google.pack(anchor=S,expand=True,fill=X)
youtube.pack(anchor=S,expand=True,fill=X)

# Packing
head_frame.pack(fill=X)
main_frame.pack(fill=BOTH, expand=True)
app_name.pack(fill=X,pady=10)
study_frame.pack(side=LEFT, fill=BOTH, expand=True)
study_frame.pack_propagate(False)

#Fact generator
fact_frame = Frame(root, bg ='#0a0908',height = 200)
facts = randfacts.get_fact(filter_enabled=False)
text = Label(fact_frame,font=('Avalon',12,'bold'),fg='cyan',bg='#0a0908',text='Did you know :')
fact = Label(fact_frame,font=('Segoe Print',13,'bold'),fg='cyan',bg='#0a0908',text=facts,wraplength=600)
fact_frame.pack(fill=X)
fact_frame.pack_propagate(False)
text.pack(expand=True,pady=(30,0))
fact.pack(expand=True,pady=(20,30))
#bind button
save_button.bind('<Enter>',save_button_hover)
show_button.bind('<Enter>',show_button_hover)
show_notes_delete.bind('<Enter>',delete_button_hover)
show_button.bind('<Leave>',show_button_leave)
save_button.bind('<Leave>',save_button_leave)
show_notes_delete.bind('<Leave>',delete_button_leave)
title_text.bind('<Return>',title_text_focus)
google.bind('<Enter>',google_hover)
google.bind('<Leave>',google_hover_leave)
youtube.bind('<Enter>',youtube_hover)
youtube.bind('<Leave>',youtube_hover_leave)

# Set the window geometry to fill the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

root.mainloop()
