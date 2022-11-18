from tkinter import *




try:
    file_name = "Directories.txt"
    Directoryfile = open(file_name, "r")
    print(Directoryfile.read())
    Directoryfile.close()
except IOError:
    print("This file : (" + file_name + ") does not exist.")
    
  
window = Tk()
window.title('Im under the water Please Help me!')
window.iconbitmap('Iconss.ico')
window.geometry('955x600')
bg = PhotoImage(file="C:\\Programming Directory\\hindi.png")
    
my_label = Label(window, image = bg)
my_label.place(x = 0, y = 0, relwidth=1, relheight=1)
    
def frame_sentence():
    char_name = char_name_tf.get()
    descrip = descrip_tf.get()
    Type = Type_tf.get()
    Powers = Powers_tf.get()
    Origin = Origin_tf.get()
    
    display_tf.insert(0,f',CHARACTER NAME: {char_name}\n')
    display_tf.insert(1,f'DESCRIPTION: {descrip}\n')
    display_tf.insert(2,f'TYPE: {Type}\n')
    display_tf.insert(3,f'POWERS: {Powers}\n')
    display_tf.insert(4,f'ORIGIN: {Origin}\n')  
    
frame = LabelFrame(window,bg = "#005757", text="INFORMATION", font = ("Felix Titling", 10), padx = 40, pady = 40)
frame.pack(fill = "both")
frame.place(x=30, y=20)
    
    
    # CHARACTER NAME
Character_label = Label(frame, text='CHARACTER NAME',bg = "#005757", font = ("Felix Titling", 10), fg='black')
Character_label.pack(padx = 10, pady = 10)
char_name_tf = Entry(frame)
char_name_tf.pack()
    
    # DESCRIPTION
Description_label = Label(frame, text='DESCRIPTION',bg = "#005757", font = ("Felix Titling", 10), fg='black')
Description_label.pack(padx = 10, pady = 10)
descrip_tf = Entry(frame)
descrip_tf.pack()
    
    # TYPE
Type_label = Label(frame, text='TYPE',bg = "#005757", font = ("Felix Titling", 10), fg='black')
Type_label.pack(padx = 10, pady = 10)
Type_tf = Entry(frame)
Type_tf.pack()
    
    # POWER
Power_label = Label(frame, text='POWERS',bg = "#005757", font = ("Felix Titling", 10), fg='black')
Power_label.pack(padx = 10, pady = 10)
Powers_tf = Entry(frame)
Powers_tf.pack()
    
    
    # ORIGIN
Country_label = Label(frame, text='ORIGIN',bg = "#005757", font = ("Felix Titling", 10), fg='black')
Country_label.pack(padx = 10, pady = 10)
Origin_tf = Entry(frame)
Origin_tf.pack()
    
    # SAVE
Save_button = Button(frame, text='SAVE',bg = "#005757", font = ("Felix Titling", 10),relief=SOLID,padx = 40, pady = 4, command=frame_sentence)
Save_button.pack(padx = 10, pady = 10)
    
    #DISPLAY TEXT
display_tf = Listbox(window,bg = "#005757", width= 70, height = 25, font=('Felix Titling', 9), selectmode = EXTENDED)
display_tf.pack(pady = 5)
display_tf.place(x = 310, y = 50)
    
    

window.mainloop()
